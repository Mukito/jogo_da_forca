import random

# Função para carregar palavras do arquivo txt
def carrega_palavras(arquivo):
    with open(arquivo, 'r') as f:
        palavras = f.read().splitlines()    # Lê todas as linhas e remove quebras de linha
    return palavras

# Função para escolher uma palavra aleatória
def escolher_palavra(palavras):
    return random.choice(palavras)

letras_corretas = []
tentativa = 6
letras_erradas = []

# Função de inicio do jogo
def inicio():
    print("=================================================================")
    print("==========       Bem Vindo ao jogo da Forca            ==========")
    print("=================================================================")
    print(" O jogo começou! A palavra secreta ja foi escolhida.  \n")

# Função para exibir o status atual
def exibir_status():
    print("Palavra: " + " ".join(letras_corretas))
    print(f"Tentativas restantes: {tentativa}")
    print(f"Letras erradas: {', '.join(letras_erradas)}\n")

# Função principal do jogo
def jogo(palavraSecreta):
    global tentativa
    global letras_erradas
    global letras_corretas

    letras_corretas = ['_'] * len(palavraSecreta)   # Inicializa a lista com underscores

    while tentativa > 0:
        exibir_status()

        chute = input("Qual Letra? ").strip().lower()

        if len(chute) != 1 or not chute.isalpha():              # isalpha retorna True quando todos caracters da string forem letras de a-z 
            print("Por favor, digite uma única letra. ")
            continue

        if chute in letras_erradas or chute in letras_corretas:
            print(f"A letra '{chute}' já foi tentada. Tente outra. \n")
            continue

        if chute in palavraSecreta:
            print(f"Boa a letra '{chute}' esta na palavra. ")
            for i in range(len(palavraSecreta)):
                if palavraSecreta[i] == chute:
                    letras_corretas[i] = chute
        else:
            print(f"Ops!! A letra '{chute}' esta na palavra.")
            tentativa -= 1
            letras_erradas.append(chute)

        if "_" not in letras_corretas:
            print("Parabens! Você adivinhou a palavra:", palavraSecreta)
            break
    if tentativa == 0:
        print(f"Você perdeu! a palavra era: {palavraSecreta}")
        
if __name__ == "__main__":
    # Carregar palavras do arquivo txt
    palavras = carrega_palavras("palavras.txt")

    #Escolher uma palavra aleatória
    palavraSecreta = escolher_palavra(palavras)

    inicio()     # Iniciar o Jogo
    jogo(palavraSecreta)       # Jogar com a palavra escolhida



