import unittest
import sys
import os

#permettant l'import
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from model.point5 import genererPoint5

class Test(unittest.TestCase):

    def testIpInvalid(self):
        self.assertEqual(genererPoint5("256.55.55.25","255.255.255.0","2","1"),"IpInvalid")
        self.assertEqual(genererPoint5("255.55.55.","255.255.255.0","2","1"),"IpInvalid")
        self.assertEqual(genererPoint5("255.55..25","255.255.255.0","2","1"),"IpInvalid")
        self.assertEqual(genererPoint5("255.555.55.25","255.255.255.0","2","1"),"IpInvalid")

    def testMaskInvalid(self):
        self.assertEqual(genererPoint5("192.168.1.65","255.0.255.0","2","1"), "MaskInvalid")
        self.assertEqual(genererPoint5("192.168.1.65","255.255.0","2","1"), "MaskInvalid")
        self.assertEqual(genererPoint5("192.168.1.65","sdfs","2","1"), "MaskInvalid")
        self.assertEqual(genererPoint5("192.168.1.65","255.255.127.0","2","1"), "MaskInvalid")
        self.assertEqual(genererPoint5("192.168.1.65","255.255.0.0.0","2","1"), "MaskInvalid")

    def testNbSubnetsInvalid(self):
        self.assertEqual(genererPoint5("192.168.1.65","255.255.255.0","-8","1"), "NbSubnetsInvalid")
        self.assertEqual(genererPoint5("192.168.1.65","255.255.255.0","qdfv","1"), "NbSubnetsInvalid")
        self.assertEqual(genererPoint5("192.168.1.65","255.255.255.0","1","1"), "NbSubnetsInvalid")

    def testNbHostsInvalid(self):
        self.assertEqual(genererPoint5("192.168.1.65","255.255.255.0","2","-8"), "NbHostsInvalid")
        self.assertEqual(genererPoint5("192.168.1.65","255.255.255.0","2","qdfv"), "NbHostsInvalid")

    def test(self):
        self.assertEqual(genererPoint5("192.168.1.65","255.255.255.0","2","5"), "Le nombre d'hôte total avec l'IP et le masque de départ est de 254 machines.\n\n" +
        "La découpe classique est possible car :\n\n" +
        "Il peut y avoir maximum 126 machines par sous-réseaux sur base du nombre de sous-réseaux.\n\n" +
        "Il peut y avoir maximum 32 sous-réseaux sur base du nombre d'hôtes par sous-réseaux.\n\n")
        self.assertEqual(genererPoint5("192.168.1.65","255.255.255.0","5","31"), "Le nombre d'hôte total avec l'IP et le masque de départ est de 254 machines.\n\n" +
        "La découpe classique n'est pas possible car :\n\n" +
        "Il peut y avoir maximum 30 machines par sous-réseaux sur base du nombre de sous-réseaux.\n\n" +
        "Il peut y avoir maximum 4 sous-réseaux sur base du nombre d'hôtes par sous-réseaux.\n\n")
        self.assertEqual(genererPoint5("192.168.1.65","255.255.255.0","130","5"), "Le nombre d'hôte total avec l'IP et le masque de départ est de 254 machines.\n\n" +
        "La découpe classique n'est pas possible car :\n\n" +
        "La découpe classique n'est pas possible sur base du nombre de sous-réseaux.\n\n" +
        "Il peut y avoir maximum 32 sous-réseaux sur base du nombre d'hôtes par sous-réseaux.\n\n")
        self.assertEqual(genererPoint5("192.168.1.65","255.255.255.0","2","130"), "Le nombre d'hôte total avec l'IP et le masque de départ est de 254 machines.\n\n" +
        "La découpe classique n'est pas possible car :\n\n" +
        "Il peut y avoir maximum 126 machines par sous-réseaux sur base du nombre de sous-réseaux.\n\n" +
        "La découpe classique n'est pas possible sur base du nombre d'hôtes par sous-réseaux.\n\n")
        self.assertEqual(genererPoint5("192.168.1.65","255.255.255.0","130","130"), "Le nombre d'hôte total avec l'IP et le masque de départ est de 254 machines.\n\n" +
        "La découpe classique n'est pas possible car :\n\n" +
        "La découpe classique n'est pas possible sur base du nombre de sous-réseaux.\n\n" +
        "La découpe classique n'est pas possible sur base du nombre d'hôtes par sous-réseaux.\n\n")
        
if __name__ == '__main__':
    unittest.main()