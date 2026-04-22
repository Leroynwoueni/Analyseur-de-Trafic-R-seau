import unittest
from models.node import Node
from models.packet import Packet


class TestNode(unittest.TestCase):

    def setUp(self):
        self.noeud = Node("A", capacite=5)
        self.paquet = Packet(id=1, source="A", destination="E", taille=1)

    def test_creation_noeud(self):
        self.assertEqual(self.noeud.nom, "A")
        self.assertEqual(self.noeud.capacite, 5)

    def test_recevoir_paquet(self):
        resultat = self.noeud.recevoir_paquet(self.paquet)
        self.assertTrue(resultat)
        self.assertEqual(self.noeud.file_attente.taille(), 1)

    def test_file_pleine(self):
        for i in range(5):
            p = Packet(id=i, source="A", destination="B", taille=1)
            self.noeud.recevoir_paquet(p)
        paquet_extra = Packet(id=99, source="A", destination="B", taille=1)
        resultat = self.noeud.recevoir_paquet(paquet_extra)
        self.assertFalse(resultat)
        self.assertEqual(self.noeud.paquets_perdus, 1)

    def test_traiter_paquet(self):
        self.noeud.recevoir_paquet(self.paquet)
        traite = self.noeud.traiter_paquet()
        self.assertEqual(traite.id, self.paquet.id)
        self.assertEqual(self.noeud.paquets_traites, 1)

    def test_saturation(self):
        for i in range(4):
            p = Packet(id=i, source="A", destination="B", taille=1)
            self.noeud.recevoir_paquet(p)
        self.assertTrue(self.noeud.est_sature(seuil=0.8))


class TestQueue(unittest.TestCase):

    def setUp(self):
        from models.queue import Queue
        self.queue = Queue(capacite_max=3)
        self.p1 = Packet(id=1, source="A", destination="B", taille=1)
        self.p2 = Packet(id=2, source="A", destination="C", taille=1)

    def test_enfiler_defiler_fifo(self):
        self.queue.enfiler(self.p1)
        self.queue.enfiler(self.p2)
        sorti = self.queue.defiler()
        self.assertEqual(sorti.id, 1)  

    def test_file_vide(self):
        self.assertIsNone(self.queue.defiler())

    def test_taux_occupation(self):
        self.queue.enfiler(self.p1)
        self.assertAlmostEqual(self.queue.taux_occupation(), 1/3)


if __name__ == '__main__':
    unittest.main()