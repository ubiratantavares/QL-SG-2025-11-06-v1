# -*- coding: utf-8 -*-

from leitor import Leitor
from extrator import Extrator
from ql import QL
from analise import Analise
from visualizador import Visualizador

if __name__ == '__main__':

    # ler o arquivo csv com os dados setoriais do municipio e da regiao de referencia
    leitor = Leitor("dados.csv")
    df = leitor.ler()

    # criar o extrator para manipular os dados
    extrator = Extrator(df)

    # extrair dados do local especifico e da regiao de referencia
    df_sg = extrator.extrair_por_local("SG")
    df_rj = extrator.extrair_por_local("RJ")

    # criar o objeto que calcula o QL
    calculadora = QL()

    # criar o objeto de analise
    analise = Analise(df_sg, df_rj, calculadora)
    df_ql = analise.executar()

    # criar o objeto para exibir e visualizar os resultados
    visualizaor = Visualizador()
    visualizaor.exibir_resultados(df_ql, local="SG", referencia="RJ")
    visualizaor.plotar_evolucao(df_ql, local="SG")


