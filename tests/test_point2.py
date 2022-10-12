import unittest
import sys
import os

#permettant l'import
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from model.point2 import genererPoint2

class Test(unittest.TestCase):

    def testIpInvalid(self):
        self.assertEqual(genererPoint2("256.55.55.25","255.255.255.0"),"IpInvalid")
        self.assertEqual(genererPoint2("255.55.55.","255.255.255.0"),"IpInvalid")
        self.assertEqual(genererPoint2("255.55..25","255.255.255.0"),"IpInvalid")
        self.assertEqual(genererPoint2("255.555.55.25","255.255.255.0"),"IpInvalid")

    def testMaskInvalid(self):
        self.assertEqual(genererPoint2("192.168.1.65","255.0.255.0"), "MaskInvalid")
        self.assertEqual(genererPoint2("192.168.1.65","255.255.0"), "MaskInvalid")
        self.assertEqual(genererPoint2("192.168.1.65","sdfs"), "MaskInvalid")
        self.assertEqual(genererPoint2("192.168.1.65","255.255.127.0"), "MaskInvalid")
        self.assertEqual(genererPoint2("192.168.1.65","255.255.0.0.0"), "MaskInvalid")

    def testMaskInvalidGlobal(self):
        self.assertEqual(genererPoint2("192.168.1.65","255.255.0.0"), "MaskInvalidGlobal")
        self.assertEqual(genererPoint2("152.168.1.65","255.0.0.0"), "MaskInvalidGlobal")

    def testReserve(self):
        self.assertEqual(genererPoint2("0.25.55.56","255.255.255.0"),'On ne peut pas utiliser cette adresse IP \ncar elle fait partie des adresses réservés')
        self.assertEqual(genererPoint2("0.255.255.255","255.255.255.0"),'On ne peut pas utiliser cette adresse IP \ncar elle fait partie des adresses réservés')
        self.assertEqual(genererPoint2("127.58.96.68","255.255.255.0"),'On ne peut pas utiliser cette adresse IP \ncar elle fait partie des adresses réservés')
        self.assertEqual(genererPoint2("127.78.96.36","255.255.255.0"),'On ne peut pas utiliser cette adresse IP \ncar elle fait partie des adresses réservés')

    def testClassD(self):
        self.assertEqual(genererPoint2("224.23.12.71","255.255.255.0"),'On ne peut pas utiliser cette adresse IP \ncar elle fait partie de la classe D') 
        self.assertEqual(genererPoint2("236.24.35.85","255.255.255.0"),'On ne peut pas utiliser cette adresse IP \ncar elle fait partie de la classe D') 
        self.assertEqual(genererPoint2("225.23.12.71","255.255.255.0"),'On ne peut pas utiliser cette adresse IP \ncar elle fait partie de la classe D') 
        self.assertEqual(genererPoint2("231.23.12.71","255.255.255.0"),'On ne peut pas utiliser cette adresse IP \ncar elle fait partie de la classe D') 
        self.assertEqual(genererPoint2("235.23.12.71","255.255.255.0"),'On ne peut pas utiliser cette adresse IP \ncar elle fait partie de la classe D') 
        self.assertEqual(genererPoint2("239.23.12.71","255.255.255.0"),'On ne peut pas utiliser cette adresse IP \ncar elle fait partie de la classe D')
        
    def testClassE(self):
        self.assertEqual(genererPoint2("240.23.12.71","255.255.255.0"),'On ne peut pas utiliser cette adresse IP \ncar elle fait partie de la classe E') 
        self.assertEqual(genererPoint2("245.24.35.85","255.255.255.0"),'On ne peut pas utiliser cette adresse IP \ncar elle fait partie de la classe E') 
        self.assertEqual(genererPoint2("250.23.12.71","255.255.255.0"),'On ne peut pas utiliser cette adresse IP \ncar elle fait partie de la classe E') 
        self.assertEqual(genererPoint2("255.23.12.71","255.255.255.0"),'On ne peut pas utiliser cette adresse IP \ncar elle fait partie de la classe E') 
        self.assertEqual(genererPoint2("242.23.12.71","255.255.255.0"),'On ne peut pas utiliser cette adresse IP \ncar elle fait partie de la classe E') 
        self.assertEqual(genererPoint2("254.23.12.71","255.255.255.0"),'On ne peut pas utiliser cette adresse IP \ncar elle fait partie de la classe E')

    def testSucces(self):
        self.assertEqual(genererPoint2("192.168.1.65","255.255.255.0"),"Adresse de réseau : 192.168.1.0\nAdresse de broadcast : 192.168.1.255\n")
        self.assertEqual(genererPoint2("192.168.1.65","255.255.255.128"),"Adresse de réseau : 192.168.1.0\nAdresse de broadcast : 192.168.1.255\nAdresse de sous-réseau : 192.168.1.0\nAdresse de broadcast du sous-réseau : \n192.168.1.127\n")
        
        
if __name__ == '__main__':
    unittest.main()