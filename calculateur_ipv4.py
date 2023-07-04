from database import Database
from rapport import Rapport
from ipaddress import IPv4Address, IPv4Network


class CalculateurIPv4:
    def __init__(self):
        self.reseaux = []

    def calculer_segmentation(self, nom_reseau, reseau, masque, sous_reseaux):
        # Effectuer le calcul de la segmentation IPv4 et renvoyer les sous-réseaux calculés

        # Convertir l'adresse réseau et le masque en objets IPv4Address
        adresse_reseau = IPv4Address(reseau)
        masque_reseau = IPv4Address(masque)

        # Calculer la longueur du préfixe du masque
        longueur_prefixe = bin(int(masque_reseau)).count('1')

        # Créer le réseau principal
        reseau_principal = IPv4Network((adresse_reseau, longueur_prefixe), strict=False)

        # Diviser le réseau principal en sous-réseaux égaux
        sous_reseaux_calculés = list(reseau_principal.subnets(new_prefix=longueur_prefixe + sous_reseaux.bit_length()))

        # Stocker les sous-réseaux calculés avec leur nom, adresse hôte, adresse de diffusion et adresse réseau
        self.reseaux = []
        for i, sr in enumerate(sous_reseaux_calculés):
            reseau = {
                'nom': f'{nom_reseau}-{i + 1}',
                'reseau': str(sr.network_address),
                'masque': str(sr.netmask),
                'nombre_hotes': sr.num_addresses - 2
            }
            self.reseaux.append(reseau)

        # Retourner les sous-réseaux calculés
        return self.reseaux

    def enregistrer_donnees(self, sous_reseaux):
        # Enregistrer les données de segmentation dans la base de données
        db = Database()
        db.ajouter_reseaux(sous_reseaux)

    def generer_rapport(self, sous_reseaux):
        # Générer un rapport des données de segmentation
        rapport = Rapport()
        rapport.generer(sous_reseaux)
