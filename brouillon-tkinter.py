import tkinter as tk

racine = tk.Tk()
label1 = tk.Label(racine, text="12", font = ("helvetica", "26"))
label2 = tk.Label(racine, text="+", font = ("helvetica", "26"))
label3 = tk.Label(racine, text="25", font = ("helvetica", "26"))
label4 = tk.Label(racine, text="=", font = ("helvetica", "26"))
label5 = tk.Label(racine, text="37", font = ("helvetica", "26"))
label6 = tk.Label(racine, text="choisir une valeur pour l'opérande gauche", font = ("helvetica", "26"))
label7 = tk.Label(racine, text="calculer", font = ("helvetica", "26"))
label8 = tk.Label(racine, text="choisir une valeur pour l'opérande droite", font = ("helvetica", "26"))

label1.grid(column=1, row=0)
label2.grid(column=2, row=0)
label3.grid(column=3, row=0)
label4.grid(column=4, row=0)
label5.grid(column=5, row=0)
label6.grid(column=0, row=1)
label7.grid(column=1, row=1, columnspan=5)
label8.grid(column=0, row=2)

racine.mainloop()