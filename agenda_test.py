import unittest
from agenda import consulta

class TestAgenda(unittest.TestCase):
    def testConsult(self):
        assert consulta('pablo') == True

    def testConsult2(self):
        self.assertEqual(consulta('pablo'), True)

