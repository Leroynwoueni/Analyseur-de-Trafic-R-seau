
class Router:
    def __init__(self, network):
        self.network = network

    def chemin_optimal(self, source, destination):
        noeuds = self.network.noms_noeuds()

        if source not in noeuds:
            print(f"  [ERREUR] Noeud source '{source}' introuvable.")
            return None
        if destination not in noeuds:
            print(f"  [ERREUR] Noeud destination '{destination}' introuvable.")
            return None

        distances = {n: float('inf') for n in noeuds}
        distances[source] = 0
        predecesseurs = {n: None for n in noeuds}
        non_visites = set(noeuds)

        while non_visites:
            noeud_actuel = min(non_visites, key=lambda n: distances[n])

            if distances[noeud_actuel] == float('inf'):
                break

            if noeud_actuel == destination:
                break

            non_visites.remove(noeud_actuel)

            for voisin, debit_max in self.network.get_voisins(noeud_actuel):
                if voisin not in non_visites:
                    continue
                cout = 1 / debit_max if debit_max > 0 else float('inf')
                nouvelle_distance = distances[noeud_actuel] + cout

                if nouvelle_distance < distances[voisin]:
                    distances[voisin] = nouvelle_distance
                    predecesseurs[voisin] = noeud_actuel

        return self._reconstruire_chemin(predecesseurs, source, destination)

    def _reconstruire_chemin(self, predecesseurs, source, destination):
        chemin = []
        noeud = destination

        while noeud is not None:
            chemin.insert(0, noeud)
            noeud = predecesseurs[noeud]

        if chemin[0] != source:
            return None  

        return chemin

    def afficher_chemin(self, source, destination):
        chemin = self.chemin_optimal(source, destination)
        if chemin:
            print(f"  Chemin optimal {source} -> {destination} : "
                  f"{' -> '.join(chemin)}")
        else:
            print(f"  Aucun chemin entre {source} et {destination}.")
        return chemin