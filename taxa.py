# João Vitor Yokoyama Nobayashi: 2022 0494 0026
# Eduardo Costa Pantoja: 2022 0494 0009
# Andreya Paiva: 2022 0494 0005

import matplotlib.pyplot as plt

def exibirTerreno(lotes, k):
  ax = axes[k]
  labels = sizes = lotes[:]
  d = ax.pie(sizes, labels=labels, startangle=180, labeldistance=1.05, wedgeprops=dict(width=.3))

def inputLimited(mini, maxi, n):
  while True:
    values = input(f"Insira o(s) {n} valor(es) que esteja(m) no intervalo ]{mini}, {maxi}]: ").split()
    values = [float(elemento) for elemento in values]
    
    if len(values) != n:
      print(f"Insira {n} valores...\n")
      continue
    
    elif False in [0 < elemento <= 500 for elemento in values]:
      print("Insira os valores dentro do intervalo...\n")

    else:
      return values

while True:
  N, F = input("Insira o número de lotes(entre 1 e 200) seguido do fator de divisão(entre 0 e 5): ").split()
  N, F = int(N), float(F)

  if not (1 <= N <= 200 and 0 <= F <= 5):
    continue
  break

lotes = inputLimited(0, 500, N)
imposto = 0
fig, axes = plt.subplots(N, 1, figsize=(10, 10))

# realizando a divisão do terreno
for j in range(N-1):   
    pares = [ [], # lista com o par de vizinhança 
              []  # lista com o lote de maior valor de uma vizinhança com índice x
            ]

    for i in range(len(lotes)):
        # gerando um par de vizinhos
        par = [i, (i+1 if i+1<len(lotes) else 0)]
        # armazenando o par de vizinhos
        pares[0].append(par)
        # armazenando o maior valor entre eles
        pares[1].append(max([lotes[par[0]] , lotes[par[1]]]))
    
    # buscando o par de vizinhos com menor valor de divisão
    parMenorValor = pares[0][pares[1].index(min(pares[1]))]
    exibirTerreno(lotes, j)
    imposto += max([lotes[parMenorValor[0]], lotes[parMenorValor[1]]]) * F
    
    # transformando o par(parMenorValor) em um lote apenas
    lotes.insert(min(parMenorValor), 
                 lotes.pop(parMenorValor[0]) + lotes.pop(parMenorValor[1] - (1 if parMenorValor[0] < parMenorValor[1] else 0)))

exibirTerreno(lotes, N-1)

# ajustando espaçamento entre gráficos
fig.subplots_adjust(wspace=.8)
plt.subplots_adjust(top=0.85, bottom=0.15)

# renderizando
plt.show()

print(f"\n\nImposto Total: {imposto}")
