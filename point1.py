#point 1

#imports
import sqlite3

#récupération des données dans la base de données
connexion = sqlite3.connect("BDDLabo")
cursor = connexion.cursor()
cursor.execute("SELECT * FROM class")
result = cursor.fetchall()


#Affichage à l'écran
IpFromUser = input("Veuillez encoder l'adresse IP\n")

#séparation en 
IpListPerByte = IpFromUser.split(".")

#conversion string à int
firstByte = int(IpListPerByte[0])

#Recherche de la classe 
#mettre valeur dans db après
if (firstByte < 127):
    #classe A
    print(f'Classe {result[0][1]}: \n{result[0][2]} réseaux de {result[0][3]} machines')
elif(firstByte < 128):
        #classe reservées
    print("Classes réservées")
elif(firstByte < 192):
    #classe B
     print(f'Classe {result[1][1]}: \n{result[1][2]} réseaux de {result[1][3]} machines')
elif(firstByte < 224):
    #classe C
     print(f'Classe {result[2][1]}: \n{result[2][2]} réseaux de {result[2][3]} machines')
elif(firstByte < 240):
    #classe D
    print("Classe D :\nadresses uniques")
else:
    print("Classe E :\nadresses uniques")

#A SUPPRIMER SI PAS UTILE
#point 1 automatique
"""from ipaddress import IPv4Address, IPv4Network


classA = IPv4Network(("10.0.0.0", "255.0.0.0"))  # or IPv4Network("10.0.0.0/8")
classB = IPv4Network(("172.16.0.0", "255.240.0.0"))  # or IPv4Network("172.16.0.0/12")
classC = IPv4Network(("192.168.0.0", "255.255.0.0"))  # or IPv4Network("192.168.0.0/16")
classD = IPv4Network(("192.168.0.0", "255.255.0.0"))  # or IPv4Network("192.168.0.0/16")
classE = IPv4Network(("192.168.0.0", "255.255.0.0"))  # or IPv4Network("192.168.0.0/16")
classReserved = IPv4Network(("192.168.0.0", "255.255.0.0"))  # or IPv4Network("192.168.0.0/16")


ip1 = IPv4Address("126.255.255.225")
ip2 = IPv4Address("172.18.76.25")
ip3 = IPv4Address("192.168.45.62")

print(ip1 in classA)  # True
print(ip2 in classA)  # False
print(ip3 in classA)  # False

print(ip1 in classB)  # False
print(ip2 in classB)  # True
print(ip3 in classB)  # False

print(ip1 in classC)  # False
print(ip2 in classC)  # False
print(ip3 in classC)  # True
"""
    



