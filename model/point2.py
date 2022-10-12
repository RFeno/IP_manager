import sqlite3
from unittest import result

from util.functions import calcul_reseau_bc, int_to_binary, octet_to_int, verifyIsIpValid, verifyIsMaskValid

# TODO Rename this  
def _extracted_from_genererPointInformations2_98(arg0, liste_binary_ip, titre, titrevar):
    
    resultGeneration = ""
        # Ajout de chaque octet de l'adresse de masque en binaire dans une nouvelle liste
    liste_binary_masque = [int_to_binary(i) for i in arg0]
    binary_sousreseau_adresse, binary_sousreseau_broadcast_adresse = calcul_reseau_bc(liste_binary_ip,liste_binary_masque)

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
        ip_sousreseau += f"{str(liste_octet_sousreseau_int[i])}."
        ip_sousreseau_broadcast += f"{str(liste_octet_sousreseau_broadcast_int[i])}."
    ip_sousreseau = ip_sousreseau[:-1]
    ip_sousreseau_broadcast = ip_sousreseau_broadcast[:-1]

    print(titre, ip_sousreseau)
    
    resultGeneration+=titre+ip_sousreseau+"\n"
    
    print(titrevar, ip_sousreseau_broadcast)
    
    resultGeneration+=titrevar+ip_sousreseau_broadcast+"\n"
    
    return resultGeneration

def genererPoint2(ip,masque):
    
    #utilitaires
    resultGeneration = ""
    adresse_masque_valide = False
    adresse_ip_valide = False
    
    #récupération des données dans la base de données
    connexion = sqlite3.connect("BDDLabo")
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM class")
    result = cursor.fetchall()

    # Séparation des octets dans une liste
    liste_octet_ip = ip.split(".")
    liste_octet_masque = masque.split(".")  

    # Vérification adresse ip
    adresse_ip_valide = bool(verifyIsIpValid(ip))
    
    if adresse_ip_valide:
        liste_octet_ip_int = [int(i) for i in liste_octet_ip]
        # Vérification adresse masque_classe
        adresse_masque_valide = bool(verifyIsMaskValid(masque))
        
    
        # Conversion du masque de string en int
        if adresse_masque_valide:
            liste_octet_masque_int = [int(i) for i in liste_octet_masque]
        #récupèration du premier octet de l'ip
        firstByte = int(liste_octet_ip_int[0])

        #Recherche de la classe 
        if(firstByte == 0):
            #classe reservées (A)
            print(f'Classe {result[5][1]}')
            return 'On ne peut pas utiliser cette adresse IP \ncar elle fait partie des adresses réservés'
        elif(firstByte < 127):
            #classe A
            masque_classe_str = result[0][4].split('.')
            print(f'Classe {result[0][1]}: \n\n{result[0][2]} réseaux de {result[0][3]} machines')
        elif(firstByte < 128):
            #classe reservées (A)
            print(f'Classe {result[5][1]}')
            'On ne peut pas utiliser cette adresse IP \ncar elle fait partie des adresses réservés'
        elif(firstByte < 192):
            #classe B
            masque_classe_str = result[1][4].split('.')
            print(f'Classe {result[1][1]}: \n\n{result[1][2]} réseaux de {result[1][3]} machines')
        elif(firstByte < 224):
            #classe C
            masque_classe_str = result[2][4].split('.')
            print(f'Classe {result[2][1]}: \n\n{result[2][2]} réseaux de {result[2][3]} machines')
        elif(firstByte < 240):
            #classe D
            print(f'Classe {result[3][1]}: \n\n{result[3][2]}')
            return 'On ne peut pas utiliser cette adresse IP \ncar elle fait partie de la classe D'
        else:
            #classe E
            print(f'Classe {result[4][1]}: \n\n{result[4][2]}')
            return 'On ne peut pas utiliser cette adresse IP \ncar elle fait partie de la classe E'

        # Conversion du masque de classe de string en int
        masque_classe = [int(i) for i in masque_classe_str]
        
        if not adresse_masque_valide:
            print(f"l'adresse de masque {masque} n'est pas valide")
            return "MaskInvalid"
        
        #erreur msg box
        if(masque_classe > liste_octet_masque_int):
            print("l'adresse de masque ne peut pas être plus englobante \n que l'adresse de classe.") 
            return "MaskInvalidGlobal"
        
    #
    if not adresse_ip_valide:
        print(f"l'adresse ip {ip} n'est pas valide")
        return "IpInvalid"

    #
    if not adresse_masque_valide:
        print(f"l'adresse de masque {masque} n'est pas valide")
        return "MaskInvalid"


    # Ajout de chaque octet de l'adresse ip en binaire dans une nouvelle liste
    liste_binary_ip = [int_to_binary(i) for i in liste_octet_ip_int]
    resultGeneration+= _extracted_from_genererPointInformations2_98(masque_classe, liste_binary_ip, "Adresse de réseau : ", "Adresse de broadcast : ")

    
    # TODO : effacer si pas besoin 
    """binary_sousreseau_adresse = []
    binary_sousreseau_broadcast_adresse = []"""
    # Calcul de l'adresse de sous-reseau et de broadcast du sous-réseaux s'il y en a
    if (liste_octet_masque_int != masque_classe):
        resultGeneration+= _extracted_from_genererPointInformations2_98(liste_octet_masque_int, liste_binary_ip, "Adresse de sous-réseau : ", "Adresse de broadcast du sous-réseau : \n")
    
    
    return resultGeneration



