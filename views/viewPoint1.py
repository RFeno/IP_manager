from ast import In
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.ttk import *


def displayMenuOne(WindowMain,framePoint1):

    
    #changement titre
    WindowMain.title("Projet LABO_TCPIP - Point 1")
    #création des composants
    ttk.Label(framePoint1, text="Veuillez encoder l'adresse IP ", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=1)
    ttk.Button(framePoint1, text="Générer les informations ").grid(column=2, row=7, padx=200, pady=30, ipadx=50)
    Entry(framePoint1,text="IP").grid(column=2, row=5, pady=25)
    
    
    #ajout du conteneur
    framePoint1.grid()
    