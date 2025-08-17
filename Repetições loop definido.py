var_capital = 0
var_capital_apli = 0
var_taxa = 0
var_meses = 0
var_contador = 1

var_capital = input("Capital de entrada ")
var_capital_apli = float(var_capital)
var_taxa = input("Taxa de rentabilidade ao mês ")
var_meses = input("Meses de aplicacao ")

for var_contador in range (1, int(var_meses)+1):
 var_capital_apli = float(var_capital_apli) + (float(var_capital_apli) *  float(var_taxa))
 print(var_contador)
 

print("Capital de entrada ", var_capital)
print("Capital final ", var_capital_apli)
