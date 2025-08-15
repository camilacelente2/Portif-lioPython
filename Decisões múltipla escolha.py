var_produto = ""
var_valor = 0
var_estado = ""

var_produto = input ("Qual produto ")
var_valor = input ("Qual valor ")
var_estado = input ("Estado de entrega (SP/ RJ/ MG)")

var_frete = 0
if var_estado == "SP":
  var_frete = float  (var_valor) * 0.10
elif var_estado == "RJ":
  var_frete = float  (var_valor) * 0.15
  print ("Custo do frete ", var_frete)
elif var_estado == "MG":
  var_frete = float  (var_valor) * 0.17

if (float(var_frete)== 0):
  print ("Nao entregamos")
else:
  print ("Custo do frete ", var_frete )
