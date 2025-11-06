# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

class Visualizador:

    @staticmethod
    def exibir_resultados(df_ql: pd.DataFrame, local: str, referencia: str):
        print(f"Resultados do QL para {local} (Referencia: {referencia})")
        print("=" * 62)        
        print("QL > 1: Especializacao Relativa e QL < 1: Nao Especializacao")
        print("=" * 62)

        df_formatado = df_ql.copy()
        for col in df_formatado.columns:
            df_formatado[col] = df_formatado[col].apply(lambda x: f"{x:.4f}" if pd.notna(x) else "N/A")

        print(df_formatado.to_string())

    @staticmethod
    def plotar_evolucao(df_ql: pd.DataFrame, local: str):
        # Detecta dinamicamente as colunas de QL
        colunas_ql = [col for col in df_ql.columns if col.startswith("QL_")]

        # Filtra setores com QL > 1 em todos os anos
        df_especializados = df_ql[df_ql[colunas_ql].gt(1).all(axis=1)]

        if df_especializados.empty:
            print("\nNenhum setor apresentou QL > 1 em " \
            "todos os anos para plotagem.")
            return
        
        print(f"\nSetores com QL > 1 em todos os anos para {local}:")
        for setor in df_especializados.index:
            print(f"- {setor}")

        # Transpoe o DataFrame para formato de serie temporal (anos nas linhas)
        df_plot = df_especializados[colunas_ql].T
        df_plot.index = df_plot.index.str.replace("QL_", "")  # Remove o prefixo "QL_"

        # === Grafico ===
        plt.figure(figsize=(12, 7))
        for setor in df_plot.columns:
            plt.plot(df_plot.index, df_plot[setor], marker="o", linewidth=2, label=setor)

        plt.axhline(1, color="red", linestyle="--", linewidth=1, label="QL = 1 (Limite de Especializacao)")
        plt.title(f"Evolucao do Quociente Locacional: {local}", fontsize=14)
        plt.xlabel("Ano")
        plt.ylabel("Quociente Locacional (QL)")
        plt.legend(title="Setores Especializados", bbox_to_anchor=(1.05, 1), loc="upper left")
        plt.grid(True, linestyle=":", alpha=0.6)
        plt.tight_layout()
        plt.show()
