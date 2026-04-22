class Link:
    def __init__(self, noeud1, noeud2, debit_max=100):
        self.noeud1 = noeud1
        self.noeud2 = noeud2
        self.debit_max = debit_max
        self.debit_actuel = 0
        self.paquets_transmis = 0
        self.actif = True

    def transmettre(self, quantite=1):
        if not self.actif:
            return False
        if self.debit_actuel + quantite > self.debit_max:
            return False
        self.debit_actuel += quantite
        self.paquets_transmis += quantite
        return True

    def reinitialiser_debit(self):
        self.debit_actuel = 0

    def est_sature(self, seuil=0.8):
        if self.debit_max == 0:
            return True
        return (self.debit_actuel / self.debit_max) >= seuil

    def taux_utilisation(self):
        if self.debit_max == 0:
            return 0.0
        return self.debit_actuel / self.debit_max

    def connecte(self, noeud):
        return noeud == self.noeud1 or noeud == self.noeud2

    def autre_extremite(self, noeud):
        if noeud == self.noeud1:
            return self.noeud2
        if noeud == self.noeud2:
            return self.noeud1
        return None

    def afficher(self):
        taux = self.taux_utilisation() * 100
        statut = "SATURE" if self.est_sature() else "OK"
        print(f"  Lien [{self.noeud1} <-> {self.noeud2}] | "
              f"Debit: {self.debit_actuel}/{self.debit_max} ({taux:.0f}%) | "
              f"Transmis: {self.paquets_transmis} | Statut: {statut}")

    def __str__(self):
        return f"Link({self.noeud1}<->{self.noeud2}, debit_max={self.debit_max})"

    def __repr__(self):
        return self.__str__()