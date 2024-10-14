# CPS863 – Aprendizado de Máquina

Este repositório é utilizado para armazenar os trabalhos da disciplina de pós-graduação CPS863 – Aprendizado de Máquina.

## Informações da Disciplina

- **Programa:** Programa de Engenharia de Sistemas e Computação (PESC)
- **Instituto:** Instituto Alberto Luiz Coimbra de Pós-Graduação e Pesquisa de Engenharia (COPPE/UFRJ)
- **Professor:** Prof. Dr. Edmundo de Souza e Silva (PESC/COPPE/UFRJ)

# Questão 1

Este exercício foi feito em classe no dia 10/Out/2024. A lista contém as questões resolvidas e ainda
alguns itens a mais. Faça a lista e complete as questões que faltaram.

Este exercício é motivado pelo trabalho em [https://ieeexplore.ieee.org/document/9006548](https://ieeexplore.ieee.org/document/9006548),
Seção H (Leveraging spatio-temporal correlation across homes). O problema foi simplificado neste
exercício.

Imagine que dispomos de um classificador implementado em roteadores residenciais de um provedor
de Internet (ISP). A cada janela de tempo (por exemplo a cada 5 minutos) o classificador do roteador
$i$ fornece como saída uma dentre 2 possibilidades: (a) existe um ataque DDoS acontecendo a partir da
residência do roteador $i$, nesta janela de tempo; (b) não há ataque acontecendo a partir da residência
do roteador $i$ nesta janela.

A cada 5 minutos o ISP amostra o resultado de $M$ roteadores escolhidos de forma aleatória dentre
todos os roteadores da sua base que, para todos os efeitos deste problema, pode ser considerada como
muito grande (infinita). O objetivo do ISP é determinar, a partir das $M$ amostras coletadas, se
um ataque aconteceu ou não durante a janela de tempo amostrada. Em outras palavras, o ISP quer
determinar a possibilidade de uma das seguintes hipóteses serem verdadeiras: $h_a$ (há um ataque DDoS
acontecendo na rede do ISP na janela amostrada) ou $h_b$ que é a hipótese complementar.

O ISP conhece o classificador usado em cada roteador residencial, e sabe que o resultado não é
100% confiável. Portanto, ele usará correlação espacial conforme sugerido no artigo acima e explicado
em classe.

No que se segue usaremos algumas definições comuns que podem ser encontradas em
[https://en.wikipedia.org/wiki/Confusion_matrix](https://en.wikipedia.org/wiki/Confusion_matrix) (ver também a figura em [https://en.wikipedia.org/wiki/Confusion_matrix](https://en.wikipedia.org/wiki/Confusion_matrix)).

## Notação:

- $M$: número de roteadores amostrados (em uma janela de tempo);
- Inf: variável aleatória (va) indicando se a residência é um “bot”, isto é, está ou não infectada.
  $P[\text{Inf}]$ ($P[\overline{\text{Inf}}]$) é a probabilidade de uma residência estar infectada (não estar infectada);
- TPR: (true positive rate ou hit rate) taxa de acerto do classificador, ou probabilidade do classificador corretamente sinalizar um ataque, dado que um ataque está acontecendo no ISP (Nota: obviamente somente residências infectadas podem gerar um ataque quando ele ocorre);
- FPR: (false positive rate) ou probabilidade do classificador do roteador residencial erradamente sinalizar um ataque a partir da residência;
- $L$: variável aleatória indicadora $L = 1$ se o roteador alarma, $L = 0$, caso contrário;
- $P[h_a]$: probabilidade de ocorrer um ataque DDoS no ISP em uma janela de tempo. (Se você tem algum conhecimento prévio sobre ataques, talvez possa estimar o $P[h_a]$).

Suponha que, em uma determinada janela de tempo, das $M$ amostras coletadas, $V$ roteadores
sinalizaram que um ataque estava ocorrendo na janela (e então $M - V$ roteadores sinalizaram que
tudo estava normal nas suas respectivas residências). Suponha ainda que um ataque ocorre em um
intervalo independentemente das infecções nas residências.

Para os seus cálculos, suponha que: TPR = 0.8, FPR = 0.1, $P[\text{Inf}] = 0.2$. Como você
não tem conhecimento prévio sobre $P[h_a]$, suponha inicialmente que $P[h_a] = P[h_b] = 0.5$, $V = 20$, $M = 200$.

\vspace{1\baselineskip}
Responda as seguintes perguntas, mas só substitua os valores no final:




