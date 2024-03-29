
# P9 - LitRevu Project 

Projet d'apprentissage. 
Développer une application pour demander et écrire des revues d'articles et livres avec Django, 
et suivre d'autres utilisateurs. 


## Environnemnet virtuel Pipenv 
[Doc de Pipenv](https://post-it.pycolore.fr/post-it/python/pipenv) 

*  Créer un projet : `pipenv --python 3.11` -> créer Pipfile 
*  Installer les dépendances du projet : `pipenv install` (ajouter des dépndances, comme "dev" par exemple : `--dev`) 
*  Activer l'environnement virtuel : `pipenv shell` 
    --> Le message "Launching subshell in virtual environment..." est afifché dans la console  
    --> le nom du termianl devient "pipenv" 
*  Lancer des commandes à l'intérieur de l'env virtuel : `pipenv run <command>` 
*  Lancer le serveur : `pipenv run python litrevu/manage.py runserver` 


## Installation 

1. Télécharger le dossier .zip 
2. Extraire les fichiers dans un dossier local dédié au projet 
3. installer et lancer l'environnement virtuel 
4. Visiter l'adresse http://localhost:8000/admin/ pour utiliser l'interface admin avec les identifiants d'un super_utilisateur 
5. Visiter l'adresse http://localhost:8000/home/ pour utiliser l'application en tant qu'utilisateur. 


## Autres 

### Créer un super_utilisateur depuis la console 

1. Depuis le terminal, dans le dossier du projet 'litrevu', appeler la commande `commands/createsuperuser` 
2. Répondre aux questions :    
    * Username 
    * Mail (facultatif) 
    * Mot de passe 
    * Confirmation du mot de passe 
3. Visiter l'adresse http://localhost:8000/admin/ pour utiliser l'interface d'administration, avec les informations de connexion du superutilisateur créé. 


### Créer un utilisateur (normal) depuis la console 

1.  Ouvrir une console python :    
`python manage.py shell`    

2.  Taper le code pour créer l'utilisateur : 
`from django.contrib.auth.models import User` 
`User.objects.create_user(username='<nom_user>', password='<mdp>')` 

La métohde `save()` hashe le mdp avant de l'enregistrer. 

3.  Vérifier dans l'itf web qu'il est bien créé. 


## Commandes utiles 

Ouvrir le fichier de commande désiré pour vérifier le script (avec / sans Docker, nom du container, chemin de manage.py, nom de l'app à créer...) 

Lancer une commande à partir du dossier `litrevu`. 

`./commands/migrate_pipenv` ou `./commands/migrate_docker` pour effectuer les migrations et mettre à jour la BDD. 
`./commands/install` (pour installer un package ou module Python) 
`./commands/startapp` (pour installer une application Django) 


## Visuel 

Utilisation du framework (W3CSS)[https://www.w3schools.com/w3css/] principalement pour l'utilisation des grilles CSS. 

Contraste élevé pour répondre aux recommandations WCAG du W3C. 
Tests de contraste : https://web-color.aliasdmc.fr/contraste-couleur-text-fond-wcag.php

