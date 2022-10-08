from tkinter import Button, Canvas, Entry, StringVar, messagebox

from util.db import createUser
from images import *

import views.login as lg
def displayAddUser(WindowMain):
    
    global windowFromMain
    global password_value 
    global username_value
    username = StringVar()
    password = StringVar()
    windowFromMain = WindowMain
    
    #mise à jour du titre de la fenêtre
    WindowMain.title("Projet LABO_TCPIP - Inscription")
    
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
        235.0,
        116.0,
        anchor="nw",
        text="Ajouter un utilisateur",
        fill="#212B27",
        font=("Karla Bold", 36 * -1)
    )

    
    entry_username = Entry(
        textvariable=username,
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0,
    )
    
    entry_username.place(
        x=222.0,
        y=238.0,
        width=355.0,
        height=53.0
    )
    
    
    entry_password = Entry(
        textvariable=password,
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0,
        show="*"
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

    button_create = Button(
        image=image_button_creer_compte,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: addUser(username.get(), password.get()),
        relief="flat"
    )

    button_create.place(
        x=273.0,
        y=384.0,
        width=255.0,
        height=59.0
    )
    
    button_deja_compte = Button(
        image=image_button_deja_compte,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: lg.DisplayLogin(windowFromMain),
        relief="flat"
    )
    
    button_deja_compte.place(
        x=294.0,
        y=466.0,
        width=213.0,
        height=32.0
    )
    

def addUser(username,password):
    
    result = createUser(username,password)

    if ((result == "passwordTooSmall")):
        messagebox.showerror("ERREUR", "Le mot de passe que vous avez choisit doit dépasser 4 caractères.")
    elif((result == "usernameTooSmall")):
        messagebox.showerror("ERREUR", "Le nom d'utilisateur que vous avez choisit doit dépasser 4 caractères.")
    elif((result == "UserAlreadyExist")):
        messagebox.showerror("ERREUR", "Le nom d'utilisateur que vous avez choisit existe déjà merci d'en choisir un autre !")
    elif((result == "ErrorCreation")):
        messagebox.showerror("ERREUR", "Erreur lors de la création de l'utilisateur dans la base de données !")
    elif (result == "UserCree"):
        messagebox.showinfo("Succès","L'utilisateur a bien été créé")
    
    
    