
from models.node import Node
from models.link import Link


class Network:
    def __init__(self):
        self.noeuds = {}   
        self.liens = []    


    def ajouter_noeud(self, nom, capacite=100):
        if nom in self.noeuds:
            print(f"  [AVERTISSEMENT] Le noeud '{nom}' existe deja.")
            return
        self.noeuds[nom] = Node(nom, capacite)

    def ajouter_lien(self, noeud1, noeud2, debit_max=100):
        if noeud1 not in self.noeuds:
            print(f"  [ERREUR] Noeud '{noeud1}' introuvable.")
            return
        if noeud2 not in self.noeuds:
            print(f"  [ERREUR] Noeud '{noeud2}' introuvable.")
            return
        lien = Link(noeud1, noeud2, debit_max)
        self.liens.append(lien)

    def supprimer_noeud(self, nom):
        if nom not in self.noeuds:
            print(f"  [ERREUR] Noeud '{nom}' introuvable.")
            return
        del self.noeuds[nom]
        self.liens = [l for l in self.liens if not l.connecte(nom)]


    def get_noeud(self, nom):
        return self.noeuds.get(nom, None)

    def get_voisins(self, nom):
        voisins = []
        for lien in self.liens:
            autre = lien.autre_extremite(nom)
            if autre is not None and lien.actif:
                voisins.append((autre, lien.debit_max))
        return voisins

    def get_lien(self, noeud1, noeud2):
        for lien in self.liens:
            if lien.connecte(noeud1) and lien.connecte(noeud2):
                return lien
        return None

    def noms_noeuds(self):
        return list(self.noeuds.keys())

    def reinitialiser_debits(self):
        for lien in self.liens:
            lien.reinitialiser_debit()


    def afficher(self):
        print(f"\nReseau : {len(self.noeuds)} noeuds | {len(self.liens)} liens")
        print("\nNoeuds :")
        for noeud in self.noeuds.values():
            noeud.afficher()
        print("\nLiens :")
        for lien in self.liens:
            lien.afficher()

    def __str__(self):
        return f"Network({len(self.noeuds)} noeuds, {len(self.liens)} liens)"

    def __repr__(self):
        return self.__str__()