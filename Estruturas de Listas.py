
#estruturasdelistas.py

#Introdução a listas
#0 1 2 3 4 5... n
nome = "pyton"
lista = [2,3,4,5]
lista2 = [1.5, 2.3, 6.5]
lista3 = [1, 1.5, "numero"]
lista4 = []
print(lista2[1])

#Percorrendo listas
lista = [100, 200, 300, 400, 500, 600, 700, 800]
for i in range(len(lista)):
  print(lista[i])

print(lista)

#Fatiando Listas

#         0 1 2
lista = [2, 3, 4]
#       -3 -2 -1

nova_lista = lista[0:2:2]
print(nova_lista)

lista2 = ['p', 'y', 't', 'h' 'o', 'n']
nova_lista2 = lista2[::-1]
print(nova_lista2)

#Incluir, alterar e Excluir
animais = ['gato', 'cachorro', 'elefante']
print(animais)
animais.append('galinha')
print(animais)
animais.insert(0, 'papagaio')
print(animais)
animais.pop(0)
print(animais)
animais.remove('gato')
print(animais)

#Ordenação de listas
lista = ['a', 'x', 's', 'w', 'd', 'a', 'n', 'a']
#lista.reserve()
lista.sort()

print(lista)

for i in range(len(lista)):
  print(lista[i])
  l = lista.count('a')
  print(l)
