var_n1 = 0
var_n2 = 0
var_media = 0

var_msg = "Aprovado"
var_np = "Nova Prova"


var_n1 = input("Digite a 1a nota ")
var_n2 = input("Digite a 2a nota ")

var_media = ( int (var_n1) + int (var_n2 ) ) / 2

print ("Media calculada", var_media)
if (var_media >=7):
  print ("---------")
  print (var_msg)
else:
  print ("==========")
  print (var_np)
