import unittest
import sys
import os

#permettant l'import
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from model.point3 import genererPoint3

class Test(unittest.TestCase):

    def testIpInvalid(self):
        self.assertEqual(genererPoint3("256.55.55.25","255.255.255.0","192.168.1.65"),"IpInvalid")
        self.assertEqual(genererPoint3("255.55.55.","255.255.255.0","192.168.1.65"),"IpInvalid")
        self.assertEqual(genererPoint3("255.55..25","255.255.255.0","192.168.1.65"),"IpInvalid")
        self.assertEqual(genererPoint3("255.555.55.25","255.255.255.0","192.168.1.65"),"IpInvalid")

    def testMaskInvalid(self):
        self.assertEqual(genererPoint3("192.168.1.65","255.0.255.0","192.168.1.65"), "MaskInvalid")
        self.assertEqual(genererPoint3("192.168.1.65","255.255.0","192.168.1.65"), "MaskInvalid")
        self.assertEqual(genererPoint3("192.168.1.65","sdfs","192.168.1.65"), "MaskInvalid")
        self.assertEqual(genererPoint3("192.168.1.65","255.255.127.0","192.168.1.65"), "MaskInvalid")
        self.assertEqual(genererPoint3("192.168.1.65","255.255.0.0.0","192.168.1.65"), "MaskInvalid")

    def testIpNetworkInvalid(self):
        self.assertEqual(genererPoint3("192.168.1.65","255.255.0.0","192.263.1.1"), "IpNetworkInvalid")
        self.assertEqual(genererPoint3("152.168.1.65","255.0.0.0","qsfv"), "IpNetworkInvalid")

    def testMemeAdress(self):
        self.assertEqual(genererPoint3("192.168.1.65","255.255.0.0","192.168.1.65"), "MemeAdress")
        self.assertEqual(genererPoint3("152.168.1.65","255.0.0.0","152.168.1.65"), "MemeAdress")

    def test(self):
        self.assertEqual(genererPoint3("192.168.1.65","255.255.255.0","192.168.1.0"),"L'adresse IP :192.168.1.65\nappartient bien au réseau :192.168.1.0")
        self.assertEqual(genererPoint3("192.168.1.65","255.255.255.128","192.168.1.152"),"L'adresse IP :192.168.1.65\nn'appartient pas au réseau :192.168.1.152")
        
if __name__ == '__main__':
    unittest.main()