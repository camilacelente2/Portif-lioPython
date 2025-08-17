var_notas = []
var_media = 0

for x in range(4):
  var_notas.append( input("Nota ") )
  var_media = float(var_media) + float(var_notas[x])

for x in range(4):
  print(var_notas[x])

var_media = float(var_media) / 4



print(var_media)

if var_media >= 7:
  print("Aprovado ")
else:
  print("Nova prova ")
