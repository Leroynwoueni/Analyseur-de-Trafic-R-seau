class Stats:
    def __init__(self):
        self.paquets = []          

    def enregistrer_paquet(self, paquet):
        self.paquets.append(paquet)

    def total_paquets(self):
        return len(self.paquets)

    def total_livres(self):
        return sum(1 for p in self.paquets if p.est_livre)

    def total_perdus(self):
        return sum(1 for p in self.paquets if p.est_perdu)

    def taux_livraison(self):
        if self.total_paquets() == 0:
            return 0.0
        return self.total_livres() / self.total_paquets()

    def latence_moyenne(self):
        latences = [p.latence() for p in self.paquets
                    if p.est_livre and p.latence() is not None]
        if not latences:
            return None
        return sum(latences) / len(latences)

    def latence_max(self):
        latences = [p.latence() for p in self.paquets
                    if p.est_livre and p.latence() is not None]
        return max(latences) if latences else None

    def longueur_moyenne_chemin(self):
        chemins = [len(p.chemin) for p in self.paquets if p.chemin]
        if not chemins:
            return 0
        return sum(chemins) / len(chemins)

    def resume(self):
        return {
            'total_paquets': self.total_paquets(),
            'paquets_livres': self.total_livres(),
            'paquets_perdus': self.total_perdus(),
            'taux_livraison_%': round(self.taux_livraison() * 100, 2),
            'latence_moyenne_s': self.latence_moyenne(),
            'latence_max_s': self.latence_max(),
            'longueur_moyenne_chemin': round(self.longueur_moyenne_chemin(), 2),
        }