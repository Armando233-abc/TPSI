import matplotlib.pyplot as plt
import numpy as np

guadagno_matite = []
guadagno_quaderni = []

scorte_matite = []
scorte_quaderni = []

def fatturato(x1, x2):
    guadagno_matite.append(x1)
    guadagno_quaderni.append(x2)

def scorte_magazino(matite, quaderni):
    scorte_matite.append(matite)
    scorte_quaderni.append(quaderni)



def stampa():
    guadagni()
    scorte()

def guadagni():
    x = np.arange(0, len(guadagno_matite))
    plt.title("Fatturato")
    plt.plot(x, guadagno_matite, label="matite")
    plt.plot(x, guadagno_quaderni, label="quaderni")
    plt.grid()
    plt.legend()
    plt.show()

def scorte():
    x = np.arange(0, len(guadagno_matite))
    width = 0.35  # the width of the bars
    plt.title("scorte")
    plt.bar(x - width/2, scorte_matite, width=width, label="matite")
    plt.bar(x + width/2, scorte_quaderni, width=width, label="quaderni")
    plt.grid()
    plt.legend()
    plt.show()

