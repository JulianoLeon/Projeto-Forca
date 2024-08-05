import random

def origem_arquivo():
  
    arquivo = open(r'C:\Users\Administrador\Projetos_Python\123\palavras.txt', 'r')
    return arquivo

def palavras_lista():
    
    with origem_arquivo() as file:
    
        palavras = file.readlines()

    palavras = [palavra.strip().lower() for palavra in palavras]
    
    return palavras



def mostrar_status(palavra_adivinhada, letras_tentadas):

    print(' '.join(palavra_adivinhada))
    print(f"Letras já tentadas: {', '.join(letras_tentadas)}")


def main():
    palavra = palavras_lista()
    palavra = palavra[random.randint(0, len(palavra) - 1)]

    tamanho_palavra = len(palavra)
    palavra_adivinhada = ['_'] * tamanho_palavra 
    letras_tentadas = set()
    erros = 0
    max_erros = 6 

    print("Bem-vindo ao Jogo da Forca! - DICA - É um animal")
    
    while erros < max_erros:
        mostrar_status(palavra_adivinhada, letras_tentadas)
        tentativa = input("Adivinhe uma letra ou tente adivinhar a palavra inteira: ").lower()

        if tentativa == palavra:
            print(f"Parabéns! Você acertou a palavra '{palavra}'!")
            return

        if len(tentativa) == 1 and tentativa.isalpha(): 
            if tentativa in letras_tentadas:
                print("Você já tentou essa letra.")
                continue

            letras_tentadas.add(tentativa)

            if tentativa in palavra:
              
                for indice, letra in enumerate(palavra):
                    if letra == tentativa:
                        palavra_adivinhada[indice] = tentativa
                if '_' not in palavra_adivinhada:
                    print(f"Parabéns! Você ganhou! A palavra era '{palavra}'.")
                    return
            else:
                erros += 1
                print(f"Letra errada! Tentativas restantes: {max_erros - erros}")
        else:
            print("Entrada inválida. Por favor, insira uma única letra ou tente adivinhar a palavra.")

    print(f"Game over! A palavra era '{palavra}'.")


main()
