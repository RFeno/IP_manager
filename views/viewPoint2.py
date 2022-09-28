from tkinter import *
from tkinter import messagebox

from model.point2 import genererPoint2


def displayMenuTwo(WindowMain,framePoint2):
    
    global valueLabel
    
    valueAdresse = StringVar()
    valueMasque = StringVar()
    valueLabel = StringVar()
    
    #changement titre
    WindowMain.title("Projet LABO_TCPIP - Point 2")
    #création des composants
    Label(framePoint2, text="Point 2 ", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=0,pady=5)
    
    Label(framePoint2, text="Veuillez encoder l'adresse IP ", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=1)
    Entry(framePoint2,textvariable=valueAdresse).grid(column=2, row=2, pady=25)

    
    Label(framePoint2, text="Veuillez encoder le masque de l'adresse IP", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=3)
    Entry(framePoint2,textvariable=valueMasque).grid(column=2, row=4, pady=25)

    Label(framePoint2, textvariable=valueLabel, font=("Impact",10),foreground="white", background="#009790").grid(column=2, row=5)
    
    Button(framePoint2, text="Générer les informations ",command=lambda:genererInformationsTwo(valueAdresse.get(),valueMasque.get())).grid(column=2, row=9, padx=200, pady=30, ipadx=50)
    
   
    
    #ajout du conteneur
    framePoint2.grid()


def genererInformationsTwo(IpAdress, MaskAdress):
    
    result = genererPoint2(IpAdress, MaskAdress)
    
    #traitement
    if((result == "IpInvalid")):
        messagebox.showerror("ERREUR", "L'adrese IP encodée n'est pas valide\nmerci de d'en choisir une autre !")
    elif((result == "MaskInvalid")):
        messagebox.showerror("ERREUR", "L'adrese de masque encodée n'est pas valide\nmerci de d'en choisir une autre !")
    elif((result == "MaskInvalidGlobal")):
        messagebox.showerror("ERREUR", "l'adresse de masque ne peut pas être plus englobant que l'adresse de classe\nmerci de d'en choisir une autre !")
    else:
        valueLabel.set("Resultats\n---------------------------------------------\n"+result)   