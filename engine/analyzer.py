class Analyzer:
    def __init__(self, network, seuil=0.8):
        self.network = network
        self.seuil = seuil
        self.goulots_noeuds = []
        self.goulots_liens = []

    def detecter_goulots(self):
        self.goulots_noeuds = []
        self.goulots_liens = []

        for noeud in self.network.noeuds.values():
            if noeud.est_sature(self.seuil):
                self.goulots_noeuds.append(noeud)

        for lien in self.network.liens:
            if lien.est_sature(self.seuil):
                self.goulots_liens.append(lien)

        self._afficher_resultats()

    def _afficher_resultats(self):
        if not self.goulots_noeuds and not self.goulots_liens:
            print("  Aucun goulot d'etranglement detecte. Reseau fluide.")
            return

        if self.goulots_noeuds:
            print(f"  [ALERTE] {len(self.goulots_noeuds)} noeud(s) sature(s) :")
            for noeud in self.goulots_noeuds:
                taux = noeud.file_attente.taux_occupation() * 100
                print(f"    - Noeud {noeud.nom} : {taux:.0f}% d'occupation")

        if self.goulots_liens:
            print(f"  [ALERTE] {len(self.goulots_liens)} lien(s) sature(s) :")
            for lien in self.goulots_liens:
                taux = lien.taux_utilisation() * 100
                print(f"    - Lien {lien.noeud1}<->{lien.noeud2} : "
                      f"{taux:.0f}% d'utilisation")

    def rapport_goulots(self):
        return {
            'noeuds': [n.nom for n in self.goulots_noeuds],
            'liens': [f"{l.noeud1}<->{l.noeud2}" for l in self.goulots_liens]
        }