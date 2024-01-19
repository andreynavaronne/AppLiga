import unittest

class JogoTest(unittest.TestCase):

    def test_multiplicadores(self):
        jogo = Jogo("Catan", 7, 7, 2)
        self.assertEqual([1, 0], jogo.multiplicadores())