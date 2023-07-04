import json


class Database:
    def __init__(self):
        self.nom_fichier = 'reseaux_enregistres.json'

    def ajouter_reseaux(self, reseaux):
        # Ajouter les réseaux à la base de données
        # (dans notre cas, enregistrement dans un fichier JSON)
        with open(self.nom_fichier, 'a') as f:
            for reseau in reseaux:
                json.dump(reseau, f)
                f.write('\n')
