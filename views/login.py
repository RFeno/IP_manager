from importlib.metadata import entry_points
from tkinter import messagebox

from util.db import checkUserPassword, createUser
from tkinter import *
from tkinter.ttk import *
from tkinter import PhotoImage, Tk

from images import *
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from views.addUser import displayAddUser

from views.menu import displayMenuMain


def DisplayLogin(WindowMain):
    #changement titre
    WindowMain.title("Projet LABO_TCPIP - Connexion")
    
    global windowFromMain
    windowFromMain = WindowMain
    
    #création des composants
    usernamevalue = StringVar()
    passwordvalue = StringVar()
    
    #global pour êtres appelés dans d'autres méthodes
    global canvas
    
    
    canvas = Canvas(
    WindowMain,
    bg = "#A7D7C5",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)

    canvas.create_rectangle(
        173.0,
        79.0,
        628.0,
        534.0,
        fill="#F6FBF9",
        outline="")

    canvas.create_text(
        309.0,
        116.0,
        anchor="nw",
        text="Connexion",
        fill="#212B27",
        font=("Karla Bold", 36 * -1)
    )

    entry_username = Entry(
        textvariable=usernamevalue,
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    
    entry_username.place(
        x=222.0,
        y=238.0,
        width=355.0,
        height=53.0
    )

    entry_password = Entry(
        show="*",
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0,
        textvariable=passwordvalue
    )
    entry_password.place(
        x=225.0,
        y=318.0,
        width=355.0,
        height=53.0
    )

    canvas.create_text(
        215.0,
        212.0,
        anchor="nw",
        text="Nom d’utilisateur",
        fill="#000000",
        font=("Karla Regular", 15 * -1)
    )

    canvas.create_text(
        215.0,
        292.0,
        anchor="nw",
        text="Mot de passe",
        fill="#000000",
        font=("Karla Regular", 15 * -1)
    )

    
    button_Create = Button(
        text="Créer le compte",
        image=image_button_connexion,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda:connexion(usernamevalue.get(),passwordvalue.get(),WindowMain)
    )
    
    button_Create.place(
        x=273.0,
        y=384.0,
        width=255.0,
        height=59.0
    )
    
    button_pas_de_compte = Button(
        image=image_button_pas_de_compte,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: displayAddUser(WindowMain),
        relief="flat"
    )
    
    button_pas_de_compte.place(
        x=294.0,
        y=466.0,
        width=213.0,
        height=32.0
    )
    
    
def connexion(username,password,WindowMain):
    if(checkUserPassword(username, password)):
        print("identifiants valides")
        
        #suprression de l'ancienne fenêtre
        canvas.destroy()
        
        displayMenuMain(WindowMain)
    else:
        print("identifiants invalides")
        
        #showing error
        messagebox.showerror("ERREUR", "Les identifiants sont invalides")

