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


    



