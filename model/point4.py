from util.functions import *

#----------------------------------------------------------------
# Demande des informations
# firstIpAddress = input("Veuillez encoder la première adresse ip: ")
# firstNetworkMask = input("Veuillez encoder le masque de réseau de la première adresse ip: ")

# secondIpAddress = input("Veuillez encoder la deuxieme adresse ip: ")
# secondNetworkMask = input("Veuillez encoder le masque de réseau de la deuxieme adresse ip: ")

def genererPoint4(IpAdress, MaskAdress, IpAdress2, MaskAdress2):
    adresse_masque1_valide = False
    adresse_ip1_valide = False
    adresse_masque2_valide = False
    adresse_ip2_valide = False

    while not adresse_masque1_valide or not adresse_ip2_valide or not adresse_masque2_valide or not adresse_ip2_valide:
        # Séparation des octets dans une liste
        liste_octet_ip1 = IpAdress.split(".")
        liste_octet_masque1 = MaskAdress.split(".")
        liste_octet_ip2 = IpAdress2.split(".")
        liste_octet_masque2 = MaskAdress2.split(".")   

        # Vérification adresse ip1
        if verifyIsIpValid(IpAdress):
            adresse_ip1_valide = True
        else:
            adresse_ip1_valide = False

        # Conversion de l'adresse ip1 de string en int
        if(adresse_ip1_valide == True):
            liste_octet_ip1_int = []
            for i in liste_octet_ip1:
                # Ajout des octets en int dans une nouvelle liste
                liste_octet_ip1_int.append(int(i))

        # Vérification adresse masque1
        if verifyIsMaskValid(MaskAdress):
            adresse_masque1_valide = True
        else:
            adresse_masque1_valide = False

        # Conversion du masque de string en int
        if(adresse_masque1_valide == True):
            liste_octet_masque1_int = []
            for i in liste_octet_masque1:
                # Ajout des octets en int dans une nouvelle liste
                liste_octet_masque1_int.append(int(i))

        # Vérification adresse ip2
        liste_octet_ip2_int = []
        for i in liste_octet_ip2:
            if int(i) in range(256):
                # Ajout des octets en int dans une nouvelle liste
                liste_octet_ip2_int.append(int(i))
                adresse_ip2_valide = True
            else:
                adresse_ip2_valide = False
                break

        # Vérification adresse ip2
        if verifyIsIpValid(IpAdress2):
            adresse_ip2_valide = True
        else:
            adresse_ip2_valide = False

        # Conversion de l'adresse ip1 de string en int
        if(adresse_ip2_valide == True):
            liste_octet_ip2_int = []
            for i in liste_octet_ip2:
                # Ajout des octets en int dans une nouvelle liste
                liste_octet_ip2_int.append(int(i))

        # Vérification adresse masque2
        liste_octet_masque2_int = []
        for i in liste_octet_masque2:
            if int(i) in {0, 128, 192, 224, 240, 248, 252, 255}:
                # Ajout des octets en int dans une nouvelle liste
                liste_octet_masque2_int.append(int(i))
                adresse_masque2_valide = True
            else:
                adresse_masque2_valide = False
                break

        # Vérification adresse masque1
        if verifyIsMaskValid(MaskAdress2):
            adresse_masque2_valide = True
        else:
            adresse_masque2_valide = False

        # Conversion du masque de string en int
        if(adresse_masque2_valide == True):
            liste_octet_masque2_int = []
            for i in liste_octet_masque2:
                # Ajout des octets en int dans une nouvelle liste
                liste_octet_masque2_int.append(int(i))

        # On redemande l'adresse du masque_classe si elle n'est pas valide
        if adresse_masque1_valide == False:
            print("Le premier masque n'est pas valide.")
            return "MaskInvalid1"

        # On redemande l'adresse ip si elle n'est pas valide
        if adresse_ip1_valide == False:
            print("La première adresse ip n'est pas valide.")
            return "IpInvalid1"

        # On redemande l'adresse du masque_classe si elle n'est pas valide
        if adresse_masque2_valide == False:
            print("La deuxième masque n'est pas valide.")
            return "MaskInvalid2"

        # On redemande l'adresse ip si elle n'est pas valide
        if adresse_ip2_valide == False:
            print("La deuxième adresse ip n'est pas valide.")
            return "IpInvalid2"

    if (liste_octet_masque1_int != liste_octet_masque2_int):
        return "Les 2 machines ne font pas partie du même réseau."
    else:
        # Ajout de chaque octet de l'adresse ip en binaire dans une nouvelle liste
        liste_binary_ip1 = [int_to_binary(i) for i in liste_octet_ip1_int]
        # Ajout de chaque octet de l'adresse de masque en binaire dans une nouvelle liste
        liste_binary_masque1 = [int_to_binary(i) for i in liste_octet_masque1_int]
        # Ajout de chaque octet de l'adresse ip en binaire dans une nouvelle liste
        liste_binary_ip2 = [int_to_binary(i) for i in liste_octet_ip2_int]
        # Ajout de chaque octet de l'adresse de masque en binaire dans une nouvelle liste
        liste_binary_masque2 = [int_to_binary(i) for i in liste_octet_masque2_int]
        
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
            return "Les 2 machines sont dans le même réseau."
        else:
            return "Les 2 machines ne font pas partie du même réseau."









