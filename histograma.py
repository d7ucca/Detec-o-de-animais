import cv2
import matplotlib.pyplot as plt

def mostrar_histograma(frame):

    cores = ('b', 'g', 'r')

    plt.figure("Histograma RGB")

    for i, cor in enumerate(cores):

        hist = cv2.calcHist([frame], [i], None, [256], [0,256])

        plt.plot(hist, color=cor)

    plt.xlim([0,256])

    plt.xlabel("Intensidade")
    plt.ylabel("Quantidade de Pixels")

    plt.title("Histograma da Imagem")

    plt.show()