from util.functions import *

#----------------------------------------------------------------

def genererPoint4(IpAdress, MaskAdress, IpAdress2, MaskAdress2):
    
    # verification des données avant traitement
    if (not verifyIsMaskValid(MaskAdress)):
        print("Le premier masque n'est pas valide.")
        return "MaskInvalid1"

    if(not verifyIsIpValid(IpAdress)):
        print("La première adresse ip n'est pas valide.")
        return "IpInvalid1"

    if (not verifyIsMaskValid(MaskAdress2)):
        print("La deuxième masque n'est pas valide.")
        return "MaskInvalid2"

    if (not verifyIsIpValid(IpAdress2)):
        print("La deuxième adresse ip n'est pas valide.")
        return "IpInvalid2"
    
    # Séparation des octets dans une liste
    liste_octet_ip1 = IpAdress.split(".")
    liste_octet_masque1 = MaskAdress.split(".")
    liste_octet_ip2 = IpAdress2.split(".")
    liste_octet_masque2 = MaskAdress2.split(".")   

    # Conversion de l'adresse ip1 de string en int
    liste_octet_ip1_int = []
    for i in liste_octet_ip1:
        # Ajout des octets en int dans une nouvelle liste
        liste_octet_ip1_int.append(int(i))

    # Conversion du masque de string en int
    liste_octet_masque1_int = []
    for i in liste_octet_masque1:
        # Ajout des octets en int dans une nouvelle liste
        liste_octet_masque1_int.append(int(i))

    # Conversion de l'adresse ip1 de string en int
    liste_octet_ip2_int = []
    for i in liste_octet_ip2:
        # Ajout des octets en int dans une nouvelle liste
        liste_octet_ip2_int.append(int(i))

    # Conversion du masque de string en int
    liste_octet_masque2_int = []
    for i in liste_octet_masque2:
        # Ajout des octets en int dans une nouvelle liste
        liste_octet_masque2_int.append(int(i))

    #-------------------------------------------------------------------------------------

    # Ajout de chaque octet de l'adresse ip en binaire dans une nouvelle liste
    liste_binary_ip1 = [int_to_binary(i) for i in liste_octet_ip1_int]
    # Ajout de chaque octet de l'adresse de masque en binaire dans une nouvelle liste
    liste_binary_masque1 = [int_to_binary(i) for i in liste_octet_masque1_int]
    # Ajout de chaque octet de l'adresse ip en binaire dans une nouvelle liste
    liste_binary_ip2 = [int_to_binary(i) for i in liste_octet_ip2_int]
    # Ajout de chaque octet de l'adresse de masque en binaire dans une nouvelle liste
    liste_binary_masque2 = [int_to_binary(i) for i in liste_octet_masque2_int]
    
    # Calcul de l'adresse de reseau 1 et de broadcast 1
    binary_reseau1_adresse, binary_broadcast1_adresse = calcul_reseau_bc(liste_binary_ip1,liste_binary_masque1)

    # Calcul de l'adresse de reseau 2 et de broadcast 2
    binary_reseau2_adresse, binary_broadcast2_adresse = calcul_reseau_bc(liste_binary_ip2,liste_binary_masque2)


    # Calcul de l'adresse de reseau 1bis et de broadcast 1bis avec le masque 2
    text = ""
    binary_reseau1bis_adresse, binary_broadcast1bis_adresse = calcul_reseau_bc(liste_binary_ip1,liste_binary_masque2)
    if(binary_reseau1bis_adresse == binary_reseau2_adresse and binary_broadcast1bis_adresse == binary_broadcast2_adresse):
        text += "\nLa machine 2 considère la machine 1 dans son réseau.\n\n"
    else:
        text += "\nLa machine 2 ne considère pas la machine 1 dans son réseau.\n\n"


    # Calcul de l'adresse de reseau 2bis et de broadcast 2bis avec le masque 1
    binary_reseau2bis_adresse, binary_broadcast2bis_adresse = calcul_reseau_bc(liste_binary_ip2,liste_binary_masque1)
    if(binary_reseau2bis_adresse == binary_reseau1_adresse and binary_broadcast2bis_adresse == binary_broadcast1_adresse):
        text += "La machine 1 considère la machine 2 dans son réseau.\n"
    else:
        text += "La machine 1 ne considère pas la machine 2 dans son réseau.\n"

    return text