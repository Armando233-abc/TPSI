import matplotlib.pyplot as plt
import numpy as np

def fatturato(x, y1, y2):
    plt.plot(x, y1, label="matite")
    plt.plot(x, y2, label="quaderni")
    plt.title("Fatturato")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    x = np.linspace(0, 10, 40)
    y1 = [p*1 for p in x]
    y2 = [p*2 for p in x]
    fatturato(x, y1, y2)