
from math import floor
import re
from pathlib import Path

# Fonction pour vérifier si une adresse IP est valide ou non
def verifyIsIpValid(adressIP):
    if not re.search(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", adressIP):
       print(f"L'adresse IP {adressIP} n'est pas valide")
       return False

    bytes = adressIP.split(".")
  
    for ip_byte in bytes:
        if int(ip_byte) < 0 or int(ip_byte) > 255:
            print(f"L'adresse IP {adressIP} n'est pas valide")
            return False
    print(f"L'adresse de IP {adressIP} est valide")
    return True
    
# Fonction pour vérifier si un masque est valide ou non
def verifyIsMaskValid(mask):
    if not re.search(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", mask):
       print(f"L'adresse de masque {mask} n'est pas valide")
       return False

    bytes = mask.split(".")
  
    for ip_byte in bytes:
        if int(ip_byte) not in {0, 128, 192, 224, 240, 248, 252, 255}:
            print(f"L'adresse de masque {mask} n'est pas valide")
            return False

    for i in range(1,4): 
        if(int(bytes[i]) != 0 and int(bytes[i-1]) != 255):
            print(f"L'adresse de masque {mask} n'est pas valide")
            return False
        
    if(int(bytes[3]) == 255):
        print(f"L'adresse de masque {mask} n'est pas valide")
        return False

    print(f"L'adresse de masque {mask} est valide")
    return True

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

#a supprimer
"""ASSETS_PATH = Path("ressources/images/viewsIMG")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)"""