
#Funcoes.py

#Introdução a Funções
def funcao():
  print("Eu sou uma função!")
funcao()

#Parametro de funções
def soma(x, y):
  total = x + y
  print(total)

soma(2,4)

#Retorno
def show():
  return 15

print(show())

#Retorno(1)
def mult(a, b):
  return a * b

print(mult(2,5))

#Exercício de Operações Matemática
def operacoes(a, b):
  soma = a + b
  sub = a - b
  mult = a * b
  div = a /b
  print("soma:", soma)
  print("subitração:", sub)
  print("multiplicação:", mult)
  print("divisão:", div)

operacoes(4, 2)
