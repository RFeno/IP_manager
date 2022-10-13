import copy
from util.functions import *

# Vérification des adresses valides ou non
def genererPoint5(IpAdress, maskAdress, numberOfSubNet, numberOfHosts):

    """
    It takes an IP address, a mask, a number of subnets, and a number of hosts, and returns a string
    containing the results of the calculations
    
    :param IpAdress: The IP address of the network
    :param maskAdress: The mask of the network
    :param numberOfSubNet: The number of subnets you want to create
    :param numberOfHosts: The number of hosts you want in each subnet
    :return: a string.
    """
    text = ""

    #vérification des données avant traitement
    if (not verifyIsMaskValid(maskAdress)):
        print("Adresse du masque n'est pas valide.")
        return "MaskInvalid"
    
    if (not verifyIsIpValid(IpAdress)):
        print("Adresse ip n'est pas valide.")
        return "IpInvalid"

    if(not numberOfHosts.isdigit()):
        print("Le nombre de machines n'est pas valide.")
        return "NbHostsInvalid"
    else:
        numberOfHosts = int(numberOfHosts)
        
    if(not numberOfSubNet.isdigit()):
        print("Le nombre de sous-réseaux n'est pas valide.")
        return "NbSubnetsInvalid"
    else:
        numberOfSubNet = int(numberOfSubNet)
    
    if numberOfSubNet < 2:
        print("Le nombre de sous-réseaux n'est pas valide.")
        return "NbSubnetsInvalid"
    
    if numberOfHosts < 1:
        print("Le nombre de machines n'est pas valide.")
        return "NbHostsInvalid"
        
    # Séparation des octets dans une liste
    liste_octet_masque = maskAdress.split(".")  

    # Conversion du masque de string en int
    liste_octet_masque_int = [int(i) for i in liste_octet_masque]

    # Ajout de chaque octet de l'adresse de masque de classe en binaire dans une nouvelle liste
    liste_binary_masque = [int_to_binary(i) for i in liste_octet_masque_int]

    #----------------------------------------------------------------
    # Partie 1
    # Calcul du nombre d'hôte total possible
    nb_of_1 = 0
    for byte in liste_binary_masque:
        for binary in byte:
            if(binary == 1):
                nb_of_1 += 1
    nb_of_zero_in_mask = 32 - nb_of_1
    nb_total_host = (2**nb_of_zero_in_mask)-2

    text += "Le nombre d'hôte total avec l'IP et le masque de départ est de " + str(nb_total_host) + " machines.\n\n"

    #----------------------------------------------------------------
    # Partie 2
    # Possibilié de découpe classique en fonction du nombre de SR

    # Calcul du nombre de bits à réserver à la numérotation des SR
    for i in range(32):
        if(numberOfSubNet <= ((2**i))):
            bit_to_back = i
            break

    print("Le nombre de bit a reculer",bit_to_back)

    # Calcul du nouveau masque pour les SR (Masquage)
    masque_binary_sr = copy.deepcopy(liste_binary_masque)
    for byte in range(4):
        for bit in range(8):
            if(masque_binary_sr[byte][bit] == 0 and bit_to_back != 0):
                masque_binary_sr[byte][bit] = 1
                bit_to_back -= 1

    # Calcul du nombre de 0 dans le masque des sous-réseaux
    nb_of_0 = 0
    for byte in masque_binary_sr:
        for binary in byte:
            if(binary == 0):
                nb_of_0 += 1

    nb_host_per_subnet = ((2**nb_of_0)-2)

    #----------------------------------------------------------------
    # Partie 3
    # Possibilié de découpe classique en fonction du nombre de machines par sous-réseaux

    nb_of_0_to_let = 0
    for i in range(nb_of_zero_in_mask):
        if (numberOfHosts <= (2**(i+1))-2 ):
            nb_of_0_to_let = i+1
            break

    print("nb zero a laisser :",nb_of_0_to_let)

    print("nb zero dans masque :",nb_of_zero_in_mask)

    nb_subnet_max = (2**(nb_of_zero_in_mask-nb_of_0_to_let))

    if(nb_host_per_subnet < numberOfHosts or nb_subnet_max < numberOfSubNet):
        text += "La découpe classique n'est pas possible car :\n\n"
    else:
        text += "La découpe classique est possible car :\n\n"

    if(nb_host_per_subnet > 0):
        text += "Il peut y avoir maximum " + str(nb_host_per_subnet) + " machines par sous-réseaux sur base du nombre de sous-réseaux.\n\n"
    else:
        text += "La découpe classique n'est pas possible sur base du nombre de sous-réseaux.\n\n"
    
    if (nb_subnet_max > 1 and nb_of_0_to_let != 0):
        text += "Il peut y avoir maximum " + str(nb_subnet_max) + " sous-réseaux sur base du nombre d'hôtes par sous-réseaux.\n\n"
    else:
        text += "La découpe classique n'est pas possible sur base du nombre d'hôtes par sous-réseaux.\n\n"

    return text