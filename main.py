# FRITZ RALUCA-MIHAELA
# GRUPA 243
# Problema de cautare (un mesaj...)

"""
In drum spre scoala un copilas a auzit doi copii mai mari vorbind despre
un coleg si prieten bun de-al lui. Cei doi voiau sa-i faca o farsa rautacioasa
in prima pauza. Copilasul insa a ajuns dupa ce incepuse ora si a trebuit sa se
 aseze direct in banca, fara a-si putea avertiza colegul de primejdie.
 Din fericire i-a venit in minte sa-i trimita din coleg in coleg un bilet
 cu un mesaj in care sa-l atentioneze despre farsa

 Copii sunt asezati in banci de cate doua persoane. Bancile sunt dispuse in trei coloane astfel:
|===================================================|
|---------------------------------------------------|
|    a | a    ||      a | a     ||      a | a       |
|    ------   ---     ------    ---     ------      |
|    a | a    ||      a | a     ||      a | a       |
|    ------   ---     ------    ---     ------      |
|    .....    ||      .....     ||      .....       |
|    ------   ---     ------    ---     ------      |
|    a | a    ||      a | a     ||      a | a       |
|    ------   ---     ------    ---     ------      |
|    a | a    ||      a | a     ||      a | a       |
|---------------------------------------------------|
|===================================================|

 Un copil poate da fara probleme biletul catre colegul de banca, la fel neobservat de catre
 profesor poate da biletul catre colegii din fata sau din spatele lui, insa nu si in diagonala,
 deoarece, intinzanduse peste banca ar atrage privirea profesorului.
Considerand fragmentul de clasa de mai jos:
 a | b
 ------
 c | d

Elevul a poate trimite biletul doar catre b sau c

Probleme apar din faptul ca unele locuri in banci pot fi libere, dar si din faptul ca o serie
de colegi sunt suparati intre ei si nu-si vorbesc, deci nici nu ar trimite biletul
(supararea este reciproca).
De asemenea, trecerea biletelului de pe un rand pe altul este mai anevoioasa,
 deoarece poate fi vazut foarte usor de catre profesor, de aceea singurele banci intre care se
 poate face transferul sunt penultimele si ultimele de pe fiecare rand.

Copilul vrea sa scrie pe bilet drumul pe care trebuie sa-l parcurga, de la un
coleg la altul, pentru a fi sigur ca nu se rataceste prin clasa si nu mai ajunge la prietenul sau
pana la inceputul pauzei.

Se considera prin conventie ca:
- fiecare copil este identificat unic prin numele sau.
- niciun copil nu se numeste 'suparati' sau 'liber'
- locurile libere sunt marcate prin identificatorul 'liber'

Formatul fisierului de intrare este urmatorul.
Pe primele linii din fisier se precizeaza asezarea in banci.
Fiecare linie cuprinde 6 nume (numele sunt formate doar din litere).
Primii doi identificatori corespund primei coloane de banci,
urmatorii doi identificatori coloanei din mijloc, si utltimii doi, ultimei coloane
de banci.

Dupa ce se termina liniile cu asezare in banci,
apare un rand cu identificatorul suparati.
Sub acest rand, sunt trecuti cate doi elevi (numele lor) care sunt suparati intre ei.

Exemplu de fisier:

ionel alina teo eliza carmen monica
george diana bob liber nadia mihai
liber costin anda bogdan dora marin
luiza simona dana cristian tamara dragos
mihnea razvan radu patricia gigel elena
liber andrei oana victor liber dorel
viorel alex ela nicoleta maria gabi
suparati
george ionel
ela nicoleta
victor oana
teo eliza
teo luiza
elena dragos
alina dragos
mesaj: ionel -> dragos

Exemplu de drum din fisierul de iesire:

ionel > alina v diana v costin v simona v razvan v andrei >> oana ^ radu > patricia v
victor v nicoleta >> maria > gabi ^ dorel ^ elena < gigel ^ tamara > dragos

In urma rularii se va afisa drumul parcurs, in ordine cronologica.
Daca biletelul merge in cadrul aceluiasi rand, deci catre un coleg de banca,
in stanga, se va afisa <, daca merge in dreapta, se va afisa >.
Daca biletelul merge spre spatele clasei, intre copiii care transmit biletul se va
afisa un v (pe post de sagetica in jos), iar daca merge spre fata clasei, se va afisa ^ pe post de sagetica in sus.
Cand biletul se deplaseaza spre stanga de pe un rand de banci pe altul, se va afisa <<, iar spre dreapta: >>.
"""
# Citire fisiere de intrare / iesire de la tastatura + NSOL + timpul de timeout

# pathIn = input("path fisierIn: ")
# fisierIn = open(pathIn,'r')
# pathOut = input("path fisierOut: ")
# fisierOut = open(pathOut,'w')
# NSOL = int(input("NSOL= "))
# timeout = int(input(Timp de timeout= "))
########################################### CITIRE DATE INPUT ########################################
# Citire folosita pentru testing
fisierIn = open('fisier.in','r')
fisierOut = open('fisier.out','w')

# citire din fisier + parsare fisier de input care respecta formatul cerut in enunt
linii = fisierIn.readlines()

numarRanduri = 0
numarColoane = 0
liniiCopii = []

# salvez pozitiile copiilor in banci cu ajutorul unor coordonate de forma (rand, coloana)

coordCopii = {} # {nume, (rand, coloana)} => lista coordonate copii, se afla dupa nume
# ex:
#   ionel     0,0
#   alina     0,1
#   teo       0,2
#   alina     0,3
numeCopii = {} # {(rand, coloana), nume} => lista nume copii, se afla dupa coord
# ex:
#   0,0       ionel
#   0,1       alina
#   0,2       teo
#   0,3       alina

copiiSuparati = {}

copilStart = ""
copilScop = ""

for linie in linii:
    linieSplit = linie.strip("\n").split()
    lengthLinie = len(linieSplit)
    # memorare pozitii copii
    if lengthLinie == 6:
        for pozitie in range(len(linieSplit)):
            coordCopii[linieSplit[pozitie]] = (numarRanduri, pozitie)
            numeCopii[(numarRanduri, pozitie)] = linieSplit[pozitie]
        numarRanduri += 1
        numarColoane += 1
    # memorare copii suparati
    elif lengthLinie==2:
        if linieSplit[0] not in copiiSuparati:
            # daca copilul nr 1 nu se afla in lista de copii suparati, il adaugam
            copiiSuparati[linieSplit[0]] = []
        if linieSplit[1] not in copiiSuparati:
            # daca copilul nr 2 nu se afla in lista de copii suparati, il adaugam
            copiiSuparati[linieSplit[1]] = []
        # adaugam fiecare copil in lista de copiiSuparati ai celuilalt
        copiiSuparati[linieSplit[0]].append(linieSplit[1])
        copiiSuparati[linieSplit[1]].append(linieSplit[0])
    # memorare nodStart si nodScop
    elif linieSplit[0] == "mesaj:":
        copilStart = linieSplit[1]
        copilScop = linieSplit[3]

print(numeCopii)
# Clase ajutatoare pentru folosirea alogirtmului A*: NodParcurgere, Nod, Problema

# In exemplul dat la laborator s-a integrat clasa Nod in clasa NodParcurgere prin a introduce info si h in NodParcurgere,
# Pentru evitarea confuziei, am ales sa folosesc aceeasi abordare, de aceea urmatoarea secventa de cod este comentata:

################################################# CLASA NOD  ##############################################

# # Clasa Nod, cu proprietatile:
# #   - info despre nod
# #   - h^
# #   In cazul de fata am ales: numele copilului(pentru nodul initial este 'ionel' iar pentru cel final este 'dragos'
# #   si h^, pe care am notat-o cu h_ este estimarea costului facuta pentruu nod, de la nodul curent la nodul scop
#
# class Nod:
#     def __init__(self, copil, h_):
#         self.copil = copil
#         self.h_ = h_
#
#     def __str__(self):
#         return f"nod: {self.copil} \n" \
#                f"h^: {self.h_} \n"
#
#     def __repr__(self):
#         return f"nod: {self.copil} \n" \
#                f"h^: {self.h_} \n"

########################################### CLASA NOD PARCURGERE ########################################

# Clasa NodParcurgere, cu proprietatile:
#   nod - referinta catre nodul corespunzator din graf
            # #   - info despre nod
            # #   - h^
            # #   In cazul de fata am ales: numele copilului(pentru nodul initial este 'ionel' iar pentru cel final este 'dragos'
            # #   si h^, pe care am notat-o cu h_ este estimarea costului facuta pentruu nod, de la nodul curent la nodul scop
#   parinte - referinta catre nodul-parinte din arbore. Pentru radacina arborelui, parintele va avea valoarea None.
#   g - costul de la radacina arborelui pana la nodul curent
#   f - costul estimat pentru drumul care porneste de la radacina si trece prin nodul curent
#   expandat - o proprietate optionala (booleana). O putem folosi in locul listei closed si urmatoarele metode:
#   expandeaza - care va returna o lista cu toti succesorii posibili ai nodului curent
#   test_scop -care testeaza daca nodul e nod scop


class NodParcurgere:
    def __init__(self, copil, cost, h_, parinte=None, directie=None):
        self.copil = copil
        self.parinte = parinte # daca este radacina => None
        self.g = cost
        self.h_ = h_
        # f = g + h
        self.f = self.g + self.h_

        # in cazul problemei noastre, avem nevoie de o directie din care se vine, care poate fi una din urmatoarele:
        #               '^'
        #               '>'
        #               '<'
        #               'v'
        #               '>>'
        #               '<'
        # astfel vom introduce inca o proprietate numita directie care va fi setata ulterior
        self.directie = directie

    def obtineDrum(self):
        drum = [self.copil]
        nod = self
        while nod.parinte is not None:
            drum.insert(0, nod.parinte.copil)
            nod = nod.parinte
        return drum

    def afisDrum(self):
        drum = self.obtineDrum()
        for nod in drum:
            print(f"{nod.copil} {nod.directie} ")
        return len(drum)

    def outputDrum(self):
        drum = self.obtineDrum()
        for nod in drum:
            fisierOut.write(f"{nod.copil} ")
            if nod.directie is not None:
                fisierOut.write(f"{nod.directie} ")

    #  pornind de la exemplul din laborator => verificam daca un nod face parte din drum
    def contineInDrum(self, nodNou):
        nodCurent = self
        while nodCurent is not None:
            if nodNou == nodCurent.copil:
                return True
            nodCurent = nodCurent.parinte
            return False

    # functia de generare a succesorilor
    # generam lista tuturor succesorilor posibili al nodului curent
    def expandeaza(self, nodScop, tipEuristica="euristica banala"):
        global numarRanduri
        global copiiSuparati
        # initializam lista succesorilor cu multimea vida
        succesori = []
        # preluam coordonatele copilului
        pozRand, pozCol = coordCopii[self.copil]

        # selectam toti vecinii:
        # VECINUL DE SUS ^
        # testam daca exista vecinul de sus
        if pozRand - 1 >= 0:
            # salvam numele copilului
            numeSuccesor = numeCopii[(pozRand - 1, pozCol)]
            # testam daca acest succesor este certat cu copilul curent sau daca este liber
            if not self.esteLiberSauSuntSuparati(self, numeSuccesor):
                # creez nodul si calculez h_
                succesor = NodParcurgere(numeSuccesor, self.g +1, self.g + 1 + self.calculeazaH_(self, numeSuccesor, nodScop))
                # setez directia catre acest succesor
                succesor.directie = "^"
                # adaug succesorul in lista succesorilor
                succesori.append(succesor)
        # VECINUL DE JOS v
        # testam daca exista vecinul de jos -> SEPARAT ULTIMA SI PENULTIMA BANCA pozRand +2  si pozRand+1 == numarRnaduri
        # Daca suntem pe penultimul sau ultimul rand
        if pozRand + 1 == numarRanduri or pozRand + 2 == numarRanduri:
            # verificam daca este intr-o coloana impara sau para => ne mutam la dreapta sau la stanga
            # daca este coloana impara => ne mutam la dreapta => trebuie sa verificam daca exista un alt set de
            # banci la dreapta
            if (pozCol % 2 == 1) and (pozCol != numarColoane - 1 ):
                # salvam numele copilului
                numeSuccesor = numeCopii[(pozRand - 1, pozCol)]
                # testam daca acest succesor este certat cu copilul curent sau daca este liber
                if not self.esteLiberSauSuntSuparati(self, numeSuccesor):
                    # creez nodul si calculez h_
                    succesor = NodParcurgere(numeSuccesor, self.g + 1,
                                             self.g + 1 + self.calculeazaH_(self, numeSuccesor, nodScop))
                    # setez directia catre acest succesor
                    succesor.directie = ">>"
                    # adaug succesorul in lista succesorilor
                    succesori.append(succesor)
             # daca este coloana para => ne mutam la stanga  => trebuie sa verificam daca exista un alt set de
             # banci la stanga
            elif (pozCol % 2 == 0) and (pozCol -1 > -1):
                 # salvam numele copilului
                 numeSuccesor = numeCopii[(pozRand - 1, pozCol)]
                 # testam daca acest succesor este certat cu copilul curent sau daca este liber
                 if not self.esteLiberSauSuntSuparati(self, numeSuccesor):
                     # creez nodul si calculez h_
                     succesor = NodParcurgere(numeSuccesor, self.g + 1,
                                              self.g + 1 + self.calculeazaH_(self, numeSuccesor, nodScop))
                     # setez directia catre acest succesor
                     succesor.directie = "<<"
                     # adaug succesorul in lista succesorilor
                     succesori.append(succesor)
        elif pozRand + 1 < numarRanduri:
            numeSuccesor = numeCopii[(pozRand + 1, pozCol)]
            # testam daca acest succesor este certat cu copilul curent sau daca este liber
            if not self.esteLiberSauSuntSuparati(numeSuccesor):
                # creez nodul si calculez h_
                succesor = NodParcurgere(numeSuccesor, self.g + 1,
                                         self.g + 1 + self.calculeazaH_(self, numeSuccesor, nodScop))
                # setez directia catre acest succesor
                succesor.directie = "v"
                # adaug succesorul in lista succesorilor
                succesori.append(succesor)
        # VECINUL DIN STANGA
        # testam daca exista vecinul din stanga
        if pozRand % 2 == 1:
            numeSuccesor = numeCopii[(pozRand, pozCol - 1)]
            # testam daca acest succesor este certat cu copilul curent sau daca este liber
            if not self.esteLiberSauSuntSuparati(self, numeSuccesor):
                # creez nodul si calculez h_
                succesor = NodParcurgere(numeSuccesor, self.g + 1,
                                         self.g + 1 + self.calculeazaH_(self, numeSuccesor, nodScop))
                # setez directia catre acest succesor
                succesor.directie = "<"
                # adaug succesorul in lista succesorilor
                succesori.append(succesor)

        # VECINUL DIN DREAPTA
        # testam daca exista vecinul din dreapta
        if pozRand % 2 == 0:
            numeSuccesor = numeCopii[(pozRand, pozCol + 1)]
            # testam daca acest succesor este certat cu copilul curent sau daca este liber
            if not self.esteLiberSauSuntSuparati(numeSuccesor):
                # creez nodul si calculez h_
                succesor = NodParcurgere(numeSuccesor, self.g + 1,
                                         self.g + 1 + self.calculeazaH_(numeSuccesor, nodScop))
                # setez directia catre acest succesor
                succesor.directie = ">"
                # adaug succesorul in lista succesorilor
                succesori.append(succesor)
        return succesori

    # calculatera costului pentru o mutare
    def calculeazaH_(self, copil, nodScop, tipEuristica="euristica banala"):
        # euristica banala = daca este nodScop => 0, daca nu este => 1
        if tipEuristica == "euristica banala":
            if copil != nodScop.copil:
                return 1
            return 0
        # eursitica admisibila 1=
        # elif tipEuristica =="euristica admisibila 1":
        # elif tipEuristica == "euristica admisibila 2":
        # elif tipEuristica == "euristica neadmisibila":


    def esteLiberSauSuntSuparati(self, copil):
        if self.esteLocLiber(copil) or self.copiiSuparati(copil):
            return True
        return False

    def esteLocLiber(self, copil):
        # daca locul este liber
        if copil == "liber":
            return True
        return False

    def copiiSuparati(self, copil):
        # daca cei 2 copii sunt suparati
        global copiiSuparati
        if (self.copil in copiiSuparati[copil]) and (copil in copiiSuparati[self.copil]):
            return True
        return False

    # test scop pe care un agent il ploate aplica unei singure descrieri de stare pentru a determina daca ea este o
    # stare de tip scop => in cazul nostru, starea de tip scop == copilScop

    def testScop(self, nodScop):
        return self.copil == nodScop.copil

    def __str__(self):
        f"Nod: {self.copil} \n" \
        f"Cost nodStart -> nodCurent: {self.g} \n" \
        f"Cost estimativ nodCurent -> nodScop: {self.h_} \n" \
        f"Drum = {('->').join(self.obtineDrum())} \n" \
        f"Cost estimat pentru drum: {self.f} \n"

    def __repr__(self):
        return f"Nod: {self.copil} \n" \
               f"Cost nodStart -> nodCurent: {self.g} \n" \
               f"Cost estimativ nodCurent -> nodScop: {self.h_} \n" \
               f"Drum = {('->').join(self.obtineDrum())} \n" \
               f"Cost estimat pentru drum: {self.f} \n"



################################################# PROBLEMA ############################################

# Clasa Graph Problema => contine datele problemei + graful de cautare

class GraphProblema:
    def __init__(self,  nodStart, nodScop):
        self.nodStart = nodStart
        self.nodScop = nodScop

    def a_star(self, tipEuristica="euristica banala"):
        # pentru a nu folosi self.nodStart si self.nodScop am initializat local aceste 2 variabile
        nodStart = self.nodStart
        nodScop = self.nodScop
        # # graf de cautare care contine doar nodStart
        # G = [nodStart]
        # adaugam OPEN + adaugam nodul pentru inceput nodStart in OPEN
        open = [nodStart]
        # aduagam lista CLOSED care este vida
        closed = []
        # esteOpenVida initalizat cu False pentru ca in OPEN se afla nodStart
        esteOpenVida = False
        # daca OPEN ajunge vida => False => ESEC, daca nodCurent ajunge sa fie nodScop => True => Success
        end = False

        while not esteOpenVida:
            # selectez primul nod din lista OPEN  si il scot din OPEN
            nodCurent = open.pop(0)
            # il adaug in CLOSED => nodCurent = nod n
            closed.append(nodCurent)
            # daca nodCurent = nodScop => oprire secutie cu success
            if nodCurent.testScop(nodScop):
                # Success
                end = True
                # write Output
                # nodStart ^/>/v/</>>/<<....>/v/</>>/<</^ nodScop
                drum = nodCurent.outputDrum()
            if not end:
                # extindem nodul n -> obtinem succesorii
                # generam multimea M in care retinem succesorii lui n
                multimeaM = nodCurent.expandeaza(nodScop, tipEuristica="euristica banala")
                for succesor in multimeaM:
                    # verificam daca succesorii din M sunt in OPEN sau in CLOSED (adica daca sunt deja in graful de cautare)
                    # comparam valorile f pentru a retine copilul cu valoare f mai mica
                    # si il scoatem din OPEN si CLOSED pentru a il adauga in OPEN intr-un mod sortat
                    if self.esteInLista(succesor,open):
                        for nod in open:
                            if succesor.copil == nod.copil:
                                if succesor.f >= nod.f:
                                    multimeaM.remove(succesor)
                                else:
                                    open.remove(succesor)
                    elif self.esteInLista(succesor, closed):
                        for nod in closed:
                            if succesor.copil == nod.copil:
                                if succesor.f >= nod.f:
                                    multimeaM.remove(succesor)
                                else:
                                    closed.remove(succesor)
                for succesor in multimeaM:
                    i = 0
                    gasitLoc = False
                    # trecem prin toata lista OPEN pana gasim o locatie unde f-ul succesorului este mai mic ca f-ul nodului
                    # aflat la pozitia i in OPEN.
                    # daca se gaseste, se insereaza in fata acestuia
                    # daca nu se gaseste, se adauga la final
                    for i in range(len(open)):
                        # ordonam in principal dupa f, dar daca f-urile sunt egale, se sorteaza descrescator dupa g
                        # puteam folosi si adaugarea sau modificarea in open direct a nodurilor si sortarea ulterioara
                        # prin open.sort(key=lambda x: (x.f, -x,g) care face exact acelasi lucru
                        if open[i].f > succesor.f or(open[i].f == succesor.f and open[i].g <= succesor.g):
                            gasitLoc =  True
                            break
                    if gasitLoc:
                        open.insert(i, succesor)
                    else:
                        open.append(succesor)
        if not end:
            fisierOut.write("Nu exista solutie")

            #testam daca Open este vida
            # if not open:
            #     esteOpenVida = True

    def esteInLista(self, copil, lista):
        for nod in lista:
            if nod.copil == copil:
                return True
        return False


########################################### SCRIERE DATE OUTPUT ########################################
# afisare output + 4 fisierei de input

nodStart = NodParcurgere(copilStart, 0, 0)
nodScop = NodParcurgere(copilScop, 0, 0)

graphProblema = GraphProblema(nodStart, nodScop)
graphProblema.a_star()


fisierIn.close()
fisierOut.close()





# documentatie
# in README.MD + README.PDF(transformarea MD in PDF)