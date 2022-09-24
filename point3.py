from math import floor

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
def calcul_reseau_bc(binary_ip, binary_masque):
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
# Demande des informations
ip = input("IP : ")
masque = input("Masque : ")
adresse_reseau_a_appartenir = input("Adresse réseau : ")

adresse_masque_valide = False
adresse_ip_valide = False
adresse_reseau_a_appartenir_valide = False

while adresse_masque_valide == False or adresse_ip_valide == False or adresse_reseau_a_appartenir_valide == False:
    # Séparation des octets dans une liste
    liste_octet_ip = ip.split(".")
    liste_octet_masque = masque.split(".")  
    liste_octet_adresse_reseau_a_appartenir = adresse_reseau_a_appartenir.split(".")

    # Vérification adresse masque
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
    
    # Vérification adresse réseau à appartenir
    liste_octet_adresse_reseau_a_appartenir_int = []
    for i in liste_octet_adresse_reseau_a_appartenir:
        if int(i) in range(0,256):
            # Ajout des octets en int dans une nouvelle liste
            liste_octet_adresse_reseau_a_appartenir_int.append(int(i))
            adresse_reseau_a_appartenir_valide = True
        else:
            adresse_reseau_a_appartenir_valide = False
            break

    # On redemande l'adresse du masque_classe si elle n'est pas valide
    if adresse_masque_valide == False:
        print("Adresse du masque n'est pas valide.")
        masque = input("Rentrez une adresse de masque valide : ")

    # On redemande l'adresse ip si elle n'est pas valide
    if adresse_ip_valide == False:
        print("Adresse ip n'est pas valide.")
        ip = input("Rentrez une adresse ip valide : ")

    # On redemande l'adresse réseau à appartenir si elle n'est pas valide
    if adresse_reseau_a_appartenir_valide == False:
        print("Adresse réseau n'est pas valide.")
        ip = input("Rentrez une adresse réseau valide : ")

# Ajout de chaque octet de l'adresse ip en binaire dans une nouvelle liste
liste_binary_ip = []
for i in liste_octet_ip_int:
    liste_binary_ip.append(int_to_binary(i))

# Ajout de chaque octet de l'adresse de masque en binaire dans une nouvelle liste
liste_binary_masque = []
for i in liste_octet_masque_int:
    liste_binary_masque.append(int_to_binary(i))

# Calcul de l'adresse de reseau et de broadcast
binary_reseau_adresse, binary_broadcast_adresse = calcul_reseau_bc(liste_binary_ip,liste_binary_masque)

# Conversion des adresse de réseau et de broadcast en entier
liste_octet_reseau_int = []
for i in range(4):
    liste_octet_reseau_int.append(octet_to_int(binary_reseau_adresse[i]))

if(liste_octet_adresse_reseau_a_appartenir_int == liste_octet_reseau_int):
    print("L'adresse IP ", liste_octet_ip_int," appartient bien au réseau ",liste_octet_adresse_reseau_a_appartenir_int)
else:
    print("L'adresse IP ", liste_octet_ip_int," n'appartient pas au réseau ",liste_octet_adresse_reseau_a_appartenir_int)