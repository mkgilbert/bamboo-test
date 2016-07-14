from unittest import TestCase
from bam import Bam

class TestBam(TestCase):
    
    def setUp(self):
        self.b = Bam(10)        

    def test_init(self):
        self.assertEqual(self.b.height, 10)

    def test_grow(self):
        h = self.b.height
        g = self.b.grow(1)
        self.assertEqual(g, h+1)
        self.b.height = h


if __name__ == '__main__':
    unittest.main()        
