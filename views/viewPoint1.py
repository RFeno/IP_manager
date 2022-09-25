from ast import In
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter.ttk import *

from util.point1 import genererPoint1


def displayMenuOne(WindowMain,framePoint1):

    global valueLabel
    valueLabel = StringVar()
    #changement titre
    WindowMain.title("Projet LABO_TCPIP - Point 1")
    #création des composants
    ttk.Label(framePoint1, text="Veuillez encoder l'adresse IP ", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=1)
    labelResult = ttk.Label(framePoint1, textvariable=valueLabel, font=("Impact",10),foreground="white", background="#009790").grid(column=2, row=0)
    valueEntry = StringVar()
    entryIP = Entry(framePoint1,textvariable=valueEntry).grid(column=2, row=5, pady=25)
    ttk.Button(framePoint1, text="Générer les informations",command=lambda:generateInformationsOne(valueEntry.get())).grid(column=2, row=7, padx=200, pady=30, ipadx=50)
    
    #ajout du conteneur
    framePoint1.grid()
    

def generateInformationsOne(entryIP):
    refreshLabel(genererPoint1(entryIP))
    
    
def refreshLabel(resultString):

    if(resultString == "IpInvalid"):
        valueLabel.set("")
        messagebox.showerror("ERREUR", "L'adrese IP encodée n'est pas valide, merci de d'en choisir une autre !")
    else:
        valueLabel.set(f"Resultat :\n{resultString}\n")