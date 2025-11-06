# -*- coding: utf-8 -*-

import pandas as pd

class Extrator:

    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("O parametro df deve ser um pandas.DataFrame")
        self.df = df

    def extrair_por_local(self, local):

        if 'Local' not in self.df.columns:
            raise ValueError("O DataFrame nao possui a coluna 'Local'.")
        
        df_filtrado = self.df[self.df["Local"] == local].reset_index(drop=True)        
        
        return df_filtrado
    
    def somar_por_local_e_ano(self, local, ano):
        if "Local" not in self.df.columns:
            raise ValueError("O DataFrame nao possui a coluna 'Local'.")
        if str(ano) not in self.df.columns:
            raise ValueError(f"O DataFrame nao possui a coluna do ano '{ano}'.")
        
        df_local = self.df[self.df["Local"] == local]
        
        soma = df_local[str(ano)].sum()

        return soma


