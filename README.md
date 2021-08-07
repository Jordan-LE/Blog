DEMARRER L'APPLICATION

1. Activer l'environnement virtuel Python integre au projet
	- Demarrer un terminal (PowerShell, invite de commande, ...)
	- Se deplacer dans le repertoire racine du projet avec la commande :
		cd [chemin du repertoire]
	- Activer l'environnement virtuel avec la commande (differente selon le terminal utilise) :
		source .venv/Scripts/activate
		.venv/Scripts/activate.bat (invite de commande)
		.venv/Scripts/Activate.ps1 (PowerShell)
		
2. Demarrer le serveur Django
	- Apres avoir active l'environnement virtuel et dans le repertoire racine du projet, ou se trouve le fichier manage.py, executer la commande :
		python manage.py runserver
		
3. Se rendre sur le site
	- Ouvrir un navigateur internet et se rendre a l'URL :
		localhost:8000
		
	
	
A SAVOIR POUR UTILISER L'APPLICATION

URL de la page administrateur : localhost:8000/admin

Compte administrateur :
	Nom d'utilisateur -> admin
	Mot de passe -> admin