import threading
import time
import sys
import random
guadagno_quaderni=0
guadagno_matite=0

magazzino_matite = 200
magazzino_quaderni = 200

prezzo_quaderni = 2
prezzo_matite = 1



matite = threading.Semaphore(magazzino_matite)
quaderni = threading.Semaphore(magazzino_quaderni)


def signal_quaderni():
    quaderni.acquire


def wait_quaderni():
    quaderni.acquire


def signal_matite():
    matite.acquire


def wait_matite():
    matite.acquire


def scelta_articolo():
    scelta = int(input("Che articolo ti serve? \n1) Quaderno \n2) Matita \nInserisci: "))
    if (scelta == 1):
        compro_quaderni()
    elif (scelta == 2):
        compro_matite()
    else:
        print("Non abbiamo quest'articolo. CIAO")


def compro_matite():
    global magazzino_matite
    global guadagno_matite
    guadagno_parziale_matite = 0
    print("Sei entrato nel magazzino delle matite")
    x = int(input("Quante matite vuoi ? "))
    wait_matite()
    magazzino_matite = magazzino_matite - x
    if (magazzino_matite <= 0):
        print("Non ci sono matite aspetta che il magazzino viene aggiornato ")
    signal_matite()
    guadagno_parziale_matite = x * prezzo_matite
    guadagno_matite = guadagno_matite + guadagno_parziale_matite
    print("Nel magazzino ci sono {0} matite ".format(magazzino_matite))
    if (magazzino_matite < 10):
        print("Ti consiglio di aggiornare il magazzino con più matite")
        consiglio = input("Accettti il consiglio? Y/N")
        if (consiglio == 'Y'):
            matite_aggiunte = int(input("Quante matite vuoi aggiungere?"))
            magazzino_matite += matite_aggiunte
            compro_matite()
        else:
            print("I tuoi clienti iniziano a temere la disponibilità delle matite e stanno cambiando fornitore")
            print("Non ci sono matite")
            sys.exit()

def compro_quaderni():
    global magazzino_quaderni
    global guadagno_quaderni
    guadagno_parziale_quaderni = 0
    print("Sei entrato nel magazzino dei quaderni")
    x = int(input("Quanti quaderni vuoi ? "))
    wait_quaderni()
    magazzino_quaderni = magazzino_quaderni - x
    if(magazzino_quaderni <= 0):
        print("Non ci sono quaderni aspetta che il magazzino viene aggiornato ")
    signal_quaderni()
    guadagno_parziale_quaderni = x * prezzo_quaderni
    guadagno_quaderni = guadagno_quaderni + guadagno_parziale_quaderni
    print("Nel magazzino ci sono {0} quaderni ".format(magazzino_quaderni))
    if (magazzino_quaderni < 10):
        print("Ti consiglio di aggiornare il magazzino con più quaderni")
        consiglio = input("Accettti il consiglio? Y/N ")
        if (consiglio == 'Y'):
            quaderni_aggiunte = int(input("Quanti quaderni vuoi aggiungere?"))
            magazzino_quaderni += quaderni_aggiunte
            compro_quaderni()
        else:
            print("I tuoi clienti iniziano a temere la disponibilità dei quaderni e stanno cambiando fornitore")
            if(magazzino_quaderni<=0):
                print("Non ci sono quaderni")
                sys.exit()


for i in range(10):
    t = threading.Thread(target=scelta_articolo())
    t.start()
    t.join()

print(f"Il guadagno di oggi è stato di {guadagno_quaderni+guadagno_matite}")

print(f"Con le matite hai guadagnato {guadagno_matite}")

print(f"Con i quaderni hai guadagnato {guadagno_quaderni}")