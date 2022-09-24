from ast import In
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.ttk import *


def displayMenuThree(WindowMain,framePoint3):
    #changement titre
    WindowMain.title("Projet LABO_TCPIP - Point 3")
    
    #création des composants
    ttk.Label(framePoint3, text="Veuillez encoder l'adresse IP", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=1)
    Entry(framePoint3).grid(column=2, row=2, pady=15)
    
    
    ttk.Label(framePoint3, text="Veuillez encoder le masque de l'adrese IP ", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=3)
    Entry(framePoint3).grid(column=2, row=4, pady=15)
    
    ttk.Label(framePoint3, text="Le réseau dont vous voulez vérifier l'appartenance ", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=5)
    Entry(framePoint3).grid(column=2, row=6, pady=15)
    
    ttk.Button(framePoint3, text="Vérifier la correspondance").grid(column=2, row=7, padx=200, pady=30, ipadx=50)
    
    
    #ajout du conteneur
    framePoint3.grid()