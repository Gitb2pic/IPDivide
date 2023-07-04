import argparse
from calculateur_ipv4 import CalculateurIPv4
import random
from ascii_generator import generate_ascii_art

def main():
    # Configuration de l'interface en ligne de commande (CLI)
    parser = argparse.ArgumentParser(
        description='Calculateur IPv4 et gestion de réseau',
        epilog='Utilisez la commande -h pour afficher la documentation complète.'
    )
    parser.add_argument('--reseau', type=str, help='Adresse IPv4 du réseau. (Format : xxx.xxx.xxx.xxx)')
    parser.add_argument('--masque', type=str, help='Masque de sous-réseau. (Format : xxx.xxx.xxx.xxx)')
    parser.add_argument('--sous-reseaux', type=int, help='Nombre de sous-réseaux à créer.')
    parser.add_argument('--recherche', type=str, help='Recherche un réseau par nom dans la mémoire et la base de données.')
    args = parser.parse_args()

    # Générateur de code ASCII aléatoire du nom de l'application
    ascii_text = "IPDivide"
    ascii_style = random.choice(["standard", "shadow", "slant"])
    ascii_art = generate_ascii_art(ascii_text, ascii_style)
    print(ascii_art)
    # Vérification des arguments requis

    if not args.reseau or not args.masque or not args.sous_reseaux:
        # Prompt pour demander les informations manquantes à l'utilisateur
        print("Certains arguments sont manquants.")
        args.reseau = input("Adresse IPv4 du réseau (Format : xxx.xxx.xxx.xxx) : ")
        args.masque = input("Masque de sous-réseau (Format : xxx.xxx.xxx.xxx) : ")
        args.sous_reseaux = int(input("Nombre de sous-réseaux à créer : "))

    # Exemple d'utilisation
    calculateur = CalculateurIPv4()
    if args.recherche:
        # Recherche d'un réseau par nom dans la mémoire et la base de données
        resultats = [r for r in calculateur.reseaux if args.recherche.lower() in r['nom'].lower()]
        if resultats:
            print(f"Résultats de recherche pour '{args.recherche}':")
            for resultat in resultats:
                print(f"Nom : {resultat['nom']}")
                print(f"Adresse réseau : {resultat['reseau']}")
                print(f"Adresse hôte : {IPv4Network(resultat['reseau']).network_address + 1}")
                print(f"Adresse de diffusion : {IPv4Network(resultat['reseau']).broadcast_address}")
                print("-----")
        else:
            print(f"Aucun résultat trouvé pour '{args.recherche}'.")
    else:
        sous_reseaux = calculateur.calculer_segmentation("MonReseau", args.reseau, args.masque, args.sous_reseaux)
        calculateur.enregistrer_donnees(sous_reseaux)
        calculateur.generer_rapport(sous_reseaux)

if __name__ == "__main__":
    main()
