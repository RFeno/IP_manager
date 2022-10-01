from tkinter import *
from tkinter import messagebox

from model.point5 import genererPoint5

def displayMenuFive(WindowMain,framePoint5):

    global valueLabel
    
    numberOfSubNet = StringVar()
    numberOfHosts = StringVar()
    IpAdress = StringVar()
    maskAdress = StringVar()
    valueLabel = StringVar()

    #changement titre
    WindowMain.title("Projet LABO_TCPIP - Point 5")
    
    #création des composants
    Label(framePoint5, text="Veuillez encoder l'adresse IP", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=1)
    Entry(framePoint5, textvariable=IpAdress).grid(column=2, row=2, pady=15)
    
    Label(framePoint5, text="Veuillez encoder le masque de l'adrese IP ", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=3)
    Entry(framePoint5, textvariable=maskAdress).grid(column=2, row=4, pady=15)
    
    Label(framePoint5, text="Veuillez encoder le nombre de sous-réseaux", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=5)
    Entry(framePoint5, textvariable=numberOfSubNet).grid(column=2, row=6, pady=15)
    
    Label(framePoint5, text="Veuillez encoder le nombre d'hôtes", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=7)
    Entry(framePoint5, textvariable=numberOfHosts).grid(column=2, row=8, pady=15)

    Label(framePoint5, textvariable=valueLabel, font=("Impact",10),foreground="white", background="#009790").grid(column=2, row=9)
    
    Button(framePoint5, text="Générer les informations",command=lambda:genererInformationsFive(numberOfSubNet.get(),numberOfHosts.get(),IpAdress.get(),maskAdress.get()).grid(column=2, row=11, padx=200, pady=30, ipadx=50))
    
    
    #ajout du conteneur
    framePoint5.grid()

    def genererInformationsFive(numberOfSubNet, numberOfHosts, IpAdress, maskAdress):
    
        result = genererPoint5(numberOfSubNet, numberOfHosts, IpAdress, maskAdress)
        
        #traitement
        if((result == "IpInvalid")):
            messagebox.showerror("ERREUR", "L'adrese IP de la première machine encodée n'est pas valide\nmerci de d'en choisir une autre !")
        elif((result == "MaskInvalid")):
            messagebox.showerror("ERREUR", "L'adrese de masque de la première machine encodée n'est pas valide\nmerci de d'en choisir une autre !")
        elif((result == "NbSubnetsInvalid")):
            messagebox.showerror("ERREUR", "Le nombre de sous-réseaux encodé n'est pas valide\nmerci de d'en choisir une autre !")
        elif((result == "NbHostsInvalid")):
            messagebox.showerror("ERREUR", "Le nombre d'hôtes encodé n'est pas valide\nmerci de d'en choisir une autre !")
        else:
            valueLabel.set("Resultats\n---------------------------------------------\n"+result) 