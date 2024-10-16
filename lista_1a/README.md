# CPS863 – Aprendizado de Máquina

Este repositório é utilizado para armazenar os trabalhos da disciplina de pós-graduação CPS863 – Aprendizado de Máquina.

## Informações da Disciplina

- **Programa:** Programa de Engenharia de Sistemas e Computação (PESC)
- **Instituto:** Instituto Alberto Luiz Coimbra de Pós-Graduação e Pesquisa de Engenharia (COPPE/UFRJ)
- **Professor:** Prof. Dr. Edmundo de Souza e Silva (PESC/COPPE/UFRJ)

# Questão 1
**(Recordação)**

Uma caixa contém três moedas: duas são normais e uma moeda falsa com duas caras (P(Ca)=1). Se você pegar uma moeda da caixa e jogá-la, qual a probabilidade de sair cara? Se você pegar uma moeda da caixa e jogá-la, e sair cara, qual a probabilidade de ser a moeda falsa?

# Questão 2
**(Material introdutório)**

Uma urna UA tem N = 1000 bolas sendo 25% delas azuis e o restante pretas. Uma outra urna UB também contém N = 1000 bolas, mas apenas 10% delas são azuis (e o restante pretas). As urnas são idênticas externamente, exceto por uma marcação, UA, UB, que permite a identificação de cada uma. Entretanto, essa identificação está na parte inferior das urnas, de forma que não é possível visualizar o rótulo, exceto se a urna for levantada.

- João tira (de olhos vendados) 2 bolas azuis de uma das urnas. Você vai ter que adivinhar a urna escolhida. Se a probabilidade de João escolher uma das urnas for a mesma, qual a aposta que você fará? Note que, para fazer a aposta, você precisa determinar qual a probabilidade das bolas serem provenientes da urna UA. Você tem confiança na sua aposta? Por que?
- Um amigo seu diz que João sabe a posição das urnas e escolhe a urna UA com probabilidade 0.15. Sua aposta mudaria? Você teria confiança na sua aposta? Justifique a resposta.

# Questão 3
Considere um dataset cujas amostras são obtidas independentemente a partir de uma distribuição discreta uniforme U(1, 5). Considere um dataset com as seguintes amostras: {2, 2, 4, 3, 2}.
1. Qual a verossimilhança (likelihood) de observar essas amostras?
2. E o log-likelihood?

# Questão 4
Assuma que você tem uma moeda viciada tal que com probabilidade p você obtém caras (H) e (1 - p) coroas (T). Você joga a moeda N vezes e obtém NH caras (e N - NH coroas, é claro).
1. Obtenha a função de verossimilhança L(θ|D) = p(D|θ) onde θ é o vetor de parâmetros. Qual é o valor de p(D|θ) se D = {HHT HT T HT T T} e p = 0.2? E se p = 0.6?
2. Para D dado no item acima, encontre p que otimiza o log-likelihood. De maneira geral, encontre p como uma função de N e NH para qualquer conjunto D dado.

# Questão 5
Suponha agora que suas amostras são obtidas ou de uma distribuição discreta U(1, 5) ou a partir de um dado (seis faces), sendo que todas as amostras são obtidas da mesma distribuição. Suponha que a probabilidade das amostras serem obtidas do dado é igual a p. Considere o conjunto de dados {2, 2, 4, 3, 2}, e seja p = 0.7.
1. Qual a likelihood das amostras serem retiradas a partir: (a) do dado se seis faces, ou (b) de uma U(1, 5) discreta?
2. Qual a distribuição posterior?
3. Uma vez que o dataset acima foi observado, qual a probabilidade de se retirar o número 5?
4. Uma vez que o dataset acima foi observado, qual a probabilidade de se retirar o número 6?
5. Qual o MLE?
6. Qual o MAP?
7. Caso p = 0.5, quais das respostas acima mudam de valor? Explique.

# Questão 6
Suponha agora que suas amostras são obtidas ou de uma distribuição discreta U(1, 5) ou a partir de um dado (seis faces) com probabilidade (1 - p) e p, respectivamente. Entretanto, nesta questão, a sequência pode conter amostras de ambas distribuições (mistura de distribuições). Considere o mesmo conjunto de dados {2, 2, 4, 3, 2}, e seja p = 0.7.
1. Qual a likelihood de observar essas amostras?
2. Uma vez que o dataset acima foi observado, qual a probabilidade de se retirar o número 5?
3. Uma vez que o dataset acima foi observado, qual a probabilidade de se retirar o número 6?
4. Qual a probabilidade de **todas** as amostras serem retiradas a partir: (a) do dado se seis faces, ou (b) de uma U(1, 5) discreta?
5. Calcule a função de likelihood para as amostras em função de p, o log likelihood e obtenha o valor de p que melhor explica o conjunto de dados. Comente a sua resposta.
6. Repita o item anterior, supondo que o conjunto de dados tem cardinalidade 20 e apenas uma única amostra tenha valor igual a 6.
