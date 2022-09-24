#Imports
import bcrypt
import sqlite3
from tkinter import *
from tkinter.ttk import *
from views.menu import *

#création de la fenêtre principale
WindowMain = Tk()

#création des conteneurs
frameMain   = Frame(WindowMain, padding=30, style='My.TFrame')
framePoint1 = Frame(WindowMain, padding=30, style='My.TFrame')
framePoint2 = Frame(WindowMain, padding=30, style='My.TFrame')
framePoint3 = Frame(WindowMain, padding=30, style='My.TFrame')
framePoint4 = Frame(WindowMain, padding=30, style='My.TFrame')
framePoint5 = Frame(WindowMain, padding=30, style='My.TFrame')

#ajout du titre de la fenêtre
WindowMain.title("Projet LABO_TCPIP - Menu d'accueil")

#taille minimale de la enêtre
WindowMain.minsize(700,550)
WindowMain.maxsize(700,550)

#ajout de l'icone (image)
WindowMain.iconbitmap("ressources/images/logoLabo4_1.ico")

#configuration visuelle de la fenêtre
WindowMain.config(background="#009790")

styleMain = Style()
styleMain.configure('My.TFrame', background="#009790", font="Impact")

#création du menu principal 
displayMenuMain(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5)

#A EFFACER
"""frameMain.grid_forget()
displayMenuFive(WindowMain,framePoint5)"""

#affichage de la fenêtre principale
WindowMain.mainloop()


