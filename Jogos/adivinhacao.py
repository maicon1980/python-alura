import random

def jogar():

    print("======================================")
    print("Bem vindo ao jogo de Adivinhação!")
    print("======================================")

    n_secreto = random.randrange(1,101)
    n_tentativas = 3
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil")
    print("(2) Médio")
    print("(3) Difícil")

    nivel = int(input("Escolha o nível: "))

    if (nivel == 1):
        n_tentativas = 20
    elif(nivel == 2):
        n_tentativas = 10
    else:
        n_tentativas = 5

    for rodada in range(1, n_tentativas + 1):
        print("Tentativa {}/{}".format(rodada,n_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Só aceitamos número entre 1 e 100")
            continue


        acertou = n_secreto == chute
        chute_maior = n_secreto < chute
        chute_menor = n_secreto > chute

        if(acertou):
            print("Parabéns, você acertou!")
            print("Você alcançou {} pontos!".format(pontos))
            break
        else:
            if (chute_maior):
                print("Você errou, tente um número menor que ", chute)
            elif(chute_menor):
                print("Você errou, tente um número maior que ", chute)
            pontos_perdidos = abs(n_secreto - chute)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1

        print("Você digitou: ", chute)

if (__name__ == "__main__"):
    jogar()
