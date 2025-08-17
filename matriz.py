import numpy as np

# Cria um array que aceita texto e número
var_notas = np.zeros((2,6), dtype=object)  # +1 coluna para média

for x in range(2):
    var_notas[x,0] = input("Digite o nome: ")
    soma = 0
    for y in range(4):
        nota = float(input(f"Digite a nota {y+1} de {var_notas[x,0]}: "))
        var_notas[x,y+1] = nota
        soma += nota
    media = soma / 4
    var_notas[x,5] = media   # guarda a média na última coluna

# Mostra os resultados
for x in range(2):
    print(f"\nAluno: {var_notas[x,0]}")
    print("Notas:", var_notas[x,1:5])
    print("Média:", var_notas[x,5])
