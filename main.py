from models.network import Network
from models.packet import Packet
from engine.simulator import Simulator
from engine.analyzer import Analyzer
from reports.reporter import Reporter


def main():
    print("=" * 55)
    print("   ANALYSEUR DE TRAFIC RESEAU (Simule)")
    print("   Universite de Parakou — Projet 10")
    print("=" * 55)

    reseau = Network()

    reseau.ajouter_noeud("A", capacite=100)
    reseau.ajouter_noeud("B", capacite=80)
    reseau.ajouter_noeud("C", capacite=120)
    reseau.ajouter_noeud("D", capacite=60)
    reseau.ajouter_noeud("E", capacite=90)

    reseau.ajouter_lien("A", "B", debit_max=50)
    reseau.ajouter_lien("A", "C", debit_max=30)
    reseau.ajouter_lien("B", "D", debit_max=40)
    reseau.ajouter_lien("C", "D", debit_max=20)
    reseau.ajouter_lien("C", "E", debit_max=60)
    reseau.ajouter_lien("D", "E", debit_max=35)
    reseau.ajouter_lien("B", "E", debit_max=25)

    print("\n--- Topologie du reseau ---")
    reseau.afficher()

    paquets = [
        Packet(id=1, source="A", destination="E", taille=10),
        Packet(id=2, source="A", destination="D", taille=5),
        Packet(id=3, source="B", destination="E", taille=8),
    ]

    simulateur = Simulator(reseau)
    print("\n--- Simulation en cours ---")
    for paquet in paquets:
        simulateur.envoyer(paquet)

    print("\n--- Analyse des goulots ---")
    analyseur = Analyzer(reseau)
    analyseur.detecter_goulots()

    print("\n--- Rapport de simulation ---")
    reporter = Reporter(simulateur.stats)
    reporter.afficher()
    reporter.exporter_csv("rapport_simulation.csv")
    print("\nRapport exporte dans rapport_simulation.csv")
    print("\nSimulation terminee.")


if __name__ == "__main__":
    main()