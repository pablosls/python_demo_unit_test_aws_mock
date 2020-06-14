from exercicio1 import somar
import unittest

class TestSoma(unittest.TestCase):
    def testSoma(self):
        assert somar(1,4) == 5