# -*- coding: utf-8 -*-

import pandas as pd
from ql import QL

class Analise:

    def __init__(self, df_local: pd.DataFrame, df_ref: pd.DataFrame, calculadora: QL):
        self.df_local = df_local
        self.df_ref = df_ref
        self.calculadora = calculadora

        # Detecta automaticamente colunas numericas (anos)
        self.anos = [col for col in df_local.columns if col.isdigit()]
        self.df_ql = pd.DataFrame(index=df_local["Setor"])

    def executar(self) -> pd.DataFrame:
        for ano in self.anos:
            E_ki = self.df_local[ano].values
            E_k = self.df_ref[ano].values

            # Calculo vetorial simplificado com a nova CalculadoraQL
            ql_resultados = self.calculadora.calcular(E_ki, E_k)

            # Armazena o resultado no DataFrame
            self.df_ql[f"QL_{ano}"] = ql_resultados

        # Define o indice como o nome do setor
        self.df_ql.index = self.df_local["Setor"]
        return self.df_ql
