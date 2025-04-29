
#Estruturadetuplas.py

#Introdução a tuplas
t = tuple("abc")
x = ('python', "curso")
x1 = (2, 3, 4)
x2 = (2.1, 2.3, 2.5)
x3 = ("python", 1, 2.5, True)
print(x3)
print(type(x3))

#Operações com tuplas
elementos_tupla = ('São Paulo', 'Belo Horizonte', 'Teresina')
print('Manaus' in elementos_tupla)
print('São Paulo' in elementos_tupla)
#                0        1         2        3        4       5
nomes_tupla = ('José', 'Carlos', 'Maria', 'Pedro', 'Joana', 'Maria')
print(nomes_tupla.count('Maria'))
print(nomes_tupla.index('Carlos'))
