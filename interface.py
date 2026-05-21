# -*- coding: utf-8 -*-

import tkinter as tk
from PIL import Image, ImageTk
import cv2


class App:

    def __init__(self, root):

        self.root = root
        self.root.title("Sistema Inteligente de IA - Visão Computacional")
        self.root.geometry("1800x950")
        self.root.configure(bg="#0f0f0f")

        # =========================
        # SCROLL PRINCIPAL
        # =========================

        self.canvas = tk.Canvas(root, bg="#0f0f0f", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)

        self.frame = tk.Frame(self.canvas, bg="#0f0f0f")

        self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas.create_window((0,0), window=self.frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

        # =========================
        # TÍTULO
        # =========================

        tk.Label(
            self.frame,
            text="🐾 Sistema IA - Monitoramento Inteligente",
            font=("Arial", 22, "bold"),
            fg="#00ffcc",
            bg="#0f0f0f"
        ).pack(pady=10)

        # =========================
        # ÁREA PRINCIPAL
        # =========================

        self.main = tk.Frame(self.frame, bg="#0f0f0f")
        self.main.pack()

        self.left = tk.Frame(self.main, bg="#0f0f0f")
        self.left.grid(row=0, column=0)

        self.right = tk.Frame(self.main, bg="#1a1a1a", width=450)
        self.right.grid(row=0, column=1, sticky="ns")

        # =========================
        # IMAGENS
        # =========================

        self.labels = {}

        nomes = [
            "Original",
            "YOLO",
            "Gray",
            "Blur",
            "Edges",
            "Sharpen",
            "HSV Mask",
            "Threshold"
        ]

        r = 0
        c = 0

        for n in nomes:

            box = tk.Frame(self.left, bg="#1e1e1e", bd=2)
            box.grid(row=r, column=c, padx=8, pady=8)

            tk.Label(box, text=n, fg="#00ffcc", bg="#1e1e1e").pack()

            lbl = tk.Label(box, bg="#1e1e1e")
            lbl.pack()

            self.labels[n] = lbl

            c += 1
            if c > 1:
                c = 0
                r += 1

        # =========================
        # DASHBOARD
        # =========================

        tk.Label(
            self.right,
            text="📊 Dashboard IA",
            fg="#00ffcc",
            bg="#1a1a1a",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        self.info = tk.Text(
            self.right,
            width=45,
            height=40,
            bg="#121212",
            fg="white",
            font=("Consolas", 11)
        )

        self.info.pack()

        # botão animais
        tk.Label(
            self.right,
            text="🔍 Animais Detectados",
            fg="#00ffcc",
            bg="#1a1a1a"
        ).pack(pady=5)

        self.animals_frame = tk.Frame(self.right, bg="#1a1a1a")
        self.animals_frame.pack()


    # =========================
    # CONVERTER IMAGEM
    # =========================

    def converter(self, img):

        if len(img.shape) == 2:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        img = Image.fromarray(img)
        img = img.resize((350, 200))

        return ImageTk.PhotoImage(img)


    # =========================
    # ZOOM POPUP
    # =========================

    def zoom(self, img, nome):

        pop = tk.Toplevel(self.root)
        pop.title(nome)
        pop.geometry("500x500")
        pop.configure(bg="#0f0f0f")

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = img.resize((450, 450))

        imgtk = ImageTk.PhotoImage(img)

        tk.Label(pop, image=imgtk, bg="#0f0f0f").pack()
        pop.image = imgtk


    # =========================
    # UPDATE
    # =========================

    def atualizar(
        self,
        original,
        yolo,
        gray,
        blur,
        edges,
        sharpen,
        mask,
        thresh,
        contagem,
        iluminacao,
        objetos,
        recortes
    ):

        imgs = {
            "Original": original,
            "YOLO": yolo,
            "Gray": gray,
            "Blur": blur,
            "Edges": edges,
            "Sharpen": sharpen,
            "HSV Mask": mask,
            "Threshold": thresh
        }

        for k, v in imgs.items():
            img = self.converter(v)
            self.labels[k].imgtk = img
            self.labels[k].configure(image=img)

        # limpar botões
        for w in self.animals_frame.winfo_children():
            w.destroy()

        # botoes animais
        for nome, img in recortes:

            tk.Button(
                self.animals_frame,
                text=f"{nome}",
                bg="#00ffcc",
                command=lambda i=img, n=nome: self.zoom(i, n)
            ).pack(pady=2)

        # dashboard
        self.info.delete(1.0, tk.END)

        self.info.insert(tk.END, "=== IA RESULTADOS ===\n\n")
        self.info.insert(tk.END, f"{iluminacao}\n\n")
        self.info.insert(tk.END, f"{objetos}\n\n")

        total = sum(contagem.values())

        for k, v in contagem.items():
            self.info.insert(tk.END, f"{k}: {v}\n")

        self.info.insert(tk.END, f"\nTotal: {total}\n")

        self.info.insert(tk.END, "\n✔ Pipeline completo de visão computacional + YOLO")