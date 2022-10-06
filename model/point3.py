from ipaddress import ip_address
from math import floor

from util.functions import *

#----------------------------------------------------------------
# Demande des informations
# ip = input("IP : ")
# masque = input("Masque : ")
# adresse_reseau_a_appartenir = input("Adresse réseau : ")

def genererPoint3(IpAdress, MaskAdress, IpNetworkAdress):
    
    #vérification que l'adresse réseau est différente de l'adresse IP 
    if(IpAdress==IpNetworkAdress):
        return "MemeAdress"
    
    adresse_masque_valide = False
    adresse_ip_valide = False
    adresse_reseau_a_appartenir_valide = False

    while not adresse_masque_valide or not adresse_ip_valide or not adresse_reseau_a_appartenir_valide:
        # Séparation des octets dans une liste
        liste_octet_ip = IpAdress.split(".")
        liste_octet_masque = MaskAdress.split(".")
        liste_octet_adresse_reseau_a_appartenir = IpNetworkAdress.split(".")
        
        # Vérification adresse ip
        if verifyIsIpValid(IpAdress):
            adresse_ip_valide = True
        else:
            adresse_ip_valide = False

        # Conversion de l'adresse ip de string en int
        if(adresse_ip_valide == True):
            liste_octet_ip_int = []
            for i in liste_octet_ip:
                # Ajout des octets en int dans une nouvelle liste
                liste_octet_ip_int.append(int(i))

        # Vérification adresse masque_classe
        if verifyIsMaskValid(MaskAdress):
            adresse_masque_valide = True
        else:
            adresse_masque_valide = False

        # Conversion du masque de string en int
        if(adresse_masque_valide == True):
            liste_octet_masque_int = []
            for i in liste_octet_masque:
                # Ajout des octets en int dans une nouvelle liste
                liste_octet_masque_int.append(int(i))

        # Vérification adresse réseau à appartenir
        if verifyIsIpValid(IpNetworkAdress):
            adresse_reseau_a_appartenir_valide = True
        else:
            adresse_reseau_a_appartenir_valide = False

        # Conversion de l'adresse réseau à appartenir de string en int
        if(adresse_reseau_a_appartenir_valide == True):
            liste_octet_reseau_a_appartenir_int = []
            for i in liste_octet_adresse_reseau_a_appartenir:
                # Ajout des octets en int dans une nouvelle liste
                liste_octet_reseau_a_appartenir_int.append(int(i))

        # On redemande l'adresse ip si elle n'est pas valide
        if adresse_ip_valide == False:
            print("Adresse ip n'est pas valide.")
            return "IpInvalid"

        # On redemande l'adresse du masque_classe si elle n'est pas valide
        if adresse_masque_valide == False:
            print("Adresse du masque n'est pas valide.")
            return "MaskInvalid"

        # On redemande l'adresse réseau à appartenir si elle n'est pas valide
        if adresse_reseau_a_appartenir_valide == False:
            print("Adresse réseau n'est pas valide.")
            return "IpNetworkInvalid"

    # Ajout de chaque octet de l'adresse ip en binaire dans une nouvelle liste
    liste_binary_ip = [int_to_binary(i) for i in liste_octet_ip_int]
    # Ajout de chaque octet de l'adresse de masque en binaire dans une nouvelle liste
    liste_binary_masque = [int_to_binary(i) for i in liste_octet_masque_int]
    # Calcul de l'adresse de reseau et de broadcast
    binary_reseau_adresse, binary_broadcast_adresse = calcul_reseau_bc(liste_binary_ip,liste_binary_masque)

    # Conversion des adresse de réseau et de broadcast en entier
    liste_octet_reseau_int = [octet_to_int(binary_reseau_adresse[i]) for i in range(4)]

    if(liste_octet_reseau_a_appartenir_int == liste_octet_reseau_int):
        return "L'adresse IP " + IpAdress + " appartient bien au réseau " + IpNetworkAdress
    else:
        return "L'adresse IP " + IpAdress + " n'appartient pas au réseau " + IpNetworkAdress