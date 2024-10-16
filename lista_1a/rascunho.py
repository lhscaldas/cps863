# P_2azuis_UA = 250*249/1000/999
# P_2azuis_UB = 100*99/1000/999
# P_UA = 0.15
# P_UB = 1-P_UA

# P_2azuis = P_2azuis_UA*P_UA + P_2azuis_UB*P_UB

# P_UA_2azuis = P_2azuis_UA*P_UA/(P_2azuis_UA*P_UA + P_2azuis_UB*P_UB)
# print(P_UA_2azuis)
# P_UB_2azuis = P_2azuis_UB*P_UB/(P_2azuis_UA*P_UA + P_2azuis_UB*P_UB)
# print(P_UB_2azuis)


# Priori
P_U6 = 0.7
P_U5 = 1-P_U6

# Likelihood
dados = [2,2,4,3,2]
P_dados_U6 = (1/6)**5
P_dados_U5 = (1/5)**5
print(P_dados_U6)
print(P_dados_U5)

# Posteriori
P_dados = P_dados_U6*P_U6 + P_dados_U5*P_U5
P_U6_dados = P_dados_U6*P_U6/P_dados
P_U5_dados = P_dados_U5*P_U5/P_dados
print(P_U6_dados)
print(P_U5_dados)

P_5_dados = 1/5*P_U5_dados + 1/6*P_U6_dados
print(P_5_dados)

P_6_dados = 1/6*P_U6_dados + 0*P_U5_dados
print(P_6_dados)