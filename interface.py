# -*- coding: utf-8 -*-
import tkinter as tk
from PIL import Image, ImageTk
import cv2

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Detecção de Animais 🐾")
        self.root.geometry("900x700")
        self.root.configure(bg="#1e1e1e")

        self.contagem = {}
        self.recortes = []

        self.titulo = tk.Label(
            root,
            text="🐾 Detecção Inteligente de Animais",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#1e1e1e"
        )
        self.titulo.pack(pady=10)

        self.label = tk.Label(root, bg="#1e1e1e")
        self.label.pack(pady=10)

        self.botao = tk.Button(
            root,
            text="Ver animais detectados",
            command=self.abrir_popup,
            bg="#ff00aa",
            fg="white",
            font=("Arial", 12, "bold")
        )
        self.botao.pack(pady=10)

    def atualizar(self, frame, contagem, recortes):
        self.contagem = contagem
        self.recortes = recortes

        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = img.resize((800, 500))

        img = ImageTk.PhotoImage(image=img)

        self.label.imgtk = img
        self.label.configure(image=img)

    def abrir_popup(self):
        descricao = {
            "dog": "Cachorro",
            "cat": "Gato",
            "bird": "Pássaro",
            "horse": "Cavalo",
            "cow": "Vaca",
            "sheep": "Ovelha"
        }

        if not self.recortes:
            popup = tk.Toplevel(self.root)
            popup.title("Resultado")
            popup.geometry("250x150")
            popup.configure(bg="#1e1e1e")

            tk.Label(
                popup,
                text="Nenhum animal detectado",
                fg="#ff00aa",
                bg="#1e1e1e"
            ).pack(pady=20)

        else:
            for nome, corte in self.recortes:
                popup = tk.Toplevel(self.root)
                popup.title("Animal detectado")
                popup.geometry("300x320")
                popup.configure(bg="#1e1e1e")

                nome_pt = descricao.get(nome, nome)

                img = cv2.cvtColor(corte, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(img)
                img = img.resize((200, 200))

                img_tk = ImageTk.PhotoImage(img)

                label_img = tk.Label(popup, image=img_tk, bg="#1e1e1e")
                label_img.image = img_tk
                label_img.pack(pady=10)

                tk.Label(
                    popup,
                    text=nome_pt,
                    font=("Arial", 12, "bold"),
                    fg="#ff00aa",
                    bg="#1e1e1e"
                ).pack()