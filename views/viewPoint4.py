from tkinter import *
from tkinter import messagebox

from model.point4 import genererPoint4

def displayMenuFour(WindowMain,framePoint4):

    global valueLabel
    
    valueAdresse1 = StringVar()
    valueMasque1 = StringVar()
    valueAdresse2 = StringVar()
    valueMasque2 = StringVar()
    valueLabel = StringVar()


    #changement titre
    WindowMain.title("Projet LABO_TCPIP - Point 4")
    
    #création des composants
    Label(framePoint4, text="Veuillez encoder la première adresse IP", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=1)
    Entry(framePoint4,textvariable=valueAdresse1).grid(column=2, row=2, pady=15)
    
    Label(framePoint4, text="Veuillez encoder le masque de la première adrese IP ", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=3)
    Entry(framePoint4,textvariable=valueMasque1).grid(column=2, row=4, pady=15)
    
    Label(framePoint4, text="Veuillez encoder la deuxième adresse IP ", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=5)
    Entry(framePoint4,textvariable=valueAdresse2).grid(column=2, row=6, pady=15)
    
    Label(framePoint4, text="Veuillez encoder le masque de la  deuxième adresse IP", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=7)
    Entry(framePoint4,textvariable=valueMasque2).grid(column=2, row=8, pady=15)

    Label(framePoint4, textvariable=valueLabel, font=("Impact",10),foreground="white", background="#009790").grid(column=2, row=9)
    
    Button(framePoint4, text="Vérifier les correspondances",command=lambda:genererInformationsFour(valueAdresse1.get(),valueMasque1.get(),valueAdresse2.get(),valueMasque2.get())).grid(column=2, row=11, padx=200, pady=30, ipadx=50)
    
    
    #ajout du conteneur
    framePoint4.grid()

    def genererInformationsFour(IpAdress, MaskAdress, IpAdress2, MaskAdress2):
    
        result = genererPoint4(IpAdress, MaskAdress, IpAdress2, MaskAdress2)
        
        #traitement
        if((result == "IpInvalid1")):
            messagebox.showerror("ERREUR", "L'adrese IP de la première machine encodée n'est pas valide\nmerci de d'en choisir une autre !")
        elif((result == "MaskInvalid1")):
            messagebox.showerror("ERREUR", "L'adrese de masque de la première machine encodée n'est pas valide\nmerci de d'en choisir une autre !")
        elif((result == "IpInvalid2")):
            messagebox.showerror("ERREUR", "L'adrese IP de la deuxième machine encodée n'est pas valide\nmerci de d'en choisir une autre !")
        elif((result == "MaskInvalid2")):
            messagebox.showerror("ERREUR", "L'adrese de masque de la deuxième machine encodée n'est pas valide\nmerci de d'en choisir une autre !")
        else:
            valueLabel.set("Resultats\n---------------------------------------------\n"+result) 