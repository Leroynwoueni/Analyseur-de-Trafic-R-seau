
import time


class Packet:
    def __init__(self, id, source, destination, taille=1):
        self.id = id
        self.source = source
        self.destination = destination
        self.taille = taille
        self.timestamp_creation = time.time()
        self.timestamp_livraison = None
        self.chemin = []        # Liste des noeuds traverses
        self.est_livre = False
        self.est_perdu = False

    def marquer_livre(self):
        self.est_livre = True
        self.timestamp_livraison = time.time()

    def marquer_perdu(self):
        self.est_perdu = True

    def latence(self):
        if self.timestamp_livraison is None:
            return None
        return self.timestamp_livraison - self.timestamp_creation

    def ajouter_noeud_chemin(self, nom_noeud):
        self.chemin.append(nom_noeud)

    def afficher(self):
        statut = "Livre" if self.est_livre else ("Perdu" if self.est_perdu else "En transit")
        chemin_str = " -> ".join(self.chemin) if self.chemin else "N/A"
        print(f"  Paquet #{self.id} | {self.source} -> {self.destination} | "
              f"Taille: {self.taille} | Statut: {statut} | Chemin: {chemin_str}")

    def __str__(self):
        return f"Packet(id={self.id}, {self.source}->{self.destination})"

    def __repr__(self):
        return self.__str__()