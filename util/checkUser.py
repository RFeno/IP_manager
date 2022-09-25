import bcrypt
import sqlite3


def checkUserPassword(username,password):
    print(f"mot de passe à vérifier :{password} pour user :{username}")

    #connexion db + récupération des données
    connexion = sqlite3.connect("BDDLabo")
    cursor = connexion.cursor()
    cursor.execute(f"SELECT password FROM users WHERE username like '{username}' ;")
    result = cursor.fetchone()
    
    print(f"resultat de la requête : {result}")

    if(result is None):
        return False
    
    if(bcrypt.checkpw(password.encode(),str(result[0]).encode())):
        print("Mot de passe correct, accès autorisé")
        return True
    else:
        print("Mot de passe incorrect, accès refusé")
        return False


        