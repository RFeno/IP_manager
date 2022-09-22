#point 1

#Affichage à l'écran
IpFromUser = input("Veuillez encoder l'adresse IP\n")

#séparation en 
IpListPerByte = IpFromUser.split(".")

#conversion string à int
firstByte = int(IpListPerByte[0])

#Recherche de la classe 
#mettre valeur dans db après
if(firstByte < 127):
    #classe A
    print("Classe A: \n126 réseaux de 16 777 214 machines")
elif(firstByte < 128):
        #classe reservées
    print("Classes réservées")
elif(firstByte < 192):
    #classe B
    print("Classe B :\n16384 réseaux de 65534 machines")
elif(firstByte < 224):
    #classe C
    print("Classe C: \n 2 097 152 réseaux de 254 machines")
elif(firstByte < 240):
    #classe D
    print("Classe D :\nadresses uniques")
else:
    print("Classe E :\nadresses uniques")


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
    



