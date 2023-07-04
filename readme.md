# Calculateur IPv4 et Gestion de Réseau

Ce script Python vous permet de calculer la segmentation d'un réseau IPv4 en créant des sous-réseaux et de gérer ces sous-réseaux en les enregistrant dans une base de données et en générant un rapport.

## Installation

1. Assurez-vous d'avoir Python 3 installé sur votre système.
2. Téléchargez les fichiers source du projet.
3. Installez les dépendances requises en exécutant la commande suivante :
   pip install -r requirements.txt


## Utilisation

Pour exécuter le script, utilisez la commande suivante :
python main.py
      ou
python main.py --reseau <adresse_ip> --masque <masque_sous_reseau> --sous-reseaux <nombre_sous_reseaux>


- `--reseau` : Adresse IPv4 du réseau à segmenter (format : xxx.xxx.xxx.xxx).
- `--masque` : Masque de sous-réseau à utiliser (format : xxx.xxx.xxx.xxx).
- `--sous-reseaux` : Nombre de sous-réseaux à créer.

Le script calculera la segmentation du réseau IPv4 en créant les sous-réseaux spécifiés et affichera un rapport avec les informations sur chaque sous-réseau.


## Documentation

Pour afficher la documentation complète, utilisez la commande suivante :
python main.py -h

## Auteur

Créé par Alex Mpami

## Licence

Ce projet est sous Licence MIT. Veuillez consulter le fichier LICENCE pour plus d'informations.







