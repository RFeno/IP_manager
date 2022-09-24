from math import floor
from queue import Empty
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
    binary_bis = []
    for i in range(nb_zero):
        binary_bis.append(0)
    for i in  binary:
        binary_bis.append(i)
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
def calcul_sr_bc(binary_ip, binary_masque):
    liste_octet_SR_binary = []
    liste_octet_BC_binary = []
    for i in range(0,4):
        liste_octet_SR_binary.append([])
        liste_octet_BC_binary.append([])
        for j in range(0,8):
            if binary_masque[i][j] == 1:
                liste_octet_SR_binary[i].append(binary_ip[i][j])
                liste_octet_BC_binary[i].append(binary_ip[i][j])
            else:
                liste_octet_SR_binary[i].append(0)
                liste_octet_BC_binary[i].append(1)
    return (liste_octet_SR_binary,liste_octet_BC_binary)

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

while adresse_masque_valide == False or adresse_ip_valide == False:
    # Séparation des octets dans une liste
    liste_octet_ip = ip.split(".")
    liste_octet_masque = masque.split(".")  

    # Vérification adresse masque_classe
    liste_octet_masque_int = []
    for i in liste_octet_masque:
        if int(i) == 0 or int(i) == 128 or int(i) == 192 or int(i) == 224 or int(i) == 240 or int(i) == 248 or int(i) == 252 or int(i) == 255:
            # Ajout des octets en int dans une nouvelle liste
            liste_octet_masque_int.append(int(i))
            adresse_masque_valide = True
        else:
            adresse_masque_valide = False
            break

    # Vérification adresse ip
    liste_octet_ip_int = []
    for i in liste_octet_ip:
        if int(i) in range(0,256):
            # Ajout des octets en int dans une nouvelle liste
            liste_octet_ip_int.append(int(i))
            adresse_ip_valide = True
        else:
            adresse_ip_valide = False
            break

    # On redemande l'adresse du masque_classe si elle n'est pas valide
    if adresse_masque_valide == False:
        print("Adresse du masque n'est pas valide.")
        masque = input("Rentrez une adresse de masque valide : ")

    # On redemande l'adresse ip si elle n'est pas valide
    if adresse_ip_valide == False:
        print("Adresse ip n'est pas valide.")
        ip = input("Rentrez une adresse ip valide : ")

#récupèration du premier octet de l'ip
firstByte = int(liste_octet_ip_int[0])

#Recherche de la classe 
if (firstByte < 127):
    #classe A
    masque_classe = [255,0,0,0]
    print(f'Classe {result[0][1]}: \n{result[0][2]} réseaux de {result[0][3]} machines')
elif(firstByte < 128):
        #classe reservées
    print("Classes réservées")
elif(firstByte < 192):
    #classe B
    masque_classe = [255,255,0,0]
    print(f'Classe {result[1][1]}: \n{result[1][2]} réseaux de {result[1][3]} machines')
elif(firstByte < 224):
    #classe C
    masque_classe = [255,255,255,0]
    print(f'Classe {result[2][1]}: \n{result[2][2]} réseaux de {result[2][3]} machines')
elif(firstByte < 240):
    #classe D
    print("Classe D :\nadresses uniques")
else:
    print("Classe E :\nadresses uniques")

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
    ip_reseau += str(liste_octet_reseau_int[i]) + "."
    ip_broadcast += str(liste_octet_broadcast_int[i]) + "."
ip_reseau = ip_reseau[:-1]
ip_broadcast = ip_broadcast[:-1]

print("Adresse de réseau : ",ip_reseau)
print("Adresse de broadcast : ",ip_broadcast)

# Calcul de l'adresse de sous-reseau et de broadcast du sous-réseaux s'il y en a
binary_sousreseau_adresse = []
binary_sousreseau_broadcast_adresse = []
if(liste_octet_masque_int != masque_classe):
    # Ajout de chaque octet de l'adresse de masque en binaire dans une nouvelle liste
    liste_binary_masque = []
    for i in liste_octet_masque_int:
        liste_binary_masque.append(int_to_binary(i))
        
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

