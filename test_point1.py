import unittest

from model.point1 import genererPoint1


class Test(unittest.TestCase):

    def testInvalid(self):
        self.assertEqual(genererPoint1("256.55.55.25"),"IpInvalid")
        self.assertEqual(genererPoint1("255.55.55."),"IpInvalid")
        self.assertEqual(genererPoint1("255.55..25"),"IpInvalid")
        self.assertEqual(genererPoint1("255.555.55.25"),"IpInvalid")
        
    def testReserve(self):
        self.assertEqual(genererPoint1("0.25.55.56"),"Classe Réservées")
        self.assertEqual(genererPoint1("0.255.255.255"),"Classe Réservées")
        self.assertEqual(genererPoint1("127.58.96.68"),"Classe Réservées")
        self.assertEqual(genererPoint1("127.78.96.36"),"Classe Réservées")
    
    def testClassA(self):
        self.assertEqual(genererPoint1("124.23.12.71"),"Classe A: \n126 réseaux de 16777214 machines") 
        self.assertEqual(genererPoint1("125.2.3.85"),"Classe A: \n126 réseaux de 16777214 machines") 
        self.assertEqual(genererPoint1("126.23.12.71"),"Classe A: \n126 réseaux de 16777214 machines") 
        self.assertEqual(genererPoint1("52.23.12.71"),"Classe A: \n126 réseaux de 16777214 machines") 
        self.assertEqual(genererPoint1("87.23.12.71"),"Classe A: \n126 réseaux de 16777214 machines") 
        self.assertEqual(genererPoint1("126.23.12.71"),"Classe A: \n126 réseaux de 16777214 machines") 
    
    def testClassA(self):
        self.assertEqual(genererPoint1("124.23.12.71"),"Classe A: \n126 réseaux de 16777214 machines") 
        self.assertEqual(genererPoint1("125.2.3.85"),"Classe A: \n126 réseaux de 16777214 machines") 
        self.assertEqual(genererPoint1("126.23.12.71"),"Classe A: \n126 réseaux de 16777214 machines") 
        self.assertEqual(genererPoint1("52.23.12.71"),"Classe A: \n126 réseaux de 16777214 machines") 
        self.assertEqual(genererPoint1("87.23.12.71"),"Classe A: \n126 réseaux de 16777214 machines") 
        self.assertEqual(genererPoint1("126.23.12.71"),"Classe A: \n126 réseaux de 16777214 machines") 
        
    def testClassB(self):
        self.assertEqual(genererPoint1("128.23.12.71"),"Classe B: \n16384 réseaux de 65534 machines") 
        self.assertEqual(genererPoint1("131.24.35.85"),"Classe B: \n16384 réseaux de 65534 machines") 
        self.assertEqual(genererPoint1("157.23.12.71"),"Classe B: \n16384 réseaux de 65534 machines") 
        self.assertEqual(genererPoint1("182.23.12.71"),"Classe B: \n16384 réseaux de 65534 machines") 
        self.assertEqual(genererPoint1("167.23.12.71"),"Classe B: \n16384 réseaux de 65534 machines") 
        self.assertEqual(genererPoint1("191.23.12.71"),"Classe B: \n16384 réseaux de 65534 machines")
    
    def testClassC(self):
        self.assertEqual(genererPoint1("192.23.12.71"),"Classe C: \n2097152 réseaux de 256 machines") 
        self.assertEqual(genererPoint1("200.24.35.85"),"Classe C: \n2097152 réseaux de 256 machines") 
        self.assertEqual(genererPoint1("210.23.12.71"),"Classe C: \n2097152 réseaux de 256 machines") 
        self.assertEqual(genererPoint1("197.23.12.71"),"Classe C: \n2097152 réseaux de 256 machines") 
        self.assertEqual(genererPoint1("207.23.12.71"),"Classe C: \n2097152 réseaux de 256 machines") 
        self.assertEqual(genererPoint1("223.23.12.71"),"Classe C: \n2097152 réseaux de 256 machines")
    
    def testClassD(self):
        self.assertEqual(genererPoint1("224.23.12.71"),"Classe D: \nadresses uniques") 
        self.assertEqual(genererPoint1("236.24.35.85"),"Classe D: \nadresses uniques") 
        self.assertEqual(genererPoint1("225.23.12.71"),"Classe D: \nadresses uniques") 
        self.assertEqual(genererPoint1("231.23.12.71"),"Classe D: \nadresses uniques") 
        self.assertEqual(genererPoint1("235.23.12.71"),"Classe D: \nadresses uniques") 
        self.assertEqual(genererPoint1("239.23.12.71"),"Classe D: \nadresses uniques")
        
    def testClassD(self):
        self.assertEqual(genererPoint1("240.23.12.71"),"Classe E: \nadresses uniques") 
        self.assertEqual(genererPoint1("245.24.35.85"),"Classe E: \nadresses uniques") 
        self.assertEqual(genererPoint1("250.23.12.71"),"Classe E: \nadresses uniques") 
        self.assertEqual(genererPoint1("255.23.12.71"),"Classe E: \nadresses uniques") 
        self.assertEqual(genererPoint1("242.23.12.71"),"Classe E: \nadresses uniques") 
        self.assertEqual(genererPoint1("254.23.12.71"),"Classe E: \nadresses uniques")
        
    
        
        
if __name__ == '__main__':
    unittest.main()