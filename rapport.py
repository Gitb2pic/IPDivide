import csv


class Rapport:
    def __init__(self):
        self.nom_fichier = 'rapport.csv'

    def generer(self, reseaux):
        # Générer le rapport des réseaux dans un fichier CSV
        with open(self.nom_fichier, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Réseau', 'Masque', 'Nombre d\'hôtes'])
            for reseau in reseaux:
                writer.writerow([reseau['reseau'], reseau['masque'], reseau['nombre_hotes']])
