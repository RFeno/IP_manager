from ast import In
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter.font as font

"""Fenêtre Principale"""
#création de la fenêtre principale
WindowMain = Tk()

#ajout du titre de la fenêtre
WindowMain.title("Projet LABO_TCPIP - Menu d'accueil")

#taille minimale de la enêtre
WindowMain.minsize(500,500)

#ajout de l'icone (iamge)
WindowMain.iconbitmap("ressources/images/logoLabo4_1.ico")

#configuration visuelle de la fenêtre
WindowMain.config(background="#009790")
styleMain = Style()
styleMain.configure('My.TFrame', background="#009790", font="Impact")
"""Fin Fenêtre Principale"""

#fonctions

"""Créations des composants"""
frameMain = Frame(WindowMain, padding=30, style='My.TFrame')
framePoint1 = Frame(WindowMain, padding=30,style='My.TFrame')
framePoint2 = Frame(WindowMain, padding=30,style='My.TFrame')
framePoint3 = Frame(WindowMain, padding=30,style='My.TFrame')
framePoint4 = Frame(WindowMain, padding=30,style='My.TFrame')
framePoint5 = Frame(WindowMain, padding=30,style='My.TFrame')

"""Fin création des composants"""

def HiddenAllWindow():
    frameMain.grid_forget()
    framePoint1.grid_forget()
    framePoint2.grid_forget()
    framePoint3.grid_forget()
    framePoint4.grid_forget()
    framePoint5.grid_forget()

    
def displayPoint1():
    
    #cacher les fenêtre
    HiddenAllWindow()
    
    #changement titre
    WindowMain.title("Projet LABO_TCPIP - Point 1")
    
    #ajout du conteneur
    framePoint1.grid()
    
    #création des composants
    ttk.Label(framePoint1, text="1.Salut mec").grid(column=0, row=1)
    ttk.Button(framePoint1, text="Valider (point 1)", ).grid(column=2, row=1)


    
def displayAbout():
    print("A propos")
    
def displayMenuMain():
    
    #cacher les fenêtre
    HiddenAllWindow()
    
    #changement titre
    WindowMain.title("Projet LABO_TCPIP - Menu d'accueil")
    
    #création des sections du menu
    frameMenuPoint1 = Frame(frameMain,style='My.TFrame')
    frameMenuPoint2 = Frame(frameMain,style='My.TFrame')
    frameMenuPoint3 = Frame(frameMain,style='My.TFrame')
    frameMenuPoint4 = Frame(frameMain,style='My.TFrame')
    frameMenuPoint5 = Frame(frameMain,style='My.TFrame')
    myFont = font.Font(family='Helvetica')
    
    #Point 1 composants
    Label(frameMenuPoint1, text="1. Trouver les informations de l'adresse IP                      ",foreground="white",font=("Impact",15),background="#009790").grid(column=0, row=0)
    Label(frameMenuPoint1, text="A. Classe \nB. Nombre de réseaux \nC. Nombre de machines                                                             ",foreground="white",font=("Arial",10),background="#009790").grid(column=0, row=1)
    Button(frameMain, text="Accéder (point 1)",command=displayPoint1).grid(column=5, row=1)
  
   

    #Point 2 composants
    Label(frameMenuPoint2, text="2. Trouver les informations de l'adresse IP                     ",foreground="white",font=("Impact",15),background="#009790").grid(column=0, row=3)
    Label(frameMenuPoint2, text="A. Adresse de réseau\nB. Adresse de broadcast\nC. Adresse de sous-réseau                                                        ",foreground="white",font=("Arial",10),background="#009790").grid(column=0, row=4)
    Button(frameMain, text="Accéder (point 2)").grid(column=5, row=2)

    #Point 3 composants
    Label(frameMenuPoint3, text="3. L'IP apartient-il au réseau ?                                              ",foreground="white",font="Impact",background="#009790").grid(column=0, row=6)
    Button(frameMain, text="Accéder (point 3)").grid(column=5, row=3)

    #Point 4 composants
    Label(frameMenuPoint4, text="4. Deux adresses sont-elles dans le même réseau ?   ",foreground="white",font="Impact",background="#009790").grid(column=0, row=9)
    Button(frameMain, text="Accéder (point 4)").grid(column=5, row=4)

    Label(frameMenuPoint5, text="5. Déterminer les possibilités                                                ",foreground="white",font="Impact",background="#009790").grid(column=0, row=12)
    Label(frameMenuPoint5, text="A. Le nombre d'hôtes\nB. Découpe sur nombre de sous-réseaux \nC. Découpe par nombre d'adresse IP                                           ",foreground="white",font=("Arial",10),background="#009790").grid(column=0, row=13)
    Button(frameMain, text="Accéder (point 5)").grid(column=5, row=5)

    #import image
    image_button_exit = PhotoImage(file="ressources/images/exit2.png")
    #resize
    image_button_exit_photo = image_button_exit.subsample(6,6)

    Button(frameMain,text="Exit", image=image_button_exit_photo, command=WindowMain.destroy).grid(column=5, row=6)
    
    #ajout des points dans le menu principal
    frameMenuPoint1.grid(column=0, row=1)
    frameMenuPoint2.grid(column=0, row=2)
    frameMenuPoint3.grid(column=0, row=3)
    frameMenuPoint4.grid(column=0, row=4)
    frameMenuPoint5.grid(column=0, row=5)
    
    #ajout du menu principal
    frameMain.grid()


#création et configurationd de la menubarre
menubar = Menu(WindowMain)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Accueil", command=displayMenuMain)
menu1.add_command(label="Point1", command=displayPoint1)
menu1.add_command(label="Point 2", command=displayPoint1)
menu1.add_command(label="Point 3", command=displayPoint1)
menu1.add_command(label="Point 4", command=displayPoint1)
menu1.add_command(label="Point 5", command=displayPoint1)
menu1.add_separator()
menu1.add_command(label="Quitter", command=WindowMain.quit)
menubar.add_cascade(label="Menu", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="A propos", command=displayAbout)
menubar.add_cascade(label="Info", menu=menu2)

WindowMain.config(menu=menubar)

displayMenuMain()
#afficher la fenêtre 
WindowMain.mainloop()

