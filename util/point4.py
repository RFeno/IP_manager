from math import floor
import sqlite3

# Fonction pour transformer un integer en binary
def int_to_binary(nb):
    binary = []
    tmp = nb
    while tmp != 0:
        if (tmp % 2) == 1:
            binary.append(1)
        else:
            binary.append(0)
        tmp = tmp / 2
        tmp = floor(tmp)
    nb_zero = 8 - len(binary)
    binary = list(reversed(binary))
    binary_bis = [0 for _ in range(nb_zero)]
    binary_bis.extend(iter(binary))
    return binary_bis

# Fonction pour convertir un octet en integer
def octet_to_int(tab):
    result = 0
    a = 7
    for i in tab:
        if i == 1:
            result += 2**a
        a-=1
    return result

# Fonction pour calculer le sr et bc en binaire grâce a une ip et le masque_classe en binaire
def calcul_reseau_bc(binary_ip, binary_masque):
    liste_octet_SR_binary = []
    liste_octet_BC_binary = []
    for i in range(4):
        liste_octet_SR_binary.append([])
        liste_octet_BC_binary.append([])
        for j in range(8):
            if binary_masque[i][j] == 1:
                liste_octet_SR_binary[i].append(binary_ip[i][j])
                liste_octet_BC_binary[i].append(binary_ip[i][j])
            else:
                liste_octet_SR_binary[i].append(0)
                liste_octet_BC_binary[i].append(1)
    return (liste_octet_SR_binary,liste_octet_BC_binary)

#----------------------------------------------------------------
# Demande des informations
firstIpAddress = input("Veuillez encoder la première adresse ip: ")
firstNetworkMask = input("Veuillez encoder le masque de réseau de la première adresse ip: ")

secondIpAddress = input("Veuillez encoder la deuxieme adresse ip: ")
secondNetworkMask = input("Veuillez encoder le masque de réseau de la deuxieme adresse ip: ")

adresse_masque1_valide = False
adresse_ip1_valide = False
adresse_masque2_valide = False
adresse_ip2_valide = False

while adresse_masque1_valide == False or adresse_ip2_valide == False or adresse_masque2_valide == False or adresse_ip2_valide == False:
    # Séparation des octets dans une liste
    liste_octet_ip1 = firstIpAddress.split(".")
    liste_octet_masque1 = firstNetworkMask.split(".")
    liste_octet_ip2 = secondIpAddress.split(".")
    liste_octet_masque2 = secondNetworkMask.split(".")   

    # Vérification adresse ip1
    liste_octet_ip1_int = []
    for i in liste_octet_ip1:
        if int(i) in range(0,256):
            # Ajout des octets en int dans une nouvelle liste
            liste_octet_ip1_int.append(int(i))
            adresse_ip1_valide = True
        else:
            adresse_ip1_valide = False
            break

    # Vérification adresse masque1
    liste_octet_masque1_int = []
    for i in liste_octet_masque1:
        if int(i) == 0 or int(i) == 128 or int(i) == 192 or int(i) == 224 or int(i) == 240 or int(i) == 248 or int(i) == 252 or int(i) == 255:
            # Ajout des octets en int dans une nouvelle liste
            liste_octet_masque1_int.append(int(i))
            adresse_masque1_valide = True
        else:
            adresse_masque1_valide = False
            break

    # Vérification adresse ip2
    liste_octet_ip2_int = []
    for i in liste_octet_ip2:
        if int(i) in range(0,256):
            # Ajout des octets en int dans une nouvelle liste
            liste_octet_ip2_int.append(int(i))
            adresse_ip2_valide = True
        else:
            adresse_ip2_valide = False
            break

    # Vérification adresse masque2
    liste_octet_masque2_int = []
    for i in liste_octet_masque2:
        if int(i) == 0 or int(i) == 128 or int(i) == 192 or int(i) == 224 or int(i) == 240 or int(i) == 248 or int(i) == 252 or int(i) == 255:
            # Ajout des octets en int dans une nouvelle liste
            liste_octet_masque2_int.append(int(i))
            adresse_masque2_valide = True
        else:
            adresse_masque2_valide = False
            break

    # On redemande l'adresse du masque_classe si elle n'est pas valide
    if adresse_masque1_valide == False:
        print("Le premier masque n'est pas valide.")
        firstNetworkMask = input("Rentrez une adresse de masque valide : ")

    # On redemande l'adresse ip si elle n'est pas valide
    if adresse_ip1_valide == False:
        print("La première adresse ip n'est pas valide.")
        firstIpAddress = input("Rentrez une adresse ip valide : ")

    # On redemande l'adresse du masque_classe si elle n'est pas valide
    if adresse_masque2_valide == False:
        print("La deuxième masque n'est pas valide.")
        secondNetworkMask = input("Rentrez une adresse de masque valide : ")

    # On redemande l'adresse ip si elle n'est pas valide
    if adresse_ip2_valide == False:
        print("La deuxième adresse ip n'est pas valide.")
        secondIpAddress = input("Rentrez une adresse ip valide : ")

if(liste_octet_masque1_int != liste_octet_masque2_int):
    print("Les 2 machines ne font pas partie du même réseau.")
else:
    # Ajout de chaque octet de l'adresse ip en binaire dans une nouvelle liste
    liste_binary_ip1 = []
    for i in liste_octet_ip1_int:
        liste_binary_ip1.append(int_to_binary(i))

    # Ajout de chaque octet de l'adresse de masque en binaire dans une nouvelle liste
    liste_binary_masque1 = []
    for i in liste_octet_masque1_int:
        liste_binary_masque1.append(int_to_binary(i))

    # Ajout de chaque octet de l'adresse ip en binaire dans une nouvelle liste
    liste_binary_ip2 = []
    for i in liste_octet_ip2_int:
        liste_binary_ip2.append(int_to_binary(i))

    # Ajout de chaque octet de l'adresse de masque en binaire dans une nouvelle liste
    liste_binary_masque2 = []
    for i in liste_octet_masque2_int:
        liste_binary_masque2.append(int_to_binary(i))
    
    # Calcul de l'adresse de reseau et de broadcast
    binary_reseau1_adresse, binary_broadcast1_adresse = calcul_reseau_bc(liste_binary_ip1,liste_binary_masque1)

    # Calcul de l'adresse de reseau et de broadcast
    binary_reseau2_adresse, binary_broadcast2_adresse = calcul_reseau_bc(liste_binary_ip2,liste_binary_masque2)

    # Conversion des adresse de réseau et de broadcast en entier
    liste_octet_reseau1_int = []
    liste_octet_broadcast1_int = []
    liste_octet_reseau2_int = []
    liste_octet_broadcast2_int = []
    for i in range(4):
        liste_octet_reseau1_int.append(octet_to_int(binary_reseau1_adresse[i]))
        liste_octet_broadcast1_int.append(octet_to_int(binary_broadcast1_adresse[i]))
        liste_octet_reseau2_int.append(octet_to_int(binary_reseau2_adresse[i]))
        liste_octet_broadcast2_int.append(octet_to_int(binary_broadcast2_adresse[i]))

    if(liste_octet_reseau1_int == liste_octet_reseau2_int and liste_octet_broadcast1_int == liste_octet_broadcast2_int):
        print("Les 2 machines sont dans le même réseau.")
    else:
        print("Les 2 machines ne font pas partie du même réseau.")









