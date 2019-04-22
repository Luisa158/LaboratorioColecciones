import unittest
from custom_functions import temperature


class TestCollectionMethods(unittest.TestCase):

    def test_prom(self):

        lista= [32, 33, 43, 51,21,34,32,12,34,32,56,64]
        Total= temperature.prom(lista)

        self.assertEqual(Total, 3.75)

    def test_desviatin(self):

        lista = [1,1,1,1,1,1,1,1,1,1,1,1]
        Total = temperature.desviacion_estandar(lista)


        self.assertEqual(Total, 0)




if __name__ == '__main__':
    unittest.main()
