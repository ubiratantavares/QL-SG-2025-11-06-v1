# QL-SG-2025-11-06-v1

Análise da Especialização Setorial do Município de São Gonçalo (RJ) com base no Quociente Locacional (QL), utilizando dados da RAIS (2022–2024) e técnicas de Programação Orientada a 
Objetos (POO) em Python.

## 📌 Objetivo

Este projeto tem como finalidade identificar os setores econômicos especializados de São Gonçalo/RJ por meio do cálculo do Quociente Locacional (QL), contribuindo para o 
diagnóstico da estrutura produtiva local e subsidiando estratégias de desenvolvimento regional.

## 🧠 Fundamentação

A metodologia baseia-se na Teoria da Base Econômica e nos modelos espaciais de desenvolvimento regional, como o modelo Centro-Periferia e a causalidade circular cumulativa. 
O QL é utilizado como indicador indireto de especialização setorial, comparando a participação relativa de cada setor no município em relação ao estado do Rio de Janeiro.

## 🛠️ Metodologia

- **Fonte de dados**: RAIS (2022, 2023, 2024)

- **Variável de análise**: Emprego formal por setor

- **Região de estudo**: São Gonçalo/RJ

- **Região de referência**: Estado do Rio de Janeiro

- **Ferramenta analítica**: Quociente Locacional (QL)

## 🧱 Estrutura do Projeto

| Pasta/Arquivo         | Descrição |
|-----------------------|-----------|
| `dados/`              | Contém os arquivos CSV extraídos da RAIS |
| `scripts/leitor.py`   | Leitura e estruturação dos dados |
| `scripts/extrator.py` | Separação dos dados por região e setor |
| `scripts/ql.py`       | Cálculo do Quociente Locacional |
| `scripts/analise.py`  | Coordenação da análise temporal |
| `scripts/visualizador.py` | Geração de gráficos dos QLs |
| `scripts/app.py`      | Execução principal do projeto |
| `notebooks/`          | Análises exploratórias e testes |
| `docs/`               | Documentação complementar e gráficos gerados |

## 📊 Tecnologias Utilizadas

- **Python 3.10+**

- **Pandas** – manipulação de dados

- **NumPy** – operações vetoriais

- **Matplotlib / Seaborn** – visualização gráfica

- **POO + SOLID** – organização modular e escalável

## 📈 Resultados

Foram identificados 9 setores com especialização relativa consistente (QL > 1) ao longo dos três anos analisados:

- Material de Transporte  

- Madeira e Mobiliário  

- Indústria Química  

- Indústria Têxtil  

- Construção Civil  

- Comércio Varejista  

- Comércio Atacadista  

- Transporte e Comunicações  

- Ensino

## 📚 Referências

[1] Johann Heinrich Von Thünen. Der Isolierte Staat in Beziehung auf Landwirstschaft und Nationalö-
komI’e. 1826.

[2] Alfred Weber. Theory of the Location of Industry. University of Chicago Press, Chicago, 1928.

Tradução de C. J. Friedrich da obra original Über den Standort des Industrien, publicada em 1909.

[3] Gunnar Myrdal. Economic Theory and Under-developed Regions. Duckworth, London, 1957.

[4] John Friedmann. A general theory of polarized development. Readings in Urban Economics, 1972.

## 📬 Contato

Para dúvidas, sugestões ou colaborações acadêmicas, entre em contato com o autor:

**Ubiratan da Silva Tavares**  

Email: [ust1973@gmail.com]  

Instituição: [Universidade Federal Rural do Rio de Janeiro]
