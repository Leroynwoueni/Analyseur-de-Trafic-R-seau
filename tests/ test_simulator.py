"""
Tests unitaires pour la classe Simulator.
"""

import unittest
from models.network import Network
from models.packet import Packet
from engine.simulator import Simulator


class TestSimulator(unittest.TestCase):

    def setUp(self):
        self.reseau = Network()
        self.reseau.ajouter_noeud("A", capacite=100)
        self.reseau.ajouter_noeud("B", capacite=100)
        self.reseau.ajouter_noeud("C", capacite=100)
        self.reseau.ajouter_lien("A", "B", debit_max=50)
        self.reseau.ajouter_lien("B", "C", debit_max=50)
        self.simulateur = Simulator(self.reseau)

    def test_envoi_paquet_simple(self):
        paquet = Packet(id=1, source="A", destination="C", taille=1)
        resultat = self.simulateur.envoyer(paquet)
        self.assertTrue(resultat)
        self.assertTrue(paquet.est_livre)

    def test_paquet_destination_inconnue(self):
        paquet = Packet(id=2, source="A", destination="Z", taille=1)
        resultat = self.simulateur.envoyer(paquet)
        self.assertFalse(resultat)
        self.assertTrue(paquet.est_perdu)

    def test_chemin_enregistre(self):
        paquet = Packet(id=3, source="A", destination="C", taille=1)
        self.simulateur.envoyer(paquet)
        self.assertGreater(len(paquet.chemin), 0)
        self.assertEqual(paquet.chemin[0], "A")
        self.assertEqual(paquet.chemin[-1], "C")

    def test_statistiques_mises_a_jour(self):
        paquet = Packet(id=4, source="A", destination="B", taille=1)
        self.simulateur.envoyer(paquet)
        self.assertEqual(self.simulateur.stats.total_paquets(), 1)
        self.assertEqual(self.simulateur.stats.total_livres(), 1)


if __name__ == '__main__':
    unittest.main()