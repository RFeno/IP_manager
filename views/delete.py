from tkinter import Button, Canvas, Entry

from images import image_button_suppression
def DisplayDelete(WindowMain):

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
    
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_1.place(
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
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    
    button_suppression.place(
        x=272.0,
        y=334.0,
        width=255.0,
        height=59.0
    )
    
