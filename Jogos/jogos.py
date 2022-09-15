import adivinhacao
import forca

def escolhe_jogo():
    print("======================")
    print(" Escolha o seu JOGO!")
    print("======================")

    print("(1) Adivinhação")
    print("(2) Forca")

    jogo = int(input("Qual o jogo: "))

    if(jogo == 1):
        print("Jogando o jogo da Adivinhação")
        adivinhacao.jogar()
    elif(jogo == 2):
        print("Jogando o jogo da Forca")
        forca.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()