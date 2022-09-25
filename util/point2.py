import sqlite3

from functions import *

#----------------------------------------------------------------
#récupération des données dans la base de données

connexion = sqlite3.connect("BDDLabo")
cursor = connexion.cursor()
cursor.execute("SELECT * FROM class")
result = cursor.fetchall()

# Demande des informations
ip = input("IP : ")
masque = input("Masque : ")

adresse_masque_valide = False
adresse_ip_valide = False

while not adresse_masque_valide or not adresse_ip_valide:
    # Séparation des octets dans une liste
    liste_octet_ip = ip.split(".")
    liste_octet_masque = masque.split(".")  

    # Vérification adresse ip
    if verifyIsIpValid(ip):
        adresse_ip_valide = True
    else:
        adresse_ip_valide = False

    # Conversion de l'adresse ip de string en int
    if(adresse_ip_valide == True):
        liste_octet_ip_int = []
        for i in liste_octet_ip:
            # Ajout des octets en int dans une nouvelle liste
            liste_octet_ip_int.append(int(i))

    if (adresse_ip_valide == True):
        # Vérification adresse masque_classe
        if verifyIsMaskValid(masque):
            adresse_masque_valide = True
        else:
            adresse_masque_valide = False

        # Conversion du masque de string en int
        if(adresse_masque_valide == True):
            liste_octet_masque_int = []
            for i in liste_octet_masque:
                # Ajout des octets en int dans une nouvelle liste
                liste_octet_masque_int.append(int(i))

        #récupèration du premier octet de l'ip
        firstByte = int(liste_octet_ip_int[0])
        #Recherche de la classe 
        if (firstByte < 127):
            #classe A
            masque_classe_str = result[0][4].split('.')
            print(f'Classe {result[0][1]}: \n{result[0][2]} réseaux de {result[0][3]} machines')
        elif(firstByte < 128):
            #classe reservées
            print(f'Classe {result[5][1]}')
        elif(firstByte < 192):
            #classe B
            masque_classe_str = result[1][4].split('.')
            print(f'Classe {result[1][1]}: \n{result[1][2]} réseaux de {result[1][3]} machines')
        elif(firstByte < 224):
            #classe C
            masque_classe_str = result[2][4].split('.')
            print(f'Classe {result[2][1]}: \n{result[2][2]} réseaux de {result[2][3]} machines')
        elif(firstByte < 240):
            #classe D
            print(f'Classe {result[3][1]}: \n{result[3][2]}')
        else:
            #classe E
            print(f'Classe {result[4][1]}: \n{result[4][2]}')

        # Conversion du masque de classe de string en int
        masque_classe = []
        for i in masque_classe_str:
            masque_classe.append(int(i))

        if(masque_classe > liste_octet_masque_int):
            adresse_masque_valide = False
            print("l'adresse de masque ne peut pas être plus englobant que l'adresse de classe.") #255.255.255.0  255.0.0.0

    # On redemande l'adresse du masque_classe si elle n'est pas valide
    if adresse_masque_valide == False:
        masque = input("Rentrez une adresse de masque valide : ")

    # On redemande l'adresse ip si elle n'est pas valide
    if adresse_ip_valide == False:
        ip = input("Rentrez une adresse ip valide : ")



# Ajout de chaque octet de l'adresse ip en binaire dans une nouvelle liste
liste_binary_ip = []
for i in liste_octet_ip_int:
    liste_binary_ip.append(int_to_binary(i))

# Ajout de chaque octet de l'adresse de masque de classe en binaire dans une nouvelle liste
liste_binary_masque_classe = []
for i in masque_classe:
    liste_binary_masque_classe.append(int_to_binary(i))

# Calcul de l'adresse de reseau et de broadcast
binary_reseau_adresse, binary_broadcast_adresse = calcul_sr_bc(liste_binary_ip,liste_binary_masque_classe)

# Conversion des adresse de réseau et de broadcast en entier
liste_octet_reseau_int = []
liste_octet_broadcast_int = []
for i in range(4):
    liste_octet_reseau_int.append(octet_to_int(binary_reseau_adresse[i]))
    liste_octet_broadcast_int.append(octet_to_int(binary_broadcast_adresse[i]))

# Conversion adresse int en String
ip_reseau = ""
ip_broadcast = ""
for i in range(4):
    ip_reseau += f"{str(liste_octet_reseau_int[i])}."
    ip_broadcast += f"{str(liste_octet_broadcast_int[i])}."
ip_reseau = ip_reseau[:-1]
ip_broadcast = ip_broadcast[:-1]

print("Adresse de réseau : ",ip_reseau)
print("Adresse de broadcast : ",ip_broadcast)

# Calcul de l'adresse de sous-reseau et de broadcast du sous-réseaux s'il y en a
binary_sousreseau_adresse = []
binary_sousreseau_broadcast_adresse = []
if (liste_octet_masque_int != masque_classe):
    # Ajout de chaque octet de l'adresse de masque en binaire dans une nouvelle liste
    liste_binary_masque = [int_to_binary(i) for i in liste_octet_masque_int]
    binary_sousreseau_adresse, binary_sousreseau_broadcast_adresse = calcul_sr_bc(liste_binary_ip,liste_binary_masque)

    # Conversion des adresse de sous-réseau et de broadcast du sous-réseau en entier s'ils existent
    liste_octet_sousreseau_int = []
    liste_octet_sousreseau_broadcast_int = []
    for i in range(4):
        liste_octet_sousreseau_int.append(octet_to_int(binary_sousreseau_adresse[i]))
        liste_octet_sousreseau_broadcast_int.append(octet_to_int(binary_sousreseau_broadcast_adresse[i]))
    # Conversion adresse int en String
    ip_sousreseau = ""
    ip_sousreseau_broadcast = ""
    for i in range(4):
        ip_sousreseau += str(liste_octet_sousreseau_int[i]) + "."
        ip_sousreseau_broadcast += str(liste_octet_sousreseau_broadcast_int[i]) + "."
    ip_sousreseau = ip_sousreseau[:-1]
    ip_sousreseau_broadcast = ip_sousreseau_broadcast[:-1]

    print("Adresse de sous-réseau : ",ip_sousreseau)
    print("Adresse de broadcast du sous-réseau : ",ip_sousreseau_broadcast)

