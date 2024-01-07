class Circular(list):
    
    def __init__(self, sequence=[]):
        super(Circular, self).__init__(sequence)
        self.position = 0

    def current(self):
        return self[self.position]
            
    def next(self, n=1):
        self.position = (self.position + n) % len(self)
        return self[self.position]
        
    def prev(self, n=1):
        return self.next(-n)


if __name__ == '__main__':
    '''Clase testeada con unittest'''

    import unittest

    class Prueba(unittest.TestCase):
        def setUp(self):
            self.l = Circular([1, 2, 3, 15, "www", 'u'])
        def testArrancaDeCero(self):
            self.assertEqual(self.l.current(), 1)
        def testTomaElPasoComoParametroOpcional(self):
            self.assertEqual(self.l.next(4), "www")
            self.assertEqual(self.l.next(), 'u')
        def testTomaPasoNegativo(self):
            self.assertEqual(self.l.next(-2), "www")
        def testTomaPasoQueDaUnParDeVueltas(self):
            self.assertEqual(self.l.next(8), 3)
        def testSePortaIgualParaAtrasYParaAdelante(self):
            self.assertEqual(self.l.prev(), 'u')
            self.assertEqual(self.l.prev(-6), 'u')
        def testNoItems(self):
            self.assertRaises(Exception, Circular([]).next)
        def testInstanciarSinParametros(self):
            self.assertEquals(Circular(), Circular([]))

    unittest.main()
