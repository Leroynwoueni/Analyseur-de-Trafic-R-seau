from models.queue import Queue


class Node:
    def __init__(self, nom, capacite=100):
        self.nom = nom
        self.capacite = capacite
        self.file_attente = Queue(capacite_max=capacite)
        self.paquets_traites = 0
        self.paquets_perdus = 0

    def recevoir_paquet(self, paquet):
        succes = self.file_attente.enfiler(paquet)
        if not succes:
            self.paquets_perdus += 1
            print(f"  [PERTE] Paquet {paquet.id} perdu au noeud {self.nom} (file pleine)")
        return succes

    def traiter_paquet(self):
        paquet = self.file_attente.defiler()
        if paquet:
            self.paquets_traites += 1
        return paquet

    def est_sature(self, seuil=0.8):
        return self.file_attente.taux_occupation() >= seuil

    def afficher(self):
        taux = self.file_attente.taux_occupation() * 100
        print(f"  Noeud [{self.nom}] | Capacite: {self.capacite} | "
              f"File: {self.file_attente.taille()}/{self.capacite} "
              f"({taux:.0f}%) | Traites: {self.paquets_traites} | "
              f"Perdus: {self.paquets_perdus}")

    def __str__(self):
        return f"Node({self.nom}, capacite={self.capacite})"

    def __repr__(self):
        return self.__str__()