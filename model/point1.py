from util.functions import verifyIsIpValid
from util.db import findClassesInfo

#récupération des données dans la base de données
def genererPoint1(adresseIP):
    """
    It takes an IP address as a string, and returns a string that describes the class of the IP address
    
    :param adresseIP: the IP address to be analyzed
    :return: a string 
    """
    
    if not (verifyIsIpValid(adresseIP)):
        return "IpInvalid"

    result = findClassesInfo()
    
    #séparation en 
    IpListPerByte = adresseIP.split(".")

    #conversion string à int
    firstByte = int(IpListPerByte[0])

    #Recherche de la classe et retour à la vue
    if(firstByte == 0):
        #classe reservées (A)
        return (f'Classe {result[5][1]}')
    elif(firstByte < 127):
        #classe A
        return (f'Classe {result[0][1]}: \n\n{result[0][2]} réseaux de {result[0][3]} machines')
    elif(firstByte < 128):
        #classe reservées (A)
        return (f'Classe {result[5][1]}')
    elif(firstByte < 192):
        #classe B
        return (f'Classe {result[1][1]}: \n\n{result[1][2]} réseaux de {result[1][3]} machines')
    elif(firstByte < 224):
        #classe C
        return (f'Classe {result[2][1]}: \n\n{result[2][2]} réseaux de {result[2][3]} machines')
    elif(firstByte < 240):
        #classe D
        return (f'Classe {result[3][1]}: \n\n{result[3][2]}')
    else:
        #classe E
        return (f'Classe {result[4][1]}: \n\n{result[4][2]}')
   
