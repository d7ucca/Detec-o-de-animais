import cv2
import tkinter as tk
from processamento import processar_imagem, aplicar_hsv
from yolo_detector import detectar_animais
from interface import App

frame = cv2.imread("animal.jpg")

if frame is None:
    print("Erro: imagem não encontrada!")
    exit()

frame = cv2.resize(frame, (800, 600))

gray, blur, edges = processar_imagem(frame)
mask = aplicar_hsv(frame)

frame, contagem, recortes = detectar_animais(frame)

root = tk.Tk()
app = App(root)

app.atualizar(frame, contagem, recortes)

root.mainloop()