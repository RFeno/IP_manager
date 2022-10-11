import bcrypt
import sqlite3

def checkUserPassword(username,password):
    """
    It takes a username and password, connects to the database, gets the password for the user, and then
    compares the password in the database to the password the user entered
    
    :param username: The username of the user you want to check the password for
    :param password: The password to be hashed
    :return: if password is correct.
    """
    print(f"mot de passe à vérifier :{password} pour user :{username}")

    #connexion db + récupération des données
    connexion = sqlite3.connect("BDDLabo")
    cursor = connexion.cursor()
    cursor.execute(f"SELECT password FROM users WHERE username like '{username}' ;")
    result = cursor.fetchone()
    cursor.close()

    if(result is None):
        return False
    
    if(bcrypt.checkpw(password.encode(),str(result[0]).encode())):
        print("Mot de passe correct, accès autorisé")
        return True
    else:
        print("Mot de passe incorrect, accès refusé")
        return False

def checkUserExists(username):
    """
    It connects to the database, executes a query, and returns the result
    
    :param username: the username to check
    :return: A boolean value.
    """
    #connexion db + récupération des données
    connexion = sqlite3.connect("BDDLabo")
    cursor = connexion.cursor()
    cursor.execute(f"SELECT username FROM users WHERE username like '{username}' ;")
    result = cursor.fetchone()
    cursor.close()
    return result is not None
      

def createUser(username,password):
    """
    It creates a user with the username and password provided.
    
    :param username: The username of the user you want to create
    :param password: The password for the user
    """
    
    #vérification tailles
    if (len(password) < 4):
        return "passwordTooSmall"
    
    if(len(username) < 4):
        return "usernameTooSmall"

    #encodage en utf8
    password_encode = password.encode()

    #Génération d'un sel aléatoire
    salt_for_password = bcrypt.gensalt()

    #hashage du mot de passe
    hash_password = bcrypt.hashpw(password_encode,salt_for_password)

    if (checkUserExists(username) == False):
        return insertToDB(username, hash_password.decode())
    else:
        return "UserAlreadyExist"

def insertToDB(username, hash_password):
    """
    This function takes in a username and a hash_password and inserts them into the database.
    
    :param username: The username of the user
    :param hash_password: The hashed password
    """
    
    connexion = sqlite3.connect("BDDLabo")
    cursor = connexion.cursor()
    cursor.execute("INSERT INTO users (username,password) VALUES (?,?);",(username,hash_password))
    #valider les requetes
    connexion.commit()
    
    #fermeture
    cursor.close()
    connexion.close()

    #on vérifie que l'utilisateur existe à présent
    return "UserCree" if (checkUserExists(username)) else "ErrorCreation"   

def deleteUser(username):
    """
    It deletes a user from the database.
    
    :param username: The username of the user to delete
    """
    
    if (checkUserExists(username) == False):
        return "UserDoesNotExist"
    
    connexion = sqlite3.connect("BDDLabo")
    cursor = connexion.cursor()
    cursor.execute(f'DELETE from users where username like "{username}" ;', )
    
    #valider les requetes
    connexion.commit()

    #fermeture
    cursor.close()
    connexion.close()

    if(checkUserExists(username) == False):
        return "UserDeleted"

   
   
    
