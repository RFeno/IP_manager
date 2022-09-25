from tkinter import *


def displayMenuTwo(WindowMain,framePoint2):
    
    #changement titre
    WindowMain.title("Projet LABO_TCPIP - Point 2")
    #création des composants
    Label(framePoint2, text="Veuillez encoder l'adresse IP ", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=1)
    Button(framePoint2, text="Générer les informations ").grid(column=2, row=7, padx=200, pady=30, ipadx=50)
    Entry(framePoint2,text="IP").grid(column=2, row=5, pady=25)
    
    #ajout du conteneur
    framePoint2.grid()