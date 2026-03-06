# Projeto de Análise Exploratória de Dados sobre o impacto do COVID-19 no ENEM Amazonas (2019-2023)

Este projeto realiza uma Análise Exploratória de Dados (EDA) para investigar como o decorrer da pandemia do COVID-19 afetou o desempenho dos estudantes do Amazonas no ENEM. A análise utiliza uma lente socioeconômica para destacar as disparidades enfrentadas por alunos em situação de vulnerabilidade.

A análise foi estruturada em 4 hipóteses principais: 1 - O impact da pandemia no volume de inscrições; 2 - A relação entre a falta de acesso de internet e taxa de abstenção; 3 e 4 - Comparativo de desempenho entre escola pública e privada, com foco na renda dos candidatos.

## Contexto necessário: Por que o Amazonas?
O Amazonas apresentou um dos cenários mais críticos da pandemia no Brasil: com crises no sistema de saúde e de oxigênio de Manaus em 2021, além de ter datado em maio de 2020 como sendo o estado de 13 cidades entre as 20 com maior incidências de casos do COVID-19 no Brasil. Este estudo e projeto busca compreender o impacto desses eventos no setor educacional, focando em abstenção, acesso à tecnologia e desempenho acadêmico.

## Tecnologias usadas:
**Linguagem**: Python
**Bibliotecas**: 
  *Pandas*: utilizado para o processo de ETL (extração, transformação e carga), incluindo o processamento eficiente de volumes grandes de dados por leitura em blocos (chunksize) para otimização de memória.
  *Matplotlib e Seaborn*: usados para criação de gráficos estatísticos e sua visualização.

## Principais Insights:
**Crise e Inscrições:** Houve uma queda acentuada no volume de inscritos no ENEM, correlacionada diretamente aos períodos de pico da crise sanitária no estado.
**Barreira Digital:** A ausência de acesso à Internet foi um fator determinante na taxa de abstenção, evidenciando que a medida de ensino à distância não atingiu a todos da mesma forma: alunos sem acesso à internet mantiveram consistentemente uma taxa de abstenção maior do que alunos com acesso.
**Desigualdade de Desempenho entre escolas públicas e privadas:** Enquanto todos alunos independente da rede e situação socioeconômica obtiveram uma queda significativa na média e mediana das notas em 2021, os alunos de maior renda e de escola privada conseguiram uma recuperação estável com aumento constante da nota, contrastando com os alunos de baixa renda e escola pública que não obtiveram uma recuperação consistente em suas médias.

## Fonte dos dados:
Foram coletados e filtrados os Microdados do ENEM (INEP) referente aos anos de 2019 a 2023, visando pegar apenas as colunas relevantes para o projeto e apenas alunos que realizaram a prova no estado Amazonas.
