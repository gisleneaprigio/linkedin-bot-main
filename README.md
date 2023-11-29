# linkedin-bot-main

### Introdução

A busca de emprego se mostra desafiadora em um mercado aquecido com o aumento da disponibilização de dados e tecnologia. Este trabalho realizou a análise de vagas de empresas por meio da técnica de “web scraping”. Foram aplicados critérios de filtros de vagas e localização para selecionar as vagas, o código de “web scraping” foi desenvolvido em Python e ocorreu a partir do processo de coleta, processamento e análise dos dados que permitiu avaliar as tendências de contratação em diferentes setores e regiões geográficas. O trabalho proporcionou o conhecimento de diversas ferramentas e recursos para coleta e análise de dados,  e a identificação de tendências de mercado podendo ser relevante em um cenário pós-pandemia, onde os formatos de trabalho estão passando por mudanças. O algoritmo utilizado trouxe como resultado a possibilidade de pesquisa focado no formato de trabalho e localização, podendo ser utilizado como ferramenta de pesquisa para candidatos a vagas de emprego.     

### Objetivo

A análise dos dados coletados pode oferecer insights sobre as tendências e formatos de trabalho no mercado de trabalho, auxiliando profissionais e empresas na tomada de decisões estratégicas. Além disso, o trabalho tem por objetivo analisar vagas de emprego utilizando as técnicas de “web scraping” e para a disseminação do conhecimento sobre essa ferramenta poderosa de coleta de dados em larga escala. Esse método é replicável e pode ser evoluído até como uma API, para ser utilizada como ferramenta em um aplicativo. Foram discutidas as vantagens e desafios dessa abordagem, assim como as implicações éticas e legais da coleta de dados em redes sociais. Por fim, foi contribuído para o entendimento da aplicação da técnica de web scraping na análise de vagas de emprego em redes sociais, evidenciando seu potencial como ferramenta estratégica para candidatos e empresas no atual cenário do mercado de trabalho. Nesta conjuntura, foi coletado itens estratégicos com algumas perguntas que foram utilizadas como guia para a análise realizadas, por exemplo: 

•	Quais são as cidades com mais vagas?

•	Quantas vagas de analista de dados híbridas temos em São Paulo e Região?

•	Quais as cidades que possuem diversidade de formatos de trabalho?

•	Qual formato de trabalho é mais comum para Cientistas de Dados em São Paulo e Região?

•	Qual formato de trabalho é mais comum para Cientista de Dados no Brasil?


### Metodologia


 ![image](https://github.com/gisleneaprigio/linkedin-bot-main/assets/17745481/7f427c85-f4d5-475d-ada8-0b7ea81ce5c7)


     Conforme a Figura foi utilizado o código em Python na versão 3, com as seguintes bibliotecas: 

●	Criação do código de “web scraping”: Utilizadas as bibliotecas BeautifulSoup, Requests e Pandas para coletar os dados das vagas de emprego. Foi utilizado o método de “web scraping” para coletar os dados de vagas disponíveis nas páginas da plataforma LinkedIn, em tempo real. 

●	Processamento dos dados: Os dados coletados serão organizados em um banco de dados com a utilização da biblioteca Pandas. 

●	Análise e Visualização dos Dados: A partir dos dados organizados no banco de dados, foram gerados gráficos para ilustrar as tendências de contratação em cada formato de trabalho em diferentes setores e regiões geográficas. Será utilizado a biblioteca Matplot para a criação dos gráficos e análise estatística para determinação dos resultados. Para obter os melhores resultados de visualização e análises em relação às variáveis de formato de trabalho será utilizado também o Power BI gerando gráficos a partir do “dataframes” colhidos através do recurso de “web scraping” da página.


### Resultados

No gráfico da figura abaixo, é possível observar que o algoritmo coletou localizações que podem ser consideradas com redundância como “São Paulo, SP”, “São Paulo, Brasil” e “São Paulo e Região”. Também existem casos de localização em que um registro está contido dentro do outro, como São Paulo e Região” e a cidade de “Barueri”.  

![image](https://github.com/gisleneaprigio/linkedin-bot-main/assets/17745481/66047f68-56f4-4e58-8665-f3f472a89407)

Utilizando a variável “cargo”, é possível observar o universo de palavras utilizadas nos cadastros dos registros, que vão desde palavras ligadas à função, cargo, localização, formato de trabalho e ferramentas utilizadas na vaga, mas ainda com evidência nas palavras utilizadas na pesquisa da vaga.

![image](https://github.com/gisleneaprigio/linkedin-bot-main/assets/17745481/43ace250-4b0a-4138-866d-66f249f1145b)


A Figura 8 apresenta a localização, utilizando as 10 primeiras cidades com mais vagas coletadas, assim com o primeiro cenário também podemos verificar que há duplicidade de localização, baseado no cadastro da vaga e agrupamento de cidades como Barueri no conjunto “São Paulo e Região”.

![image](https://github.com/gisleneaprigio/linkedin-bot-main/assets/17745481/0322fd26-14b3-45c6-b4de-1b3bc36b5ba0)







 
