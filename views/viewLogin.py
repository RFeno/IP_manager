from tkinter import *
from tkinter import messagebox

from util.checkUser import checkUserPassword
from views.menu import displayMenuMain 

def DisplayLogin(WindowMain,frameLogin,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5):
    #changement titre
    WindowMain.title("Projet LABO_TCPIP - Connexion")
    
    #création des composants
    usernamevalue = StringVar()
    passwordvalue = StringVar()
    
    Label(frameLogin, text="Nom d'utilisateur", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=2)
    Entry(frameLogin, textvariable=usernamevalue).grid(column=2, row=3, pady=15)
    
    Label(frameLogin, text="Mot de passe", font=("Impact",15),foreground="white", background="#009790").grid(column=2, row=4)
    Entry(frameLogin, textvariable=passwordvalue).grid(column=2, row=5, pady=15)
    
    Button(frameLogin, text="Connexion", command=lambda:connexion(usernamevalue.get(),passwordvalue.get(),WindowMain,frameMain,frameLogin,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5)).grid(column=2, row=9, padx=200, pady=30, ipadx=50)
    
    #ajout du conteneur
    frameLogin.grid()
    
    
def connexion(username,password,WindowMain,frameMain,frameLogin,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5):
    if(checkUserPassword(username, password)):
        print("identifiants valides")
        frameLogin.grid_forget()
        displayMenuMain(WindowMain,frameMain,framePoint1,framePoint2,framePoint3,framePoint4,framePoint5)
    else:
        print("identifiants invalides, nouvel essai")
        messagebox.showerror("ERREUR", "Les identifiants sont invalides")
    