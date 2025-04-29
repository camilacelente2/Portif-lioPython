#revisao de aula
def contar_caracteres(texto):
    return len(texto)

def contar_palavras(texto):
    return len(texto.split())

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Contar o número de caracteres")
        print("2. Contar o número de palavras")
        print("3. Sair")

        escolha = input("\nDigite a sua escolha (1/2/3): ")

        if escolha == '3':
            print("A sair do sistema... Adeus!")
            break
        elif escolha in ['1', '2']:
            texto = input("\nDigite o texto: ")
            if escolha == '1':
                print(f"Número de caracteres: {contar_caracteres(texto)}")
            elif escolha == '2':
                print(f"Número de palavras: {contar_palavras(texto)}")
        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
