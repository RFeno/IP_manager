import unittest
import sys
import os

#permettant l'import
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from model.point4 import genererPoint4

class Test(unittest.TestCase):

    def testIpInvalid1(self):
        self.assertEqual(genererPoint4("256.55.55.25","255.255.255.0","192.168.1.65","255.255.255.0"),"IpInvalid1")
        self.assertEqual(genererPoint4("255.55.55.","255.255.255.0","192.168.1.65","255.255.255.0"),"IpInvalid1")
        self.assertEqual(genererPoint4("255.55..25","255.255.255.0","192.168.1.65","255.255.255.0"),"IpInvalid1")
        self.assertEqual(genererPoint4("255.555.55.25","255.255.255.0","192.168.1.65","255.255.255.0"),"IpInvalid1")

    def testMaskInvalid1(self):
        self.assertEqual(genererPoint4("192.168.1.65","255.0.255.0","192.168.1.65","255.255.255.0"), "MaskInvalid1")
        self.assertEqual(genererPoint4("192.168.1.65","255.255.0","192.168.1.65","255.255.255.0"), "MaskInvalid1")
        self.assertEqual(genererPoint4("192.168.1.65","sdfs","192.168.1.65","255.255.255.0"), "MaskInvalid1")
        self.assertEqual(genererPoint4("192.168.1.65","255.255.127.0","192.168.1.65","255.255.255.0"), "MaskInvalid1")
        self.assertEqual(genererPoint4("192.168.1.65","255.255.0.0.0","192.168.1.65","255.255.255.0"), "MaskInvalid1")

    def testIpInvalid2(self):
        self.assertEqual(genererPoint4("192.168.1.65","255.255.255.0","256.55.55.25","255.255.255.0"),"IpInvalid2")
        self.assertEqual(genererPoint4("192.168.1.65","255.255.255.0","255.55.55.","255.255.255.0"),"IpInvalid2")
        self.assertEqual(genererPoint4("192.168.1.65","255.255.255.0","255.55..25","255.255.255.0"),"IpInvalid2")
        self.assertEqual(genererPoint4("192.168.1.65","255.255.255.0","255.555.55.25","255.255.255.0"),"IpInvalid2")

    def testMaskInvalid2(self):
        self.assertEqual(genererPoint4("192.168.1.65","255.255.255.0","192.168.1.65","255.0.255.0"), "MaskInvalid2")
        self.assertEqual(genererPoint4("192.168.1.65","255.255.255.0","192.168.1.65","255.255.0"), "MaskInvalid2")
        self.assertEqual(genererPoint4("192.168.1.65","255.255.255.0","192.168.1.65","sdfs"), "MaskInvalid2")
        self.assertEqual(genererPoint4("192.168.1.65","255.255.255.0","192.168.1.65","255.255.127.0"), "MaskInvalid2")
        self.assertEqual(genererPoint4("192.168.1.65","255.255.255.0","192.168.1.65","255.255.0.0.0"), "MaskInvalid2")

    def test(self):
        self.assertEqual(genererPoint4("192.168.1.65","255.255.255.0","192.168.1.68","255.255.255.0"),"\nLa machine 2 considère la machine 1 dans son réseau.\n\nLa machine 1 considère la machine 2 dans son réseau.\n")
        self.assertEqual(genererPoint4("192.168.1.65","255.255.255.0","192.168.1.168","255.255.255.128"),"\nLa machine 2 ne considère pas la machine 1 dans son réseau.\n\nLa machine 1 considère la machine 2 dans son réseau.\n")
        self.assertEqual(genererPoint4("192.168.1.65","255.255.255.128","192.168.1.168","255.255.255.128"),"\nLa machine 2 ne considère pas la machine 1 dans son réseau.\n\nLa machine 1 ne considère pas la machine 2 dans son réseau.\n")
        self.assertEqual(genererPoint4("192.168.1.165","255.255.255.128","192.168.1.68","255.255.255.0"),"\nLa machine 2 considère la machine 1 dans son réseau.\n\nLa machine 1 ne considère pas la machine 2 dans son réseau.\n")
        
if __name__ == '__main__':
    unittest.main()