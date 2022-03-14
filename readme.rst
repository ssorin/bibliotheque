Mediatheque
===========

Projet mediatheque pour illustrer le cours Django pour l'ISFAC


Install
-------
- renomer le fichier settings_local.sample.py en settings_local.py
- manage.py migrate
- manage.py createsuperuser

Etape 1 :
---------

- Création du projet
- modification du nom de l'app de base en 'core'
- creation de la home page
- ajout des templates layouts.html et home.html

Etape 2 :
---------
- Création de l'application biblio
- Création du models avec les différentes tables et quelques methodes/propriété utiles (get_absolute_url, image)
- creation des vues liste et detail pour l'ensemble des tables
- creation des templates liste et detail pour l'ensemble des tables
- administration de l'ensemble des tables
- change image upload_to in books and series models