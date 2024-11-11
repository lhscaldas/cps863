# CPS863 – Aprendizado de Máquina

Este repositório é utilizado para armazenar os trabalhos da disciplina de pós-graduação CPS863 – Aprendizado de Máquina.

## Informações da Disciplina

- **Programa:** Programa de Engenharia de Sistemas e Computação (PESC)
- **Instituto:** Instituto Alberto Luiz Coimbra de Pós-Graduação e Pesquisa de Engenharia (COPPE/UFRJ)
- **Professor:** Prof. Dr. Edmundo de Souza e Silva (PESC/COPPE/UFRJ)

## Conteúdo da Disciplina

- Inferência probabilística
- Estimativa por máxima verossimilhança (maximum likelihood estimation)
- Noções de aprendizado de máquina bayesiano
- Modelos gaussianos
- Classificadores, clusterização
- Modelos lineares
- Noções básicas de teoria de informação
- Aprendizado supervisionado e não supervisionado
- Hidden Markov models
- Processos de decisão de Markov
- Aprendizado por reforço
- Teoria de decisão bayesiana
- Noções de métodos Markov chain Monte Carlo (MCMC)
- Noções de redes neurais profundas

## Listas

1. [Exercício do Slide](exercicio_do_slide)
O objetivo deste exercício é adivinhar qual conjunto de dados foi gerado por uma moeda justa e qual foi gerado por uma moeda viciada, onde a probabilidade de obter "cara" é de 0,30. Além disso, deve-se considerar se a resposta muda ao saber que a probabilidade de usar a moeda viciada é de 1/3 e analisar o que acontece se o número de lançamentos (N) aumentar.

2. [Lista de Exercícios 1a](lista_1a/lista_1a.pdf)
O objetivo desta lista é avaliar os conhecimentos dos alunos sobre probabilidade, garantindo que todas as respostas sejam devidamente comentadas, detalhando os passos necessários para se chegar à solução. É importante que os alunos não procurem soluções na internet, em livros ou no ChatGPT, pois o intuito é que cada um avalie seu próprio conhecimento. Mesmo que o aluno já conheça o problema, é recomendado tentar resolvê-lo sozinho para identificar melhor os tópicos que ainda não domina completamente. Durante a resolução, é essencial anotar as dúvidas encontradas para discutir em classe. A explicação dos passos realizados é mais importante do que a referência ao código em si.

3. [Lista de Exercícios 1b](lista_1b/lista_1b.pdf)
O objetivo da lista 1b é resolver questões relacionadas à detecção de ataques DDoS em uma rede de ISP, utilizando um classificador implementado em roteadores residenciais que fornece, a cada janela de 5 minutos, uma indicação da ocorrência ou não de um ataque. O ISP coleta amostras aleatórias de um número grande de roteadores e precisa determinar, com base nessas amostras e usando correlação espacial, se está ocorrendo um ataque DDoS em sua rede, mesmo sabendo que os classificadores dos roteadores não são completamente confiáveis. O exercício foi simplificado a partir de um problema abordado na Seção H do artigo de referência.

4. [Lista de Exercícios 2](lista_2/lista_2.pdf)
O objetivo desta lista de exercícios é explorar técnicas de análise de dados e modelos probabilísticos em Machine Learning, focando em mistura de gaussianas e imputação de dados. A primeira questão envolve a visualização de dados e o ajuste de modelos de mistura gaussiana com diferentes números de componentes, além da avaliação de qual modelo melhor representa o conjunto de dados utilizando critérios como AIC e BIC. A segunda questão aborda a imputação de valores ausentes em um dataset, exigindo uma explicação detalhada dos passos matemáticos e a implementação do processo de imputação.

5. [Lista de Exercícios 3](lista_3/lista_3.pdf)
O objetivo desta lista de exercícios é explorar e comparar diferentes abordagens de classificação e modelagem de dados. Na primeira questão, o foco está em ajustar três modelos distintos (dois modelos de mistura de Gaussianas e um de regressão logística) em um conjunto de dados para examinar o desempenho de cada um na classificação com base em log-likelihood. Na segunda questão, o objetivo é utilizar o classificador Naive Bayes para identificar mensagens de texto como "spam" ou "ham", avaliando o impacto da suposição de independência das palavras e o desempenho do modelo em métricas como precisão e revocação.

6. [Lista de Exercícios 4](lista_4/lista_4.pdf)
O objetivo específico desta lista é explorar e aplicar técnicas de aprendizado não supervisionado e modelagem probabilística em contextos práticos. Na primeira questão, o objetivo é implementar o algoritmo de Expectation-Maximization (EM) para classificar usuários com base em suas preferências por gêneros de filmes, utilizando o modelo Naive Bayes para estimar a probabilidade de cada usuário pertencer a uma das duas classes. Na segunda questão, o foco é modelar e analisar o movimento de um robô em um ambiente restrito através de Cadeias de Markov, investigando a matriz de transição de estados, o cálculo de probabilidades de localização após um intervalo de tempo e o comportamento do robô ao longo do tempo.