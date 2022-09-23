#ce fichier sert à créer la base de données
#à éxécuter une seule fois

#imports
import sqlite3
import bcrypt

#valeurs des mots de passe 
passwordSaviour = "best"
passwordAlexandre = "5678"
passwordBoulogne = "1234"

#représentation en bytes (utf8 par défaut)
passwordSaviour = passwordSaviour.encode()
passwordAlexandre = passwordAlexandre.encode()
passwordBoulogne = passwordBoulogne.encode()

#Génération d'un sel aléatoire
saltSaviour = bcrypt.gensalt()
saltALexandre = bcrypt.gensalt()
saltBoulogne = bcrypt.gensalt()

#Génération du hash
hashSaviour = bcrypt.hashpw(passwordSaviour,saltSaviour)
hashAlexandre = bcrypt.hashpw(passwordAlexandre,saltALexandre)
hashBoulogne = bcrypt.hashpw(passwordBoulogne,saltBoulogne) 


#connexion à la base de données
connexion = sqlite3.connect('BDDLabo')
cursor = connexion.cursor()


#creation des requetes
requeteCreationUser = "create table users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,username varchar(255) unique NOT NULL, password varchar(255) NOT NULL);" 
requeteCreationClass = "create table class (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,className varchar(255) unique NOT NULL, numberOfMachines integer , numberOfNetwork INTEGER, mask varchar(255) not null);"


#exécution des requetes
cursor.execute(requeteCreationUser)
cursor.execute(requeteCreationClass)
cursor.execute("insert into class (className,numberOfMachines,numberOfNetwork,mask) values ('A',126,16777214,'255.0.0.0'),('B',16384,65534,'255.255.0.0'),('C',2097152,256,'255.255.255.0'),('D',0,0,'pas de masque : classe du multicast (multi-diffusion)'),('E',0,0,'pas de masque : classe des expérimentations'),('Réservées',0,0,'');")
cursor.execute('insert into users (username,password) values ("Saviour",?),("Boulogne",?),("Alexandre",?);',(hashSaviour.decode(),hashBoulogne.decode(),hashAlexandre.decode()))


#valider les requetes
connexion.commit()


#fermeture de la connexion à la base de données
connexion.close()

