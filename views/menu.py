from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
from PIL import ImageTk, Image

from views.viewPoint1 import displayMenuOne
from views.viewPoint2 import displayMenuTwo
from views.viewPoint3 import displayMenuThree
from views.viewPoint4 import displayMenuFour
from views.viewPoint5 import displayMenuFive

def HiddenAllWindow(frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5):
    
    frameMain.grid_forget()
    framePoint1.grid_forget()
    framePoint2.grid_forget()
    framePoint3.grid_forget()
    framePoint4.grid_forget()
    framePoint5.grid_forget()

    
def displayPoint1(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5):
    
    #cacher les fenêtres
    HiddenAllWindow(frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5)
    
    #création de menu de retour 
    ttk.Button(framePoint1, text="Retour au menu",command=lambda: displayMenuMain(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5)).grid(column=2,row=9)
    
    #créer la fenêtre du point 1
    displayMenuOne(WindowMain,framePoint1)
    
def displayPoint2(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5):
    
    #cacher les fenêtres
    HiddenAllWindow(frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5)
    
    #création de menu de retour 
    ttk.Button(framePoint2, text="Retour au menu",command=lambda: displayMenuMain(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5)).grid(column=2,row=11)
    
    #créer la fenêtre du point 2
    displayMenuTwo(WindowMain,framePoint2)

def displayPoint3(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5):
    
    #cacher les fenêtres
    HiddenAllWindow(frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5)
    
    #création de menu de retour 
    ttk.Button(framePoint3, text="Retour au menu",command=lambda: displayMenuMain(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5)).grid(column=2,row=9)
    
    #créer la fenêtre du point 2
    displayMenuThree(WindowMain,framePoint3)

def displayPoint4(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5):
    
    #cacher les fenêtres
    HiddenAllWindow(frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5)
    
    #création de menu de retour 
    ttk.Button(framePoint4, text="Retour au menu",command=lambda: displayMenuMain(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5)).grid(column=2,row=11)
    
    #créer la fenêtre du point 2
    displayMenuFour(WindowMain,framePoint4)
    
def displayPoint5(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5):
    
    #cacher les fenêtres
    HiddenAllWindow(frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5)
    
    #création de menu de retour 
    ttk.Button(framePoint5, text="Retour au menu",command=lambda: displayMenuMain(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5)).grid(column=2,row=11)
    
    #créer la fenêtre du point 2
    displayMenuFive(WindowMain,framePoint5)
       
    
def displayAbout():
    
    print("A propos")
    
def displayMenuMain(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5):
    
    global windowFromMain 
    windowFromMain = WindowMain
    
    #cacher les fenêtre
    HiddenAllWindow(frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5)
    
    #changement titre
    windowFromMain.title("Projet LABO_TCPIP - Menu d'accueil")
    
    #création des sections du menu
    frameMenuPoint1 = Frame(frameMain,style='My.TFrame')
    frameMenuPoint2 = Frame(frameMain,style='My.TFrame')
    frameMenuPoint3 = Frame(frameMain,style='My.TFrame')
    frameMenuPoint4 = Frame(frameMain,style='My.TFrame')
    frameMenuPoint5 = Frame(frameMain,style='My.TFrame')
    
    #Point 1 composants
    Label(frameMenuPoint1, text="1. Trouver les informations de l'adresse IP                      ",foreground="white",font=("Impact",15),background="#009790").grid(column=0, row=0)
    Label(frameMenuPoint1, text="A. Classe \nB. Nombre de réseaux \nC. Nombre d'hôtes                                                            ",foreground="white",font=("Arial",10),background="#009790").grid(column=0, row=1)
    Button(frameMain, text="Accéder (point 1)",command=lambda: displayPoint1(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5)).grid(column=5, row=1)

    #Point 2 composants
    Label(frameMenuPoint2, text="2. Trouver les informations de l'adresse IP                     ",foreground="white",font=("Impact",15),background="#009790").grid(column=0, row=3)
    Label(frameMenuPoint2, text="A. Adresse de réseau\nB. Adresse de broadcast\nC. Adresse de sous-réseau                                                        ",foreground="white",font=("Arial",10),background="#009790").grid(column=0, row=4)
    Button(frameMain, text="Accéder (point 2)",command=lambda: displayPoint2(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5)).grid(column=5, row=2)

    #Point 3 composants
    Label(frameMenuPoint3, text="3. L'IP apartient-il au réseau ?                                              ",foreground="white",font="Impact",background="#009790").grid(column=0, row=6)
    Button(frameMain, text="Accéder (point 3)",command=lambda: displayPoint3(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5)).grid(column=5, row=3)

    #Point 4 composants
    Label(frameMenuPoint4, text="4. Deux adresses sont-elles dans le même réseau ?   ",foreground="white",font="Impact",background="#009790").grid(column=0, row=9)
    Button(frameMain, text="Accéder (point 4)",command=lambda: displayPoint4(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5)).grid(column=5, row=4)

    Label(frameMenuPoint5, text="5. Déterminer les possibilités                                                ",foreground="white",font="Impact",background="#009790").grid(column=0, row=12)
    Label(frameMenuPoint5, text="A. Le nombre d'hôtes\nB. Découpe sur nombre de sous-réseaux \nC. Découpe par nombre d'adresse IP                                           ",foreground="white",font=("Arial",10),background="#009790").grid(column=0, row=13)
    Button(frameMain, text="Accéder (point 5)",command=lambda: displayPoint5(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5)).grid(column=5, row=5)

    #ajout des points dans le menu principal
    Label(frameMain, text="Menu principal ",foreground="white",font=("Impact",15),background="#009790").grid(column=0, row=0, pady=5)
    frameMenuPoint1.grid(column=0, row=1)
    frameMenuPoint2.grid(column=0, row=2)
    frameMenuPoint3.grid(column=0, row=3)
    frameMenuPoint4.grid(column=0, row=4)
    frameMenuPoint5.grid(column=0, row=5)
    
      
    #ajout du bouton exit
    Button(frameMain,text="Fermer", command=ExitApp).grid(column=5, row=12)
    
    createMenuBar(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5)
    
    #ajout du menu principal
    frameMain.grid()


#création et configurationd de la menubarre
def createMenuBar(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5):
    

    menubar = Menu(WindowMain)

    menu1 = Menu(menubar, tearoff=0)
    menu2 = Menu(menubar, tearoff=0)

    menu1.add_command(label="Accueil", command=lambda: displayMenuMain(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5))
    menu1.add_command(label="Point1",  command=lambda: displayPoint1(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5))
    menu1.add_command(label="Point 2", command=lambda: displayPoint2(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5))
    menu1.add_command(label="Point 3", command=lambda: displayPoint3(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5))
    menu1.add_command(label="Point 4", command=lambda: displayPoint4(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5))
    menu1.add_command(label="Point 5", command=lambda: displayPoint5(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5))
    
    menu1.add_separator()
    
    menu1.add_command(label="Quitter", command=ExitApp)
    menubar.add_cascade(label="Menu", menu=menu1)
    
    menu2.add_command(label="A propos", command=displayAbout)
    menubar.add_cascade(label="Info", menu=menu2)

    #ajout de la barre de menu
    WindowMain.config(menu=menubar)


def ExitApp():
    MsgBox = messagebox.askquestion ('Fermer','Voulez-vous vraiment quitter l\'application?',icon = 'warning')
    if MsgBox == 'yes':
       windowFromMain.destroy()