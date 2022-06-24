import Forca
import Adivinhacao

def escolha_jogo():

    print ("*********************************")
    print ("********Escolha seu jogo!********")
    print ("*********************************")

    print ("(1) Forca (2) Adivinhção")

    jogo =int(input("Qual jogo?"))

    if (jogo == 1):
        print ("jogando forca")
        Forca.jogar()

    elif (jogo ==2):
        print ("jogando adivinhação")
        Adivinhacao.jogar()



if (__name__=="__main__"):
   escolha_jogo()