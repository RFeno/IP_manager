from tkinter import *

def displayMenuFour(WindowMain,framePoint4):
    #changement titre
    WindowMain.title("Projet LABO_TCPIP - Point 4")
    
    #création des composants
    Label(framePoint4, text="Veuillez encoder la première adresse IP", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=1)
    Entry(framePoint4).grid(column=2, row=2, pady=15)
    
    Label(framePoint4, text="Veuillez encoder le masque de la première adrese IP ", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=3)
    Entry(framePoint4).grid(column=2, row=4, pady=15)
    
    Label(framePoint4, text="Veuillez encoder la deuxième adresse IP ", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=5)
    Entry(framePoint4).grid(column=2, row=6, pady=15)
    
    Label(framePoint4, text="Veuillez encoder le masque de la  deuxième adresse IP", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=7)
    Entry(framePoint4).grid(column=2, row=8, pady=15)
    
    Button(framePoint4, text="Vérifier les correspondances").grid(column=2, row=9, padx=200, pady=30, ipadx=50)
    
    
    #ajout du conteneur
    framePoint4.grid()