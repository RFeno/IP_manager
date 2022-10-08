#Imports
from tkinter import *

#active ou desactive l'accès avec mot de passe
active_login = False

#création de la fenêtre principale
WindowMain= Tk()

#ajout du titre de la fenêtre
WindowMain.title("Projet LABO_TCPIP - Connexion")

#taille minimale de la enêtre
WindowMain.geometry("800x630")
WindowMain.resizable(False, False)

#ajout de l'icone (image)
WindowMain.iconbitmap("ressources/images/logoLabo4_1.ico")

#configuration visuelle de la fenêtre
WindowMain.configure(bg = "#A7D7C5")

#import ici car sinon runtime error car images crées avant le mainWindow
from views.login import DisplayLogin
from views.menu import displayMenuMain

if(active_login):
    DisplayLogin(WindowMain)
else:
    displayMenuMain(WindowMain)

#affichage de la fenêtre principale
WindowMain.mainloop()