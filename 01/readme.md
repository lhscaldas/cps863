# Análise de Lançamentos de Moeda

Este trabalho descreve a análise de dados de lançamentos de moeda para determinar se os dados foram gerados por uma moeda justa (p = 0.5) ou uma moeda viciada (p = 0.30 para caras). A seguir, apresentamos a explicação do que está sendo feito no código e algumas simulações com diferentes valores de N.

## Explicação do Código

1. **Geração de Dados de Moeda Viciada:**
```python
import random

def generate_biased_coin_data(N, p=0.3):
    return [1 if random.random() < p else 0 for _ in range(N)]
```
   - Gera uma lista de N lançamentos de moeda onde cada lançamento tem uma probabilidade `p` de ser cara (representado por 1) e `1-p` de ser coroa (representado por 0).

2. **Cálculo da Verossimilhança:**
```python
def likelihood(data, p):
    heads = sum(data)
    tails = len(data) - heads
    return (p ** heads) * ((1 - p) ** tails)
```
   - Calcula a verossimilhança dos dados observados dado uma probabilidade `p`.

3. **Inferência Bayesiana:**
```python
def bayesian_inference(data, prior_fair=2/3, prior_biased=1/3):
    likelihood_fair = likelihood(data, 0.5)
    likelihood_biased = likelihood(data, 0.3)
    
    posterior_fair = likelihood_fair * prior_fair
    posterior_biased = likelihood_biased * prior_biased
    
    normalization_constant = posterior_fair + posterior_biased
    
    posterior_fair /= normalization_constant
    posterior_biased /= normalization_constant
    
    return posterior_fair, posterior_biased
``` 
   - Utiliza o teorema de Bayes para atualizar as probabilidades a priori com base nos dados observados e calcular as probabilidades posteriores.

4. **Simulação:**
```python
N = 10  # Número de lançamentos de moeda
for _ in range(5):
    data = generate_biased_coin_data(N, p=0.3)
    print(data)
    posterior_fair, posterior_biased = bayesian_inference(data)

    print(f"Probabilidade posterior de moeda justa: {posterior_fair:.2f}")
    print(f"Probabilidade posterior de moeda viciada: {posterior_biased:.2f}")

    if posterior_fair > posterior_biased:
        print("Os dados são mais provavelmente gerados por uma moeda justa.")
    else:
        print("Os dados são mais provavelmente gerados por uma moeda viciada.")
```
   - Gera N lançamentos de moeda com uma probabilidade `p` para caras.
   - Calcula as probabilidades posteriores de os dados serem gerados por uma moeda justa ou viciada.
   - Compara as probabilidades posteriores para determinar qual hipótese é mais provável.
   - O loop é rodado 5 vezes para ver melhor como a inferência se comporta com a aleatoriedade.

## Simulações com Diferentes Valores de N e p

### Simulação com N = 10

Nesta simulação, geramos 10 lançamentos de moeda e calculamos as probabilidades posteriores de os dados serem gerados por uma moeda justa ou viciada.

#### p = 0.3 (moeda viciada)
[0, 0, 0, 0, 1, 0, 0, 1, 0, 0]

Probabilidade posterior de moeda justa: 0.27

Probabilidade posterior de moeda viciada: 0.73

Os dados são mais provavelmente gerados por uma moeda viciada.

[0, 0, 0, 0, 0, 1, 0, 1, 1, 0]

Probabilidade posterior de moeda justa: 0.47

Probabilidade posterior de moeda viciada: 0.53

Os dados são mais provavelmente gerados por uma moeda viciada.

[0, 1, 0, 0, 0, 0, 0, 0, 1, 1]

Probabilidade posterior de moeda justa: 0.47

Probabilidade posterior de moeda viciada: 0.53

Os dados são mais provavelmente gerados por uma moeda viciada.

[1, 1, 0, 1, 1, 0, 0, 0, 0, 0]

Probabilidade posterior de moeda justa: 0.67

Probabilidade posterior de moeda viciada: 0.33

Os dados são mais provavelmente gerados por uma moeda justa.

[0, 0, 0, 0, 0, 0, 0, 1, 1, 0]

Probabilidade posterior de moeda justa: 0.27

Probabilidade posterior de moeda viciada: 0.73

Os dados são mais provavelmente gerados por uma moeda viciada.

#### p = 0.5 (moeda justa)
[0, 1, 1, 0, 0, 1, 1, 0, 0, 0]

Probabilidade posterior de moeda justa: 0.67

Probabilidade posterior de moeda viciada: 0.33

Os dados são mais provavelmente gerados por uma moeda justa.

[1, 0, 0, 1, 1, 0, 1, 1, 0, 1]

Probabilidade posterior de moeda justa: 0.92

Probabilidade posterior de moeda viciada: 0.08

Os dados são mais provavelmente gerados por uma moeda justa.

[0, 1, 1, 1, 0, 1, 0, 0, 1, 0]

Probabilidade posterior de moeda justa: 0.83

Probabilidade posterior de moeda viciada: 0.17

Os dados são mais provavelmente gerados por uma moeda justa.

[0, 0, 0, 0, 0, 0, 0, 0, 1, 1]

Probabilidade posterior de moeda justa: 0.27

Probabilidade posterior de moeda viciada: 0.73

Os dados são mais provavelmente gerados por uma moeda viciada.

[0, 1, 1, 0, 0, 1, 1, 1, 1, 1]

Probabilidade posterior de moeda justa: 0.96

Probabilidade posterior de moeda viciada: 0.04

Os dados são mais provavelmente gerados por uma moeda justa.

### Simulação com N = 50

Nesta simulação, geramos 50 lançamentos de moeda e calculamos as probabilidades posteriores de os dados serem gerados por uma moeda justa ou viciada.

#### p = 0.3 (moeda viciada)
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Probabilidade posterior de moeda justa: 0.00

Probabilidade posterior de moeda viciada: 1.00

Os dados são mais provavelmente gerados por uma moeda viciada.

[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

Probabilidade posterior de moeda justa: 0.01

Probabilidade posterior de moeda viciada: 0.99

Os dados são mais provavelmente gerados por uma moeda viciada.

[0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1]

Probabilidade posterior de moeda justa: 0.07

Probabilidade posterior de moeda viciada: 0.93

Os dados são mais provavelmente gerados por uma moeda viciada.

[0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

Probabilidade posterior de moeda justa: 0.00

Probabilidade posterior de moeda viciada: 1.00

Os dados são mais provavelmente gerados por uma moeda viciada.

[1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1]

Probabilidade posterior de moeda justa: 0.07

Probabilidade posterior de moeda viciada: 0.93

Os dados são mais provavelmente gerados por uma moeda viciada.
#### p = 0.5 (moeda justa)
[0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0]

Probabilidade posterior de moeda justa: 1.00

Probabilidade posterior de moeda viciada: 0.00

Os dados são mais provavelmente gerados por uma moeda justa.

[0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0]

Probabilidade posterior de moeda justa: 1.00

Probabilidade posterior de moeda viciada: 0.00

Os dados são mais provavelmente gerados por uma moeda justa.

[1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1]

Probabilidade posterior de moeda justa: 1.00

Probabilidade posterior de moeda viciada: 0.00

Os dados são mais provavelmente gerados por uma moeda justa.

[0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1]

Probabilidade posterior de moeda justa: 1.00

Probabilidade posterior de moeda viciada: 0.00

Os dados são mais provavelmente gerados por uma moeda justa.

[0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0]

Probabilidade posterior de moeda justa: 1.00

Probabilidade posterior de moeda viciada: 0.00

Os dados são mais provavelmente gerados por uma moeda justa.


### Simulação com N = 100

Nesta simulação, geramos 100 lançamentos de moeda e calculamos as probabilidades posteriores de os dados serem gerados por uma moeda justa ou viciada.

#### p = 0.3 (moeda viciada)
[1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Probabilidade posterior de moeda justa: 0.00

Probabilidade posterior de moeda viciada: 1.00

Os dados são mais provavelmente gerados por uma moeda viciada.

[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1]

Probabilidade posterior de moeda justa: 0.00

Probabilidade posterior de moeda viciada: 1.00

Os dados são mais provavelmente gerados por uma moeda viciada.

[1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]

Probabilidade posterior de moeda justa: 0.17

Probabilidade posterior de moeda viciada: 0.83

Os dados são mais provavelmente gerados por uma moeda viciada.

[1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1]

Probabilidade posterior de moeda justa: 0.02

Probabilidade posterior de moeda viciada: 0.98

Os dados são mais provavelmente gerados por uma moeda viciada.

[0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1]

Probabilidade posterior de moeda justa: 0.00

Probabilidade posterior de moeda viciada: 1.00

Os dados são mais provavelmente gerados por uma moeda viciada.

#### p = 0.5 (moeda justa)
[0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1]

Probabilidade posterior de moeda justa: 1.00

Probabilidade posterior de moeda viciada: 0.00

Os dados são mais provavelmente gerados por uma moeda justa.

[0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1]

Probabilidade posterior de moeda justa: 0.93

Probabilidade posterior de moeda viciada: 0.07

Os dados são mais provavelmente gerados por uma moeda justa.

[1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1]

Probabilidade posterior de moeda justa: 1.00

Probabilidade posterior de moeda viciada: 0.00

Os dados são mais provavelmente gerados por uma moeda justa.

[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]

Probabilidade posterior de moeda justa: 1.00

Probabilidade posterior de moeda viciada: 0.00

Os dados são mais provavelmente gerados por uma moeda justa.

[1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0]

Probabilidade posterior de moeda justa: 0.52

Probabilidade posterior de moeda viciada: 0.48

Os dados são mais provavelmente gerados por uma moeda justa.

## Conclusão

À medida que o número de observações (N) aumenta, o poder estatístico do teste aumenta, tornando mais fácil distinguir entre a moeda justa e a moeda viciada. Isso ocorre devido à Lei dos Grandes Números, que afirma que a média amostral convergirá para o valor esperado à medida que o tamanho da amostra aumenta.

Além disso, conforme N aumenta, a influência das probabilidades a priori diminui. Isso significa que, com um número maior de observações, os dados observados têm um impacto maior na determinação das probabilidades posteriores. Em outras palavras, as evidências fornecidas pelos dados se tornam mais dominantes, e a escolha das probabilidades a priori se torna menos relevante. Isso é uma característica importante da inferência bayesiana, onde a informação a priori é gradualmente substituída pela evidência empírica à medida que mais dados são coletados.