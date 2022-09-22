#point 1

#Affichage à l'écran
IpFromUser = input("Veuillez encoder l'adresse IP\n")

(IpListPerByte) = IpFromUser.split(".")

print(IpListPerByte)

#conversion string à int
fisrtOctet = int(IpListPerByte[0])

#Recherche de la classe 
#mettre valeur dans db après
if(fisrtOctet < 127):
    #classe A
    print("classe A: \n126 réseaux de 16 777 214 machines")
elif(fisrtOctet < 128):
        #classe reservées
    print("Classes réservées")
elif(fisrtOctet < 192):
    #classe B
    print("classe B :\n16384 réseaux de 65534 machines")
elif(fisrtOctet < 224):
    #classe C
    print("classe C: \n 2 097 152 réseaux de 254 machines")
elif(fisrtOctet < 240):
    #classe D
    print("classe D :\nadresses uniques")
else:
    print("classe E :\nadresses uniques")


    



