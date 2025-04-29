sair = True


while sair == True :


    nome_produto = str(input("Digite o  nome do  produto: "))
    print()  
    preco = float(input("digite o  peço: "))

    print("Erro! digite um numero")
    

    if (preco <= 50) :
        print("produtro de baixo  custo.")
        print(nome_produto)
        print(preco)
        sair = False

    elif(preco >50  and preco <=100 ) :

        print("produtro de medio custo.")
        print(nome_produto)
        print(preco)
        sair = False

    else :
        print("produtro de alto custo.")
        print(nome_produto)
        print(preco)
        sair = False
 
