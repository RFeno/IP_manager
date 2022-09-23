from tkinter import *
from tkinter import ttk


root = Tk()
frm = ttk.Frame(root, padding=30)
frm.grid()

ttk.Label(frm, text="1. Trouver les informations de l'adresse IP\n     A. Classe \n     B. Nombre de réseaux \n     C. Nombre de machines").grid(column=0, row=1)
ttk.Button(frm, text="Valider (point 1)", ).grid(column=2, row=1)


ttk.Label(frm, text="2. Trouvez les informations de l'adresse IP\n     A. Adresse de réseau \n     B. Adresse de broadcast \n     C. Adresse de sous-réseau").grid(column=0, row=3)
ttk.Button(frm, text="Valider (point 2)", ).grid(column=2, row=3)


ttk.Label(frm, text="3. L'IP apartient-il au réseau ?").grid(column=0, row=5)
ttk.Button(frm, text="Valider (point 3)", ).grid(column=2, row=5)


ttk.Label(frm, text="4. Sont-ils dans le même réseau ?").grid(column=0, row=7)
ttk.Button(frm, text="Valider (point 4)", ).grid(column=2, row=7)

ttk.Label(frm, text="5. Déterminer les possibilités\n     A. Le nombre d'hôtes \n     B. Découpe sur nombre de sous-réseaux \n     C. Découpe par nombre d'adresse IP").grid(column=0, row=9)
ttk.Button(frm, text="Valider (point 5)", ).grid(column=2, row=9)


ttk.Button(frm, text="Fermer", command=root.destroy).grid(column=1, row=11)

#afficher la fenêtre 
root.mainloop()