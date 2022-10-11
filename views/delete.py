from tkinter import Button, Canvas, Entry, StringVar, messagebox

from images import image_button_suppression
from util.db import deleteUser
import views.login as lg
import views.menu as menu

def DisplayDelete(WindowMain):


    username = StringVar()
    
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
        292.0,
        116.0,
        anchor="nw",
        text="Suppression",
        fill="#212B27",
        font=("Karla Bold", 36 * -1)
    )
    
    entry_username = Entry(
        textvariable=username,
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

    canvas.create_text(
        332.0,
        209.0,
        anchor="nw",
        text="Nom d’utilisateur",
        fill="#000000",
        font=("Karla Regular", 15 * -1)
    )

    button_suppression = Button(
        image=image_button_suppression,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: delete(username.get()),
        relief="flat"
    )
    
    button_suppression.place(
        x=272.0,
        y=334.0,
        width=255.0,
        height=59.0
    )
    
    def delete(username):
        
        verification = messagebox.askquestion ('Supression',f'Voulez-vous vraiment supprimer l\'utilisateur : {username} ',icon = 'warning')
        
        if(verification == 'yes'):
            #récupération du resultat de l'impression
            result = deleteUser(username)
            
            #affichage à l'écran
            if ((result == "UserDoesNotExist")):
                messagebox.showinfo("ERREUR", "Le nom d'utilisateur que vous avez encodé n'existe pas !")
            elif((result == "UserDeleted")):
                messagebox.showinfo("INFORMATION", "L'utilisateur que vous avez encodé à bien été supprimé.")
                
                #on vérifie si l'utilisateur connecté est celui qui vient d'être supprimé
                
                print(f"Utilisateur connecté:{lg.userLog}, utilisateur supprimé: {username}")
                
                if(lg.userLog==username):
                    messagebox.showinfo("INFORMATION","Vous avez supprimé le compte avec lequel vous êtes connecté\nVous allez donc être deconnecté")
                    
                    lg.DisplayLogin(WindowMain)
                    menu.remove_menubar()
                
            elif((result == "dbError")):
                messagebox.showerror("ERREUR", "Une erreur s'est produite, l'utilisateur n'a pas été supprimé")
                





   
