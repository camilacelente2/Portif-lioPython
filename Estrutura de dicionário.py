
#Estruturadedicionario.py

#Introdução ao dicionários
dicionario = {"a":"amor", "b":"blue"}
dicionario2 = {1:20, 3:30, 4:40}
dicionario3 = {5.5:50, 30.1:30.25}
dicionario4 = {(10,20):["pyton", "linguagem", 10]}
print(dicionario)
print(type(dicionario))

#Acessando dicionarios
dicionario = {"a":"letraA", "b":"letraB", "c":"letraC"}
print(dicionario["a"])
print(dicionario.get('d', "Valor não encontrado!"))

#Funções com dicionários
agenda = {40408021:"José", 87541236:"Heloise", 78945612:"Carlos", 36925874:"Claudio"}
print(agenda)
del(agenda[40408021])
print(agenda)
print("-----------------")
print(agenda.keys())
print(agenda.values())
print(agenda.popitem())
print(agenda.popitem())
print(agenda)
