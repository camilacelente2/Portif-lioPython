var_salario = 0
var_faltas = 0
var_salario_novo = 0

var_salario = input ("Salario ")
var_faltas = input ("Faltas no mês ")

if  float (var_salario) < 2000 or int (var_faltas) == 0:
   var_salario_novo = float (var_salario) * 1.10
else:
  var_salario_novo = var_salario


print("Salario Final " , var_salario_novo)
