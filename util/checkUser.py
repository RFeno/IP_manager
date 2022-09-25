import bcrypt
import sqlite3


def checkUserPassword(username,password):
    print(f"Password à vérifier :{password} pour user :{username}")

    #connexion db + récupération des données
    connexion = sqlite3.connect("BDDLabo")
    cursor = connexion.cursor()
    cursor.execute(f"SELECT password FROM users WHERE username like '%{username}%' ;")
    result = cursor.fetchone()

   
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    
    if(bcrypt.checkpw(password.encode(),str(result[0]).encode())):
        print("Mot de passe correct, accès autorisé")
        return True
    else:
        print("Mot de passe incorrect, accès refusé")
        return False
        
        