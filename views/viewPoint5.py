from tkinter import *

def displayMenuFive(WindowMain,framePoint5):
    #changement titre
    WindowMain.title("Projet LABO_TCPIP - Point 5")
    
    #création des composants
    Label(framePoint5, text="Veuillez encoder l'adresse IP", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=1)
    Entry(framePoint5).grid(column=2, row=2, pady=15)
    
    Label(framePoint5, text="Veuillez encoder le masque de l'adrese IP ", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=3)
    Entry(framePoint5).grid(column=2, row=4, pady=15)
    
    Label(framePoint5, text="Veuillez encoder le nombre de sous-réseaux", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=5)
    Entry(framePoint5).grid(column=2, row=6, pady=15)
    
    Label(framePoint5, text="Veuillez encoder le nombre d'hôtes", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=7)
    Entry(framePoint5).grid(column=2, row=8, pady=15)
    
    Button(framePoint5, text="Générer les informations").grid(column=2, row=9, padx=200, pady=30, ipadx=50)
    
    
    #ajout du conteneur
    framePoint5.grid()