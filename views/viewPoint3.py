from tkinter import *
from tkinter import messagebox

from model.point3 import genererPoint3


def displayMenuThree(WindowMain,framePoint3):

    global valueLabel
    
    valueAdresse = StringVar()
    valueMasque = StringVar()
    valueAdresseReseau = StringVar()
    valueLabel = StringVar()

    #changement titre
    WindowMain.title("Projet LABO_TCPIP - Point 3")
    
    #création des composants
    Label(framePoint3, text="Veuillez encoder l'adresse IP", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=1)
    Entry(framePoint3,textvariable=valueAdresse).grid(column=2, row=2, pady=15)
    
    
    Label(framePoint3, text="Veuillez encoder le masque de l'adrese IP ", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=3)
    Entry(framePoint3,textvariable=valueMasque).grid(column=2, row=4, pady=15)
    
    Label(framePoint3, text="Le réseau dont vous voulez vérifier l'appartenance ", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=5)
    Entry(framePoint3,textvariable=valueAdresseReseau).grid(column=2, row=6, pady=15)

    Label(framePoint3, textvariable=valueLabel, font=("Impact",10),foreground="white", background="#009790").grid(column=2, row=7)
    
    
    Button(framePoint3, text="Vérifier la correspondance",command=lambda:genererInformationsThree(valueAdresse.get(),valueMasque.get(),valueAdresseReseau.get())).grid(column=2, row=9, padx=200, pady=30, ipadx=50)
    
    
    #ajout du conteneur
    framePoint3.grid()

def genererInformationsThree(IpAdress, MaskAdress, IpNetworkAdress):
    
    result = genererPoint3(IpAdress, MaskAdress, IpNetworkAdress)
    
    #traitement
    if((result == "IpInvalid")):
        messagebox.showerror("ERREUR", "L'adrese IP encodée n'est pas valide\nmerci de d'en choisir une autre !")
    elif((result == "MaskInvalid")):
        messagebox.showerror("ERREUR", "L'adrese de masque encodée n'est pas valide\nmerci de d'en choisir une autre !")
    elif((result == "IpNetworkInvalid")):
        messagebox.showerror("ERREUR", "L'adrese IP du réseau encodée n'est pas valide\nmerci de d'en choisir une autre !")
    else:
        valueLabel.set("Resultats\n---------------------------------------------\n"+result)  