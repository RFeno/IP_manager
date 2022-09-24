#récupération des données
numberOfSubNet = int(input("Veuillez encoder le nombre de sous réseaux : \n"))
numberOfHosts = int(input("Veuillez encoder le nombre de mahcines : \n"))
IpAdress = input("Veuillez encoder l'adresse IP: \n")
maskAdress = input("Veuillez encoder le masque de l'IP : \n")

#vérifier que le système fonctionne bien

# Vérification des adresses valides ou non
test = False
while not test:
    # Séparation des octets dans une liste
    liste_octet_ip = IpAdress.split(".")
    liste_octet_masque = maskAdress.split(".")  

    # Vérification adresse masque
    adresse_masque_non_valide = True
    liste_octet_masque_int = []
    for i in liste_octet_masque:
        if int(i) in {0, 128, 192, 224, 240, 248, 254, 255}:
            # Ajout des octets en int dans une nouvelle liste
            liste_octet_masque_int.append(int(i))
        else:
            adresse_masque_non_valide = False

    # Vérification adresse ip
    adresse_ip_non_valide = True
    liste_octet_ip_int = []
    for i in liste_octet_ip:
        if int(i) in range(256):
            # Ajout des octets en int dans une nouvelle liste
            liste_octet_ip_int.append(int(i))
        else:
            adresse_ip_non_valide = False

    # On redemande l'adresse du masque si elle n'est pas valide
    if adresse_masque_non_valide == False:
        print("Adresse du masque n'est pas valide.")
        maskAdress = input("Rentrez une adresse de masque valide : ")

    # On redemande l'adresse ip si elle n'est pas valide
    if adresse_ip_non_valide == False:
        print("Adresse ip n'est pas valide.")
        IpAdress = input("Rentrez une adresse ip valide : ")

    if adresse_ip_non_valide == True and adresse_masque_non_valide == True:
        test = True