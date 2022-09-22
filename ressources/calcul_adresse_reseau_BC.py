from math import floor

ip = input("IP : ")
masque = input("Masque : ")

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

# Vérification des adresses valides ou non
test = False
while test == False:
    # Séparation des octets dans une liste
    liste_octet_ip = ip.split(".")
    liste_octet_masque = masque.split(".")  

    # Vérification adresse masque
    adresse_masque_non_valide = True
    liste_octet_masque_int = []
    for i in liste_octet_masque:
        if int(i) == 0 or int(i) == 128 or int(i) == 192 or int(i) == 224 or int(i) == 240 or int(i) == 248 or int(i) == 254 or int(i) == 255:
            # Ajout des octets en int dans une nouvelle liste
            liste_octet_masque_int.append(int(i))
        else:
            adresse_masque_non_valide = False

    # Vérification adresse ip
    adresse_ip_non_valide = True
    liste_octet_ip_int = []
    for i in liste_octet_ip:
        if int(i) in range(0,256):
            # Ajout des octets en int dans une nouvelle liste
            liste_octet_ip_int.append(int(i))
        else:
            adresse_ip_non_valide = False

    # On redemande l'adresse du masque si elle n'est pas valide
    if adresse_masque_non_valide == False:
        print("Adresse du masque n'est pas valide.")
        masque = input("Rentrez une adresse de masque valide : ")

    # On redemande l'adresse ip si elle n'est pas valide
    if adresse_ip_non_valide == False:
        print("Adresse ip n'est pas valide.")
        ip = input("Rentrez une adresse ip valide : ")

    if adresse_ip_non_valide == True and adresse_masque_non_valide == True:
        test = True
        
# Ajout de chaque octet de l'adresse ip en binaire dans une nouvelle liste
liste_binary_ip = []
for i in liste_octet_ip_int:
    liste_binary_ip.append(int_to_binary(i))

# Ajout de chaque octet de l'adresse de masque en binaire dans une nouvelle liste
liste_binary_masque = []
for i in liste_octet_masque_int:
    liste_binary_masque.append(int_to_binary(i))

# Calcul de l'adresse de SR et BC en binaire
liste_octet_SR_binary = []
liste_octet_BC_binary = []
for i in range(0,len(liste_binary_masque)):
    liste_octet_SR_binary.append([])
    liste_octet_BC_binary.append([])
    for j in range(0,len(liste_binary_masque[i])):
        if liste_binary_masque[i][j] == 1:
            liste_octet_SR_binary[i].append(liste_binary_ip[i][j])
            liste_octet_BC_binary[i].append(liste_binary_ip[i][j])
        else:
            liste_octet_SR_binary[i].append(0)
            liste_octet_BC_binary[i].append(1)

# Conversion des adresse de SR et BC en entier
liste_octet_SR_int = []
liste_octet_BC_int = []
for i in range(4):
    liste_octet_SR_int.append(octet_to_int(liste_octet_SR_binary[i]))
    liste_octet_BC_int.append(octet_to_int(liste_octet_BC_binary[i]))

# Conversion adresse int en String
ip_BC = ""
ip_SR = ""
for i in range(4):
    ip_SR += str(liste_octet_SR_int[i]) + "."
    ip_BC += str(liste_octet_BC_int[i]) + "."
ip_SR = ip_SR[:-1]
ip_BC = ip_BC[:-1]
print("SR : ",ip_SR)
print("BC : ",ip_BC)
