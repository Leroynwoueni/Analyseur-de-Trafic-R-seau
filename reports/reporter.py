import csv


class Reporter:
    def __init__(self, stats):
        self.stats = stats

    def afficher(self):
        resume = self.stats.resume()
        print("\n  +-----------------------------------------+")
        print("  |        RAPPORT DE SIMULATION            |")
        print("  +-----------------------------------------+")
        print(f"  | Total paquets       : {resume['total_paquets']:<18}|")
        print(f"  | Paquets livres      : {resume['paquets_livres']:<18}|")
        print(f"  | Paquets perdus      : {resume['paquets_perdus']:<18}|")
        print(f"  | Taux de livraison   : {resume['taux_livraison_%']}%{'':<15}|")

        lat_moy = resume['latence_moyenne_s']
        lat_moy_str = f"{lat_moy:.6f}s" if lat_moy is not None else "N/A"
        print(f"  | Latence moyenne     : {lat_moy_str:<18}|")

        lat_max = resume['latence_max_s']
        lat_max_str = f"{lat_max:.6f}s" if lat_max is not None else "N/A"
        print(f"  | Latence maximale    : {lat_max_str:<18}|")
        print(f"  | Longueur moy chemin : {resume['longueur_moyenne_chemin']:<18}|")
        print("  +-----------------------------------------+")

        print("\n  Detail par paquet :")
        for paquet in self.stats.paquets:
            paquet.afficher()

    def exporter_csv(self, nom_fichier="rapport.csv"):
        with open(nom_fichier, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)

            # En-tete
            writer.writerow([
                "id", "source", "destination", "taille",
                "statut", "chemin", "latence_s"
            ])

            # Donnees
            for paquet in self.stats.paquets:
                statut = "livre" if paquet.est_livre else "perdu"
                chemin = " -> ".join(paquet.chemin) if paquet.chemin else "N/A"
                latence = f"{paquet.latence():.6f}" if paquet.latence() else "N/A"
                writer.writerow([
                    paquet.id,
                    paquet.source,
                    paquet.destination,
                    paquet.taille,
                    statut,
                    chemin,
                    latence
                ])

            writer.writerow([])
            resume = self.stats.resume()
            writer.writerow(["RESUME", "", "", "", "", "", ""])
            for cle, valeur in resume.items():
                writer.writerow([cle, valeur])