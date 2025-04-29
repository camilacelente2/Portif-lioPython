
#percorrendostrings.py

nome = "pyton"
#for
for i in nome:
   print(i)
print("------")
   #while
i = 0
while i < len(nome):
    print(nome[i])
    i+=1
print("------")
#for/enumerate
for k, v in enumerate(nome):
   print(k, v)
   
   #percorrendo strings em alfabeto
   alfabeto = "A B C D E F G H I J L M N O P Q R S T U V W X Y Z"
for k, v in enumerate(alfabeto):
  print(k, v)

print(alfabeto.replace(" ", "-"))
