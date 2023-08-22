#------------------------------DEATLII------------------------------

#! Autor: DAVID Carciumaru
#! Ajutor: Chat GPT
#! Documentatia probabil e pe pip
#! Versiune: 1.2
#! Versiunea aceasta nu este cea mai stabila !
#! Versiunea python: 3.11
#! Contact: davidcarciumaru21@gmail.com

#------------------------------IMPORTURI------------------------------

import random
from colorama import Fore, Style
import pandas as pd

#------------------------------DATE------------------------------

judete = {
    "Alba": "01", "Arad": "02", "Arges": "03", "Bacau": "04", "Bihor": "05", "Bistrita Nasaud": "06",
    "Botosani": "07", "Brasov": "08", "Braila": "09", "Buzau": "10", "Caras Severin": "11", "Cluj": "12",
    "Constanta": "13", "Covasna": "14", "Dambovita": "15", "Dolj": "16", "Galati": "17", "Gorj": "18",
    "Harghita": "19", "Hunedoara": "20", "Ialomita": "21", "Iasi": "22", "Ilfov": "23", "Maramures": "24",
    "Mehedinti": "25", "Mures": "26", "Neamt": "27", "Olt": "28", "Prahova": "29", "Satu Mare": "30",
    "Salaj": "31", "Sibiu": "32", "Suceava": "33", "Teleorman": "34", "Timis": "35", "Tulcea": "36",
    "Vaslui": "37", "Valcea": "38", "Vrancea": "39", "Bucuresti sectorul 1": "40", "Bucuresti sectorul 2": "41",
    "Bucuresti sectorul 3": "42", "Bucuresti sectorul 4": "43", "Bucuresti sectorul 5": "44",
    "Bucuresti sectorul 6": "45"
}

listSecventaVerificare = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]

genuri = [1, 2, 3, 4, 5, 6]

#------------------------------CLASA CU ERORI------------------------------

class CnpModuleErrors(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(f'{Fore.RED}{self.message}{Style.RESET_ALL}')

#------------------------------CLASA CNP------------------------------

class Cnp:

    """Aceasta clasa creaza un cod cnp, ce contine mai multe funtii inportante
    ce te pot ajuta la folosirea acestui modul, daca vreti sa modificati
    codul adaugati creaditul pentru ajutorul initial adica eu!!!
    """

    __version__ = 1.0
    __name__ = "cnpGenerator"

#-----------------DATE DIN CLASA-----------------

    global instante
    instante = []

    def __init__(self, gen, anul, luna, ziua, judet):
        instante.append(self)
        self.gen = gen
        self.anul = anul
        self.luna = luna
        self.ziua = ziua
        self.judet = judet

        self.init()
        
#-----------------EXCUTARE FUNCTIILOR NECESARE-----------------

    def init(self):
        self.setNumarSecventa()
        self.setNumarGen()
        self.region()

#-----------------DEFINIREA FUNCTIILOR PRINCIPALE-----------------

    def setNumarGen(self):
        if int(self.anul) >= 2000 and int(self.anul) <= 2099:
            if self.gen == "Masculin" or self.gen == "M":
                self.gen = 5
            elif self.gen == "Feminin" or self.gen == "F":
                self.gen = 6
        elif int(self.anul) >= 1900 and int(self.anul) <= 1999:
            if self.gen == "Masculin" or self.gen == "M":
                self.gen = 1
            elif self.gen == "Feminin" or self.gen == "F":
                self.gen = 2
        elif int(self.anul) >= 1800 and int(self.anul) <= 1899:
            if self.gen == "Masculin" or self.gen == "M":
                self.gen = 3
            elif self.gen == "Feminin" or self.gen == "F":
                self.gen = 4
        else:
            raise CnpModuleErrors("INCORRECT GENDER ERROR IN THE INIT() !!!\n Please be sure the gender" 
                            " is 'M', 'Masculin' or'F', 'Feminin',\n verify the code again"
                            " cand be sure it is like in those"
                            " examples.\n Else read the documentation and you will find your answer !")
    
    def region(self):
        if self.judet in judete:
            self.judet = judete[self.judet]
        else:
            raise CnpModuleErrors("INCORRECT REGION IN THE INIT() !!!\n Please be sure your region is"
                                  " in the 'judete' dict in the\n source code, GitHub, or pip !")

    def setNumarSecventa(self):
        self.numarSecventa = random.randint(1, 999)
        if len(str(self.numarSecventa)) == 1:
            self.numarSecventa = "0" + "0" + str(self.numarSecventa)
        elif len(str(self.numarSecventa)) == 2:
            self.numarSecventa = "0" + str(self.numarSecventa)
        else:
            self.numarSecventa = str(self.numarSecventa)
    
#-----------------CIFRA DE CONTROL-----------------

    def setCifraDeControl(self):
        SumaCnpFaraCifra = []
        cnpFaraCifraDeVerificare = self.getCnpWithoutCifraDeVerificare() 
        for _ in range(len(listSecventaVerificare)):
            CnpSum = listSecventaVerificare[_] * int(cnpFaraCifraDeVerificare[_])
            SumaCnpFaraCifra.append(CnpSum)
        numarDeInpartint = sum(SumaCnpFaraCifra)
        return numarDeInpartint % 11

    def getCnpWithoutCifraDeVerificare(self):
        return str(self.gen) + self.anul[2:] + self.luna + self.ziua + self.judet + self.numarSecventa

    def createCnp(self):
        self.cnp = str(self.gen) + self.anul[2:] + self.luna + self.ziua + self.judet + self.numarSecventa + str(self.setCifraDeControl())

#------------------------------CLASA CNP TOOLS------------------------------

class CnpTools:

    def __init__(self):
        pass

    #-----------------FUNCTIE PENTRU GASIRII CIFREI DE CONTROL-----------------

    def getCifraControl(self, cnp):
        self.cnp = cnp

        try:
            SumaCnpFaraCifra = []
            cnpFaraCifraDeVerficare = str(self.cnp)
            for _ in range(len(listSecventaVerificare)):
                CnpSum = listSecventaVerificare[_] * int(cnpFaraCifraDeVerficare[_])
                SumaCnpFaraCifra.append(CnpSum)
                numarDeInpartint = sum(SumaCnpFaraCifra)
            return numarDeInpartint % 11
        except IndexError:
            raise CnpModuleErrors(f"THE CNP ISN'T BIG ENOUGH !!!\n The CNP length must be 11 but yours is "
                                  f"{Fore.RED}'{self.cnp}'{Style.RESET_ALL} only")

#-----------------ZONA CE CREAZA DATAFRAME-URI-----------------

    def dataFrameCnp(self):
        Gen = []
        Anul = []
        Luna = []
        Ziua = []
        Judet = []
        Cnp = []
        for _ in instante: 
            Gen.append(_.gen)
            Anul.append(_.anul)
            Luna.append(_.luna)
            Ziua.append(_.ziua)
            Judet.append(_.judet)
            Cnp.append(_.cnp)

        data = {
            "Gen": Gen,
            "Anul": Anul,
            "Luna": Luna,
            "Ziua": Ziua,
            "Judet": Judet,
            "Cnp": Cnp,
        }

        df = pd.DataFrame(data)
        print(df)

    def dataToXcel(self, filePath):
        Gen = []
        Anul = []
        Luna = []
        Ziua = []
        Judet = []
        Cnp = []
        for _ in instante: 
            Gen.append(_.gen)
            Anul.append(_.anul)
            Luna.append(_.luna)
            Ziua.append(_.ziua)
            Judet.append(_.judet)
            Cnp.append(_.cnp)

        data = {
            "Gen": Gen,
            "Anul": Anul,
            "Luna": Luna,
            "Ziua": Ziua,
            "Judet": Judet,
            "Cnp": Cnp,
        }

        df = pd.DataFrame(data)
        df.to_excel(filePath)

#-----------------FUNCTIA CARE VERIFICA DACA CIFRA DE CONTROL ESTE CREATA CORECT-----------------
    
    def verifyCnp(self, cnpVer, cnpFull):
        self.cnpVer = cnpVer
        self.cnpFull = cnpFull

        try:
            SumaCnpFaraCifra = []
            cnpFaraCifraDeVerficare = str(self.cnp)
            for _ in range(len(listSecventaVerificare)):
                CnpSum = listSecventaVerificare[_] * int(cnpFaraCifraDeVerficare[_])
                SumaCnpFaraCifra.append(CnpSum)
                numarDeInpartint = sum(SumaCnpFaraCifra)
                self.CifraVer = numarDeInpartint % 11
        except IndexError:
            raise CnpModuleErrors(f"THE CNP ISN'T BIG ENOUGH !!!\n The CNP length must be 11 but yours is "
                                  f"{Fore.RED}'{self.cnp}'{Style.RESET_ALL} only")
        
        self.cnpVer = str(cnpVer) + str(self.CifraVer)
    
        if str(self.cnpVer) == str(self.cnpFull):
            return True
        else:
            return False
        
#-----------------FUNCTIA CE VERIFICA DACA UN GENUL, DATA NASTERI SI JUDETUL UNUI BULETIN SUNT VALABILE-----------------

    def isCnp(self, gen, an, luna, zi, judet):
        verificari = []
        lucruriFacute = []
        self.gen = gen
        if str(self.gen)[0] in str(genuri):
            verificari.append(True)
            print(*verificari)
        else:
            verificari.append(False)
            print(*verificari)
            
        
        year = int(an) 
        month = int(luna)
        day = int(zi)

        if year < 1:
            verificari.append(False)
            lucruriFacute.append(1)
            print(*verificari)
        
        if month < 1 or month > 12:
            verificari.append(False)
            lucruriFacute.append(1)
            print(*verificari)
        
        daysInMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            daysInMonth[2] = 29

        if day < 1 or day > daysInMonth[month]:
            verificari.append(False)
            lucruriFacute.append(1)
            print(*verificari)

        if len(lucruriFacute) == 0:
            verificari.append(True)
            print(*verificari)

        if int(judet) >= 0 and int(judet) <= 45:
            verificari.append(True)
            print(*verificari)

        if verificari[0] == True and verificari[1] == True and verificari[2] == True:
            return True
        else:
            return False

#cnp1 = Cnp("M", "2009", "12", "21", "Valcea")
#cnp2 = Cnp("F", "1983", "11", "21", "Arges")
#cnp1.createCnp()
#cnp2.createCnp()
#print(cnp1.cnp)
##print(cnp2.cnp)
#cnpTool = CnpTools()
#print(cnpTool.getCifraControl("283112103001"))
#cnpTool.dataFrameCnp()
#print(cnpTool.verifyCnp(283112103001, 2831121030018))
#a = cnpTool.isCnp("2", "1983", "11", "21", "03")
#print(a)