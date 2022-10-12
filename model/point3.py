from util.functions import *

def genererPoint3(IpAdress, MaskAdress, IpNetworkAdress):
    """
    It takes IP adress, mask adress and network adress, and returns a string that says whether the IP address
    belongs to the network
    
    :param IpAdress: The IP address you want to check
    :param MaskAdress: The mask from IP address
    :param IpNetworkAdress: The IP address of the network you want to check if the IP address belongs to
    :return: The result of the search.
    """

    # verification des données avant traitement
    if(not verifyIsIpValid(IpAdress)):
        print("La première adresse ip n'est pas valide.")
        return "IpInvalid"

    if (not verifyIsMaskValid(MaskAdress)):
        print("Le premier masque n'est pas valide.")
        return "MaskInvalid"

    if (not verifyIsIpValid(IpNetworkAdress)):
        print("La deuxième masque n'est pas valide.")
        return "IpNetworkInvalid"

    if(IpAdress==IpNetworkAdress):
        return "MemeAdress"

    # Séparation des octets dans une liste
    liste_octet_ip = IpAdress.split(".")
    liste_octet_masque = MaskAdress.split(".")
    liste_octet_adresse_reseau_a_appartenir = IpNetworkAdress.split(".")
    
    # Conversion de l'adresse ip de string en int
    liste_octet_ip_int = []
    for i in liste_octet_ip:
        # Ajout des octets en int dans une nouvelle liste
        liste_octet_ip_int.append(int(i))

    # Conversion du masque de string en int
    liste_octet_masque_int = []
    for i in liste_octet_masque:
        # Ajout des octets en int dans une nouvelle liste
        liste_octet_masque_int.append(int(i))

    # Conversion de l'adresse réseau à appartenir de string en int
    liste_octet_reseau_a_appartenir_int = []
    for i in liste_octet_adresse_reseau_a_appartenir:
        # Ajout des octets en int dans une nouvelle liste
        liste_octet_reseau_a_appartenir_int.append(int(i))

    # Ajout de chaque octet de l'adresse ip en binaire dans une nouvelle liste
    liste_binary_ip = [int_to_binary(i) for i in liste_octet_ip_int]
    # Ajout de chaque octet de l'adresse de masque en binaire dans une nouvelle liste
    liste_binary_masque = [int_to_binary(i) for i in liste_octet_masque_int]
    # Calcul de l'adresse de reseau et de broadcast
    binary_reseau_adresse, binary_broadcast_adresse = calcul_reseau_bc(liste_binary_ip,liste_binary_masque)

    # Conversion des adresse de réseau et de broadcast en entier
    liste_octet_reseau_int = [octet_to_int(binary_reseau_adresse[i]) for i in range(4)]

    if(liste_octet_reseau_a_appartenir_int == liste_octet_reseau_int):
        return "L'adresse IP :" + IpAdress + "\nappartient bien au réseau :" + IpNetworkAdress
    else:
        return "L'adresse IP :" + IpAdress + "\nn'appartient pas au réseau :" + IpNetworkAdress