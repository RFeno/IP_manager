
from tkinter import Button, Canvas, Entry, Menu, messagebox


from images import *
from model.point1  import genererPoint1
from model.point2  import genererPoint2
from model.point3  import genererPoint3
from model.point4  import genererPoint4
from model.point5  import genererPoint5
from views.addUser import displayAddUser
from views.delete  import DisplayDelete

def HiddenAllWindow():
    
    canvas.destroy()
    
def displayPoint1():
    
    #cacher les fenêtres
    HiddenAllWindow()
    
    canvas = Canvas(
    windowFromMain,
    bg = "#A7D7C5",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        478.0,
        307.00000381469727,
        930.54833984375,
        759.5483436584473,
        fill="#C1E3D6",
        outline="")

    canvas.create_rectangle(
        109.0,
        141.0,
        561.54833984375,
        593.54833984375,
        fill="#C1E3D6",
        outline="")

    canvas.create_rectangle(
        19.0,
        72.0,
        400.0,
        533.0,
        fill="#F6FBF9",
        outline="")

    canvas.create_rectangle(
        411.0,
        136.0,
        782.0,
        464.0,
        fill="#F6FBF9",
        outline="")

    canvas.create_text(
        542.0,
        165.0,
        anchor="nw",
        text="RÉSULTATS",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )

    canvas.create_text(
        344.0,
        14.0,
        anchor="nw",
        text="Point 1",
        fill="#F6FBF9",
        font=("Karla Bold", 36 * -1)
    )
    
    #ombre titre
    canvas.create_rectangle(
    319.0,
    0.0,
    484.0,
    61.0,
    fill="#C1E3D6",
    outline="")
    
    #titr fenêtre
    canvas.create_text(
        341.0,
        7.0,
        anchor="nw",
        text="Point 1",
        fill="#F6FBF9",
        font=("Karla", 36 * -1,"bold")
    )

    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_1.place(
        x=38.0,
        y=221.0,
        width=342.0,
        height=53.0
    )

    canvas.create_text(
        56.0,
        157.0,
        anchor="nw",
        text="Veuillez encoder l’adresse IP ",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )
    
    button_generer = Button(
        image=image_button_generer,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: refreshLabel(genererPoint1(entry_1.get())),
        relief="flat"
    )
    
    button_generer.place(
        x=73.0,
        y=346.0,
        width=255.0,
        height=59.0
    )

    #les résultats
    text_resultats = canvas.create_text(
        460.0,
        239.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Karla Bold", 15 * -1)
    )

    button_retour = Button(
        image=image_button_retour,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: displayMenuMain(windowFromMain),
        relief="flat"
    )
    button_retour.place(
        x=469.0,
        y=495.0,
        width=255.0,
        height=59.0
    )
    
    windowFromMain.title("Projet LABO_TCPIP - Point 1")
    
    def refreshLabel(resultString):
        
        if(resultString == "IpInvalid"):
            messagebox.showerror("ERREUR", "L'adrese IP encodée n'est pas valide, merci de d'en choisir une autre !")
        else:
            canvas.itemconfigure(text_resultats,text=f"------------------------------------------------------\n{resultString}\n",)
    
def displayPoint2():
    
    #cacher les fenêtres
    HiddenAllWindow()
    
    #changement titre
    windowFromMain.title("Projet LABO_TCPIP - Point 2")
    
    canvas = Canvas(
    windowFromMain,
    bg = "#A7D7C5",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        478.0,
        307.00000381469727,
        930.54833984375,
        759.5483436584473,
        fill="#C1E3D6",
        outline="")

    canvas.create_rectangle(
        109.0,
        141.0,
        561.54833984375,
        593.54833984375,
        fill="#C1E3D6",
        outline="")

    canvas.create_rectangle(
        19.0,
        72.0,
        400.0,
        533.0,
        fill="#F6FBF9",
        outline="")

    canvas.create_text(
        150.0,
        272.0,
        anchor="nw",
        text="Le masque",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )

    canvas.create_rectangle(
        411.0,
        136.0,
        782.0,
        464.0,
        fill="#F6FBF9",
        outline="")

    canvas.create_text(
        542.0,
        165.0,
        anchor="nw",
        text="RÉSULTATS",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )

    #ombre titre
    canvas.create_rectangle(
    319.0,
    0.0,
    484.0,
    61.0,
    fill="#C1E3D6",
    outline="")
    
    #titr fenêtre
    canvas.create_text(
        341.0,
        7.0,
        anchor="nw",
        text="Point 2",
        fill="#F6FBF9",
        font=("Karla", 36 * -1,"bold")
    )

    entry_Ip = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    
    entry_Ip.place(
        x=38.0,
        y=198.0,
        width=342.0,
        height=53.0
    )

    entry_Mask = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    
    entry_Mask.place(
        x=38.0,
        y=317.0,
        width=342.0,
        height=53.0
    )

    canvas.create_text(
        142.0,
        157.0,
        anchor="nw",
        text=" L’adresse IP ",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )

   
    button_generer = Button(
        image=image_button_generer,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: genererTwo(),
        relief="flat"
    )
    
    button_generer.place(
        x=82.0,
        y=427.0,
        width=255.0,
        height=59.0
    )

    text_resultats = canvas.create_text(
        448.0,
        235.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Karla Bold", 15 * -1)
    )

    button_retour = Button(
        image=image_button_retour,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: displayMenuMain(windowFromMain),
        relief="flat"
    )
    
    button_retour.place(
        x=469.0,
        y=495.0,
        width=255.0,
        height=59.0
    )
    
    def genererTwo():
        result = genererPoint2(entry_Ip.get(), entry_Mask.get())
        
        #traitement
        if((result == "IpInvalid")):
            messagebox.showerror("ERREUR", "L'adrese IP encodée n'est pas valide\nmerci de d'en choisir une autre !")
        elif((result == "MaskInvalid")):
            messagebox.showerror("ERREUR", "L'adrese de masque encodée n'est pas valide\nmerci de d'en choisir une autre !")
        elif((result == "MaskInvalidGlobal")):
            messagebox.showerror("ERREUR", "l'adresse de masque ne peut pas être plus englobante que l'adresse de classe\nmerci de d'en choisir une autre !")
        else:
            canvas.itemconfigure(text_resultats,text=f"------------------------------------------------------\n{result}\n",)  
    
def displayPoint3():
    
    #changement titre
    windowFromMain.title("Projet LABO_TCPIP - Point 3")
    
    #cacher les fenêtres
    HiddenAllWindow()
    
    canvas = Canvas(
    windowFromMain,
    bg = "#A7D7C5",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        478.0,
        307.00000381469727,
        930.54833984375,
        759.5483436584473,
        fill="#C1E3D6",
        outline="")

    canvas.create_rectangle(
        109.0,
        141.0,
        561.54833984375,
        593.54833984375,
        fill="#C1E3D6",
        outline="")

    canvas.create_rectangle(
        19.0,
        72.0,
        400.0,
        533.0,
        fill="#F6FBF9",
        outline="")

    canvas.create_text(
        150.0,
        190.0,
        anchor="nw",
        text="Le masque",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )

    canvas.create_text(
        158.0,
        303.0,
        anchor="nw",
        text="Le réseau",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )

    canvas.create_rectangle(
        411.0,
        136.0,
        782.0,
        464.0,
        fill="#F6FBF9",
        outline="")

    canvas.create_text(
        542.0,
        165.0,
        anchor="nw",
        text="RÉSULTATS",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )

    #ombre titre
    canvas.create_rectangle(
    319.0,
    0.0,
    484.0,
    61.0,
    fill="#C1E3D6",
    outline="")
    
    #titr fenêtre
    canvas.create_text(
        341.0,
        7.0,
        anchor="nw",
        text="Point 3",
        fill="#F6FBF9",
        font=("Karla", 36 * -1,"bold")
    )
    
    entry_IP = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_IP.place(
        x=38.0,
        y=116.0,
        width=342.0,
        height=53.0
    )

    entry_Mask = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    
    entry_Mask.place(
        x=38.0,
        y=226.0,
        width=342.0,
        height=53.0
    )
    
    entry_Network = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    
    entry_Network.place(
        x=38.0,
        y=339.0,
        width=342.0,
        height=53.0
    )

    canvas.create_text(
        142.0,
        89.0,
        anchor="nw",
        text=" L’adresse IP ",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )


    button_verifier = Button(
        image=image_button_verifier,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: genererThree(),
        relief="flat"
    )
    
    button_verifier.place(
        x=82.0,
        y=427.0,
        width=255.0,
        height=59.0
    )

    text_resultats = canvas.create_text(
        448.0,
        235.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Karla Bold", 15 * -1)
    )
    
    button_retour = Button(
        image=image_button_retour,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: displayMenuMain(windowFromMain),
        relief="flat"
    )
    
    button_retour.place(
        x=469.0,
        y=495.0,
        width=255.0,
        height=59.0
    )
    
    def genererThree():
    
        result = genererPoint3(entry_IP.get(), entry_Mask.get(), entry_Network.get())
        
        #traitement
        if((result == "IpInvalid")):
            messagebox.showerror("ERREUR", "L'adresse IP encodée n'est pas valide\nmerci de d'en choisir une autre !")
        elif((result == "MaskInvalid")):
            messagebox.showerror("ERREUR", "L'adresse de masque encodée n'est pas valide\nmerci de d'en choisir une autre !")
        elif((result == "IpNetworkInvalid")):
            messagebox.showerror("ERREUR", "L'adresse IP du réseau encodée n'est pas valide\nmerci de d'en choisir une autre !")
        elif((result == "MemeAdress")):
            messagebox.showerror("ERREUR", "L'adresse IP du réseau encodée ne peut pas être égale à l'adresse IP encodée !")
        else:
            canvas.itemconfigure(text_resultats,text=f"------------------------------------------------------\n{result}\n",)  
    
def displayPoint4():
    
    #changement titre
    windowFromMain.title("Projet LABO_TCPIP - Point 4")
    
    #cacher les fenêtres
    HiddenAllWindow()
    
    canvas = Canvas(
    windowFromMain,
    bg = "#A7D7C5",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        478.0,
        307.00000381469727,
        930.54833984375,
        759.5483436584473,
        fill="#C1E3D6",
        outline="")

    canvas.create_rectangle(
        109.0,
        141.0,
        561.54833984375,
        593.54833984375,
        fill="#C1E3D6",
        outline="")

    canvas.create_rectangle(
        19.0,
        72.0,
        400.0,
        533.0,
        fill="#F6FBF9",
        outline="")

    canvas.create_text(
        143.0,
        188.0,
        anchor="nw",
        text="Le masque 1",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )

    canvas.create_text(
        135.0,
        281.0,
        anchor="nw",
        text="L’adresse IP 2",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )

    canvas.create_text(
        140.0,
        374.0,
        anchor="nw",
        text="Le masque 2",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )

    canvas.create_rectangle(
        411.0,
        136.0,
        782.0,
        464.0,
        fill="#F6FBF9",
        outline="")

    canvas.create_text(
        542.0,
        165.0,
        anchor="nw",
        text="RÉSULTATS",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )

    #ombre titre
    canvas.create_rectangle(
    319.0,
    0.0,
    484.0,
    61.0,
    fill="#C1E3D6",
    outline="")
    
    #titr fenêtre
    canvas.create_text(
        341.0,
        7.0,
        anchor="nw",
        text="Point 4",
        fill="#F6FBF9",
        font=("Karla", 36 * -1,"bold")
    )
    
    entry_IP1 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    
    entry_IP1.place(
        x=38.0,
        y=116.0,
        width=342.0,
        height=53.0
    )

    entry_Mask1 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    
    entry_Mask1.place(
        x=38.0,
        y=217.0,
        width=342.0,
        height=53.0
    )


    entry_IP2 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    
    entry_IP2.place(
        x=38.0,
        y=312.0,
        width=342.0,
        height=53.0
    )

    
    entry_Mask2 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    
    entry_Mask2.place(
        x=38.0,
        y=409.0,
        width=342.0,
        height=53.0
    )

    canvas.create_text(
        135.0,
        89.0,
        anchor="nw",
        text=" L’adresse IP 1 ",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )

    button_verifier = Button(
        image=image_button_verifier_petit,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: genererFour(),
        relief="flat"
    )
    
    button_verifier.place(
        x=82.0,
        y=474.0,
        width=255.0,
        height=41.0
    )

    text_results = canvas.create_text(
        448.0,
        235.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Karla Bold", 15 * -1),
        width=300
    )

    button_retour = Button(
        image=image_button_retour,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: displayMenuMain(windowFromMain),
        relief="flat"
    )
    
    button_retour.place(
        x=469.0,
        y=495.0,
        width=255.0,
        height=59
    )
    
    text_results
    
    def genererFour():

        result = genererPoint4(entry_IP1.get(), entry_Mask1.get(), entry_IP2.get(), entry_Mask2.get())
        
        #traitement
        if((result == "IpInvalid1")):
            messagebox.showerror("ERREUR", "L'adrese IP de la première machine encodée n'est pas valide\nmerci de d'en choisir une autre !")
        elif((result == "MaskInvalid1")):
            messagebox.showerror("ERREUR", "L'adrese de masque de la première machine encodée n'est pas valide\nmerci de d'en choisir une autre !")
        elif((result == "IpInvalid2")):
            messagebox.showerror("ERREUR", "L'adrese IP de la deuxième machine encodée n'est pas valide\nmerci de d'en choisir une autre !")
        elif((result == "MaskInvalid2")):
            messagebox.showerror("ERREUR", "L'adrese de masque de la deuxième machine encodée n'est pas valide\nmerci de d'en choisir une autre !")
        else:
            canvas.itemconfigure(text_results,text=f"--------------------------------------------------------\n{result}\n",)
   
def displayPoint5():

    #changement titre
    windowFromMain.title("Projet LABO_TCPIP - Point 5")
    
    #cacher les fenêtres
    HiddenAllWindow()
    
    canvas = Canvas(
    windowFromMain,
    bg = "#A7D7C5",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        478.0,
        307.00000381469727,
        930.54833984375,
        759.5483436584473,
        fill="#C1E3D6",
        outline="")

    canvas.create_rectangle(
        109.0,
        141.0,
        561.54833984375,
        593.54833984375,
        fill="#C1E3D6",
        outline="")

    canvas.create_rectangle(
        19.0,
        72.0,
        400.0,
        533.0,
        fill="#F6FBF9",
        outline="")
        
    canvas.create_text(
        135.0,
        89.0,
        anchor="nw",
        text=" L’adresse IP",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )

    canvas.create_text(
        143.0,
        188.0,
        anchor="nw",
        text="Le masque",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )

    canvas.create_text(
        60.0,
        281.0,
        anchor="nw",
        text="Le nombre de sous-réseaux",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )

    canvas.create_text(
        110.0,
        374.0,
        anchor="nw",
        text="Le nombre d'hôtes",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )

    canvas.create_rectangle(
        411.0,
        136.0,
        782.0,
        464.0,
        fill="#F6FBF9",
        outline="")

    canvas.create_text(
        542.0,
        165.0,
        anchor="nw",
        text="RÉSULTATS",
        fill="#000000",
        font=("Karla Regular", 24 * -1)
    )

    #ombre titre
    canvas.create_rectangle(
    319.0,
    0.0,
    484.0,
    61.0,
    fill="#C1E3D6",
    outline="")
    
    #titr fenêtre
    canvas.create_text(
        341.0,
        7.0,
        anchor="nw",
        text="Point 5",
        fill="#F6FBF9",
        font=("Karla", 36 * -1,"bold")
    )
    
    entry_IP = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    
    entry_IP.place(
        x=38.0,
        y=116.0,
        width=342.0,
        height=53.0
    )

    entry_Mask = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    
    entry_Mask.place(
        x=38.0,
        y=217.0,
        width=342.0,
        height=53.0
    )


    entry_NbSubnet = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    
    entry_NbSubnet.place(
        x=38.0,
        y=312.0,
        width=342.0,
        height=53.0
    )

    
    entry_NbHost = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    
    entry_NbHost.place(
        x=38.0,
        y=409.0,
        width=342.0,
        height=53.0
    )

    button_generer = Button(
        image=image_button_generer_petit,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: genererFive(),
        relief="flat"
    )
    
    button_generer.place(
        x=82.0,
        y=474.0,
        width=255.0,
        height=41.0
    )

    text_results = canvas.create_text(
        448.0,
        235.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Karla Bold", 15 * -1),
        width=300
    )

    button_retour = Button(
        image=image_button_retour,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: displayMenuMain(windowFromMain),
        relief="flat"
    )
    
    button_retour.place(
        x=469.0,
        y=495.0,
        width=255.0,
        height=59
    )

    text_results
    
    def genererFive():

        result = genererPoint5(entry_IP.get(), entry_Mask.get(), entry_NbSubnet.get(), entry_NbHost.get())
        
        #traitement
        if((result == "IpInvalid")):
            messagebox.showerror("ERREUR", "L'adrese IP de la première machine encodée n'est pas valide\nmerci d'en choisir une autre !")
        elif((result == "MaskInvalid")):
            messagebox.showerror("ERREUR", "L'adrese de masque de la première machine encodée n'est pas valide\nmerci d'en choisir une autre !")
        elif((result == "NbSubnetsInvalid")):
            messagebox.showerror("ERREUR", "Le nombre de sous-réseaux n'est pas valide.\nmerci d'encoder une nouvelle valeur !")
        elif((result == "NbHostsInvalid")):
            messagebox.showerror("ERREUR", "Le nombre de machines n'est pas valide.\nmerci d'encoder une nouvelle valeur!")
        else:
            canvas.itemconfigure(text_results,text=f"--------------------------------------------------------\n{result}\n",)
       
def displayAbout():
    print("A propos")

def displayMenuMain(WindowMain):
    
    global windowFromMain
    windowFromMain = WindowMain
    
    #changement titre
    windowFromMain.title("Projet LABO_TCPIP - Menu d'accueil")
    
    global canvas
    canvas = Canvas(
    windowFromMain,
    bg = "#A7D7C5",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    
    canvas.create_rectangle(
    260.0,
    0.0,
    539.0,
    74.0,
    fill="#C1E3D6",
    outline="")
    
    canvas.create_rectangle(
        41.0,
        85.0,
        496.0,
        579.0,
        fill="#F6FBF9",
        outline="")

    canvas.create_text(
    270.0,
    19.0,
    anchor="nw",
    text="Menu principal",
    fill="#F6FBF9",
    font=("Karla", 36 * -1,"bold"),
    )

    canvas.create_rectangle(
        73.0,
        140.0,
        448.0,
        195.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        73.0,
        216.0,
        448.0,
        271.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        73.0,
        292.0,
        448.0,
        347.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        73.0,
        368.0,
        448.0,
        423.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        73.0,
        444.0,
        448.0,
        499.0,
        fill="#FFFFFF",
        outline="")

    button_1 = Button(
        image=image_button_acd1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: displayPoint1(),
        relief="flat"
    )
    button_1.place(
        x=520.0,
        y=136.0,
        width=255.0,
        height=59.0
    )

    button_2 = Button(
        image=image_button_acd2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: displayPoint2(),
        relief="flat"
    )
    button_2.place(
        x=520.0,
        y=214.0,
        width=255.0,
        height=59.0
    )

    button_3 = Button(
        image=image_button_acd3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: displayPoint3(),
        relief="flat"
    )
    button_3.place(
        x=520.0,
        y=290.0,
        width=255.0,
        height=59.0
    )

    button_4 = Button(
        image=image_button_acd4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: displayPoint4(),
        relief="flat"
    )
    button_4.place(
        x=520.0,
        y=366.0,
        width=255.0,
        height=59.0
    )

    button_5 = Button(
        image=image_button_acd5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: displayPoint5(),
        relief="flat"
    )
    button_5.place(
        x=520.0,
        y=444.0,
        width=255.0,
        height=59.0
    )

    button_6 = Button(
        image=image_button_quitter,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: ExitApp(),
        relief="flat"
    )
    button_6.place(
        x=520.0,
        y=520.0,
        width=255.0,
        height=59.0
    )

    canvas.create_text(
        78.0,
        162.0,
        anchor="nw",
        text="Trouver les informations de l’adresse IP",
        fill="#000000",
        font=("Karla Bold", 15 * -1)
    )

    canvas.create_text(
        78.0,
        240.0,
        anchor="nw",
        text="Trouver les informations du réseau ",
        fill="#000000",
        font=("Karla Bold", 15 * -1)
    )

    canvas.create_text(
        78.0,
        316.0,
        anchor="nw",
        text="L’adresse IP appartient-elle au réseau ?",
        fill="#000000",
        font=("Karla Bold", 15 * -1)
    )

    canvas.create_text(
        78.0,
        389.0,
        anchor="nw",
        text="Les adresses IP sont-elles dans le même réseau ?",
        fill="#000000",
        font=("Karla Bold", 15 * -1)
    )

    canvas.create_text(
        78.0,
        467.0,
        anchor="nw",
        text="Déterminer les découpes et le nombre d’hôtes",
        fill="#000000",
        font=("Karla Bold", 15 * -1)
    )
    
    canvas.create_image(
        470.0,
        165.0,
        image=image_fleche
    )


    canvas.create_image(
        470.0,
        243.0,
        image=image_fleche
    )

  
    canvas.create_image(
        470.0,
        319.0,
        image=image_fleche
    )

    canvas.create_image(
        470.0,
        396.0,
        image=image_fleche
    )

    canvas.create_image(
        470.0,
        474.0,
        image=image_fleche
    )
    
    createMenuBar(WindowMain)

#création et configurationd de la menubarre
def createMenuBar(WindowMain):

    menubar = Menu(WindowMain)

    menu1 = Menu(menubar, tearoff=0)
    menu2 = Menu(menubar, tearoff=0)

    menu1.add_command(label="Menu", command=lambda: displayMenuMain(WindowMain))
    
    menu1.add_separator()
    
    menu1.add_command(label="Point 1", command=lambda: displayPoint1())
    menu1.add_command(label="Point 2", command=lambda: displayPoint2())
    menu1.add_command(label="Point 3", command=lambda: displayPoint3())
    menu1.add_command(label="Point 4", command=lambda: displayPoint4())
    menu1.add_command(label="Point 5", command=lambda: displayPoint5())
    
    menu1.add_separator()
    
    menu1.add_command(label="Quitter", command=lambda:ExitApp())
    menubar.add_cascade(label="Menu", menu=menu1)
    
    menu2.add_command(label="Ajout", command=lambda:displayAddUser(WindowMain))
    menu2.add_command(label="Suprresion", command=lambda:DisplayDelete(WindowMain))
    menubar.add_cascade(label="Admin", menu=menu2)

    #ajout de la barre de menu
    WindowMain.config(menu=menubar)

def remove_menubar():
    emptyMenu = Menu(windowFromMain)
    windowFromMain.config(menu=emptyMenu)
 
def ExitApp():
    MsgBox = messagebox.askquestion ('Fermer','Voulez-vous vraiment quitter l\'application?',icon = 'warning')
    if MsgBox == 'yes':
       windowFromMain.destroy()