from engine.router import Router
from reports.stats import Stats


class Simulator:
    def __init__(self, network):
        self.network = network
        self.router = Router(network)
        self.stats = Stats()
        self.paquets_envoyes = []

    def envoyer(self, paquet):
        print(f"\n  Envoi du paquet #{paquet.id} : "
              f"{paquet.source} -> {paquet.destination}")

        chemin = self.router.chemin_optimal(paquet.source, paquet.destination)

        if not chemin:
            print(f"  [ECHEC] Aucun chemin trouve pour le paquet #{paquet.id}")
            paquet.marquer_perdu()
            self.stats.enregistrer_paquet(paquet)
            return False

        print(f"  Chemin calcule : {' -> '.join(chemin)}")
        paquet.chemin = chemin

        for nom_noeud in chemin:
            noeud = self.network.get_noeud(nom_noeud)

            accepte = noeud.recevoir_paquet(paquet)
            if not accepte:
                paquet.marquer_perdu()
                self.stats.enregistrer_paquet(paquet)
                self.paquets_envoyes.append(paquet)
                return False

            noeud.traiter_paquet()

            idx = chemin.index(nom_noeud)
            if idx < len(chemin) - 1:
                prochain = chemin[idx + 1]
                lien = self.network.get_lien(nom_noeud, prochain)
                if lien:
                    lien.transmettre(paquet.taille)

        paquet.marquer_livre()
        self.stats.enregistrer_paquet(paquet)
        self.paquets_envoyes.append(paquet)
        print(f"  [OK] Paquet #{paquet.id} livre en "
              f"{paquet.latence():.4f}s")
        return True

    def afficher_bilan(self):
        print(f"\n  Paquets envoyes   : {len(self.paquets_envoyes)}")
        livres = sum(1 for p in self.paquets_envoyes if p.est_livre)
        perdus = sum(1 for p in self.paquets_envoyes if p.est_perdu)
        print(f"  Paquets livres    : {livres}")
        print(f"  Paquets perdus    : {perdus}")