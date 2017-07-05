from codes import code_alteracao

tamanhos = []

for i in code_alteracao:
   tamanhos.append(len(code_alteracao[i]))

print max(tamanhos)
