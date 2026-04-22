import unittest
from models.queue import Queue
from models.packet import Packet


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue(capacite_max=3)
        self.p1 = Packet(id=1, source="A", destination="B", taille=1)
        self.p2 = Packet(id=2, source="B", destination="C", taille=1)
        self.p3 = Packet(id=3, source="C", destination="D", taille=1)
        self.p4 = Packet(id=4, source="D", destination="E", taille=1)

    def test_enfiler_simple(self):
        self.queue.enfiler(self.p1)
        self.assertEqual(self.queue.taille(), 1)

    def test_defiler_fifo(self):
        self.queue.enfiler(self.p1)
        self.queue.enfiler(self.p2)
        self.assertEqual(self.queue.defiler().id, 1)
        self.assertEqual(self.queue.defiler().id, 2)

    def test_file_pleine(self):
        self.queue.enfiler(self.p1)
        self.queue.enfiler(self.p2)
        self.queue.enfiler(self.p3)
        self.assertTrue(self.queue.est_pleine())
        resultat = self.queue.enfiler(self.p4)
        self.assertFalse(resultat)

    def test_file_vide(self):
        self.assertTrue(self.queue.est_vide())
        self.assertIsNone(self.queue.defiler())

    def test_apercu_sans_retirer(self):
        self.queue.enfiler(self.p1)
        apercu = self.queue.apercu()
        self.assertEqual(apercu.id, 1)
        self.assertEqual(self.queue.taille(), 1)  # Toujours 1

    def test_vider(self):
        self.queue.enfiler(self.p1)
        self.queue.enfiler(self.p2)
        self.queue.vider()
        self.assertTrue(self.queue.est_vide())
        self.assertEqual(self.queue.taille(), 0)

    def test_taux_occupation(self):
        self.assertEqual(self.queue.taux_occupation(), 0.0)
        self.queue.enfiler(self.p1)
        self.assertAlmostEqual(self.queue.taux_occupation(), 1/3)
        self.queue.enfiler(self.p2)
        self.queue.enfiler(self.p3)
        self.assertEqual(self.queue.taux_occupation(), 1.0)


if __name__ == '__main__':
    unittest.main()