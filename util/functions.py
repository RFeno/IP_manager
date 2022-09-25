
import re


def verifyIsIpValid(adressIP):
    if not re.search(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", adressIP):
       print(f"L'adresse IP {adressIP} n'est pas valide")
       return False

    bytes = adressIP.split(".")
  
    for ip_byte in bytes:
        if int(ip_byte) < 0 or int(ip_byte) > 255:
            print(f"L'adresse IP {adressIP} n'est pas valide")
            return False
    print(f"L'adresse IP {adressIP} n'est pas valide")
    return True
    