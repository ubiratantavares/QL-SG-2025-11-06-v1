# -*- coding: utf-8 -*-

import pandas as pd

class Leitor:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.data = None

    def ler(self):
        try:
            self.data = pd.read_csv(self.caminho_arquivo, delimiter=',', encoding='utf-8')
            return self.data
        except FileNotFoundError:
            print("Erro: arquivo nao encontrado.")
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")


