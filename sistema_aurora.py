# Carlos Henrique De Godoy Santos -- RM: 569735
# Fase 3: Implementação de um Sistema Inteligente para Gerenciamento de Recursos em uma Colônia Espacial

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
import numpy as np


class GerenciadorHabitat:

    def __init__(self):
        self.estado = {
            "rede_eletrica": {
                "fontes": {
                    "fotovoltaica": {"potencia_kw": 0.0, "ativo": True},
                    "aerodinamica": {"potencia_kw": 0.0, "ativo": True},
                },
                "banco_baterias": {"nivel_carga": 100.0, "condicao": "nominal"},
            },
            "ambiente": {"temp_interna": 21.5, "temp_externa": -55.0, "velocidade_vento": 0.0},
            "operacoes": {
                "subsistemas": {
                    "suporte_vida": {"demanda_kw": 30.0, "criticidade": "alta", "ativo": True},
                    "lab_pesquisa": {"demanda_kw": 20.0, "criticidade": "media", "ativo": True},
                    "unidade_extracao": {"demanda_kw": 20.0, "criticidade": "baixa", "ativo": True},
                },
                "demanda_agregada": 70.0,
            },
            "historico_telemetria": {"registro_vento": [8.0, 10.0, 12.0], "registro_potencia": [20.0, 25.0, 30.0]},
        }

    def avaliar_seguranca_rede(self, previsao_tempo_ruim=False):
        fontes_energia = self.estado["rede_eletrica"]["fontes"]
        suprimento_total = fontes_energia["fotovoltaica"]["potencia_kw"] + fontes_energia["aerodinamica"]["potencia_kw"]

        bateria_pct = self.estado["rede_eletrica"]["banco_baterias"]["nivel_carga"]
        demanda_atual = self.estado["operacoes"]["demanda_agregada"]

        print("--- TELEMETRIA EM TEMPO REAL ---")
        print(f"Suprimento: {suprimento_total} kW | Demanda: {demanda_atual} kW")
        print(f"Baterias: {bateria_pct}%")

        if bateria_pct < 50.0 and demanda_atual > suprimento_total and previsao_tempo_ruim:
            self.estado["rede_eletrica"]["banco_baterias"]["condicao"] = "emergencia"

            for nome, componente in self.estado["operacoes"]["subsistemas"].items():
                if componente["criticidade"] != "alta":
                    componente["ativo"] = False

            demanda_suporte_vida = self.estado["operacoes"]["subsistemas"]["suporte_vida"]["demanda_kw"]
            self.estado["operacoes"]["demanda_agregada"] = demanda_suporte_vida

            return "PROCESSO CRÍTICO: Modo de emergência ativado. Suprimento restrito ao suporte vital!"

        if demanda_atual > suprimento_total:
            self.estado["rede_eletrica"]["banco_baterias"]["condicao"] = "alerta"
            return "ATENÇÃO: Carga consumida excede a gerada. Monitore o descarregamento."

        if suprimento_total > demanda_atual:
            self.estado["rede_eletrica"]["banco_baterias"]["condicao"] = "nominal"
            return "OTIMIZAÇÃO: Excedente detectado. Direcionando carga para acumuladores."

        self.estado["rede_eletrica"]["banco_baterias"]["condicao"] = "nominal"
        return "Estabilização sistêmica ideal alcançada."


def executar_modelo_preditivo(historico_x, historico_y, leitura_atual):
    atributos_treino = np.array(historico_x).reshape(-1, 1)
    alvo_treino = np.array(historico_y)

    regressor = LinearRegression()
    regressor.fit(atributos_treino, alvo_treino)

    predicoes_treino = regressor.predict(atributos_treino)

    valor_mse = mean_squared_error(alvo_treino, predicoes_treino)
    valor_r2 = r2_score(alvo_treino, predicoes_treino)

    alvo_predicao = np.array([[leitura_atual]])
    producao_estimada = regressor.predict(alvo_predicao)[0]

    print("--- DIAGNÓSTICO DO MODELO ---")
    print(f"Inclinação (Coef): {regressor.coef_[0]:.2f}")
    print(f"Intercepto: {regressor.intercept_:.2f}")
    print(f"MSE: {valor_mse:.2f}")
    print(f"R² Score: {valor_r2:.2f}")

    return producao_estimada


if __name__ == "__main__":
    print("STARTUP DO NÚCLEO OPERACIONAL - ESTAÇÃO AURORA")

    habitat = GerenciadorHabitat()

    leitura_anemometro = 11.0
    habitat.estado["ambiente"]["velocidade_vento"] = leitura_anemometro
    print(f"\n[METEOROLOGIA] Velocidade do vento registrada: {leitura_anemometro} m/s")

    historico_v = habitat.estado["historico_telemetria"]["registro_vento"]
    historico_p = habitat.estado["historico_telemetria"]["registro_potencia"]

    potencia_eolica_calculada = executar_modelo_preditivo(historico_v, historico_p, leitura_anemometro)

    habitat.estado["rede_eletrica"]["fontes"]["aerodinamica"]["potencia_kw"] = potencia_eolica_calculada
    habitat.estado["rede_eletrica"]["fontes"]["fotovoltaica"]["potencia_kw"] = 5.0

    print(f"\n[PROJEÇÃO] Potência Eólica Estimada: {potencia_eolica_calculada:.2f} kW")

    habitat.estado["rede_eletrica"]["banco_baterias"]["nivel_carga"] = 85.0
    resposta_sistema = habitat.avaliar_seguranca_rede(previsao_tempo_ruim=False)
    print(f"[RESPOSTA]: {resposta_sistema}")

    print("\n[EVENTO CLIMÁTICO] Alerta emitido: Tempestade de poeira severa em curso.")
    print("[EVENTO CLIMÁTICO] Restrição severa em painéis fotovoltaicos detectada.")

    habitat.estado["rede_eletrica"]["banco_baterias"]["nivel_carga"] = 42.0
    habitat.estado["rede_eletrica"]["fontes"]["fotovoltaica"]["potencia_kw"] = 2.0

    resposta_critica = habitat.avaliar_seguranca_rede(previsao_tempo_ruim=True)
    print(f"[RESPOSTA]: {resposta_critica}")

    print("\n[AUDITORIA] Painel de Integridade dos Subsistemas:")
    mapeamento_status = {True: "ATIVADO", False: "DESATIVADO"}

    for nome_modulo, config in habitat.estado["operacoes"]["subsistemas"].items():
        status_atual = mapeamento_status[config["ativo"]]
        print(
            f" -> Unidade: {nome_modulo.upper()} | Classe: {config['criticidade'].upper()} | Status: {status_atual}"
        )

    demanda_atualizada = habitat.estado["operacoes"]["demanda_agregada"]
    print(f"\n[AUDITORIA] Carga total consolidada na rede: {demanda_atualizada} kW")