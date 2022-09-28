from tkinter import *

window = Tk()



#changer le titre de la fenetre

window.title("Mon application")
window.geometry("300x300")
window.minsize(300,300)
l = LabelFrame(window, text="Titre de la frame", padx=20, pady=20)
l.pack(fill="both", expand="yes")
 
Label(l, text="A l'intérieure de la frame").pack()

#afficher la fenetre
window.mainloop()

