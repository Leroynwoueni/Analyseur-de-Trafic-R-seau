class Queue:
    def __init__(self, capacite_max=100):
        self.capacite_max = capacite_max
        self._file = []  
    def enfiler(self, paquet):
        if self.est_pleine():
            return False
        self._file.append(paquet)
        return True

    def defiler(self):
        if self.est_vide():
            return None
        return self._file.pop(0)

    def apercu(self):
        if self.est_vide():
            return None
        return self._file[0]

    def est_vide(self):
        return len(self._file) == 0

    def est_pleine(self):
        return len(self._file) >= self.capacite_max

    def taille(self):
        return len(self._file)

    def taux_occupation(self):
        if self.capacite_max == 0:
            return 0.0
        return len(self._file) / self.capacite_max

    def vider(self):
        self._file.clear()

    def __str__(self):
        return f"Queue({self.taille()}/{self.capacite_max})"

    def __repr__(self):
        return self.__str__()