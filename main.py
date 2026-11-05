from random import *
from math import *
from time import sleep
import requests
import json

class Pokemon:

    def __init__(self):
        '''        
        Constructeur
        '''
        self.nom = choice(names)
        self.pv = randint(20,30)
        self.maxpv = self.pv
        self.att = randint(10,15)
        self.defs = randint(8,14)
        self.vit = randint(5,12)
        self.exp = 1
        self.niv = 1
      
    def __str__(self):
        '''
        Role:
            Surcharge de print()
        Params:
            Un objet de type : Pokemon
        Return:
            Quand on print un objet: Pokemon, ses stats s'affichent
        '''
        name = self.nom
        pv = self.pv
        att= self.att
        defs=self.defs
        vit=self.vit
        exp=self.exp
        niv=self.niv
        return name + " a comme stats : " +'\n'+'Point de vie: '+str(pv)+'\n'+'Attaque: '+str(att)+'\n'+'Defense: '+str(defs)+'\n'+'Vitesse: '+str(vit)+'\n'+'Experience: '+str(exp)+'\n'+'Niveau: '+str(niv) +'\n'
    
    def MaN(self):
        '''
        Role:
            Verifie et gere la mise a niveau
        Params:
            Un objet de type : Pokemon
        Return:
            Quand on print un Pokemon, ses stats s'affichent
        '''
        if self.exp >= 3* self.niv:
            self.maxpv += randint(1,3)
            self.att += randint(1,3)
            self.defs += randint(1,3)
            self.vit += randint(1,3)
            self.exp = 1
            self.niv += 1
        else:
            pass

    def Combat(self, pk2):
        '''
        Role:
            Gere le systeme de combat
        Params:
            Deux objets de type : Pokemon
        Return:
            Le cours du combat
            Le vainqueur 
        '''
        if self.pv<=0:
            return self.nom +" n'as pas assez de point de vie pour combatre"
        elif pk2.pv<=0:
            return pk2.nom +" n'as pas assez de point de vie pour combatre"
        else:
            pass
            
        #Etape 1 (ordre attaque)
        att = Pokemon.Combattant(self,pk2) #Premier attaquant

        #Etape 2 (calcul de degat)

        continuer = True
        while continuer:
            if att == self.nom and Pokemon.Attaque(self) > 0:
                degat = max(0,Pokemon.Attaque(self) -pk2.defs)
                degat = floor(degat) #arrondissement au int inferieur
                #Amelioration (BONUS)
                activation1 = randint(0,100)
                if activation1 <= 5:
                    degat = degat*1.5
                    print(f"{self.nom} va infliger un coup critique (5% de chance)")

                degat = int(degat)
                activation2 = randint(0,100)
                if activation2 >5:
                    pk2.pv -= degat
                    print(f'{pk2.nom} a subit {degat} de degat et lui reste {pk2.pv}.\n')
                else:
                    print(f"{pk2.nom} à esquiver l'attaque (5% de chance)\n")
                
                att = pk2.nom  #Etape 4 contre attaque 
                sleep(0.6)
                if pk2.pv <=0:
                    continuer = False
                    print(f'Le vainqueur et {self.nom} et le perdant est {pk2.nom}')
                    vainqueur = self.nom
                    perdant = pk2.nom
                    pk2.pv =0 #Pas de PV negatif 

                else:
                    print(f"C'est au tour de {pk2.nom}")
                
                sleep(0.6)
 

            elif att == pk2.nom and Pokemon.Attaque(pk2) > 0:
                degat = max(0,Pokemon.Attaque(pk2) -self.defs)
                degat = floor(degat) #arrondissement au int inferieur
                #Amelioration (Bonus)
                activation3 = randint(0,100)
                if activation3 <= 5:
                    degat = degat*1.5
                    print(f"{pk2.nom} va infliger un coup critique (5% de chance)")

                degat = int(degat)
                activation4 = randint(0,100)
                if activation4 >5:
                    self.pv -= degat
                    print(f'{self.nom} a subit {degat} de degat et lui reste {self.pv}.\n')
                else:
                    print(f"{self.nom} à esquiver l'attaque (5% de chance)\n")
                
                
                att = self.nom  #Etape 4 contre attaque 
                sleep(0.8)
                if self.pv <=0:
                    continuer = False
                    print(f'Le vainqueur est {pk2.nom} et le perdant est {self.nom}')
                    vainqueur= pk2.nom
                    perdant = self.nom
                    self.pv =0#Pas de PV negatif
                else : 
                    print(f"C'est au tour de {self.nom}")
                sleep(0.8)
                
        
        #Etape 5 Fin du combat
        if vainqueur == self.nom:
            self.exp+=2
            Pokemon.MaN(self) #Verification de niveau et augmenation si besoin
            pk2.exp+=1
            Pokemon.MaN(pk2) #Verification de niveau et augmenation si besoin

        else:
            pk2.exp+=2
            Pokemon.MaN(pk2) #Verification de niveau et augmenation si besoin
            self.exp+=1
            Pokemon.MaN(self) #Verification de niveau et augmenation si besoin
        
        
        return 'Le vainqueur est '+vainqueur +'\n'+'Le perdant est'+perdant
        
    def Soigner(self):
        '''Reatribut le nombre de pv maximal a un pokemon'''
        self.pv = self.maxpv
        return f'{self.nom} est soigne, il a {self.pv} points de vie'
    
    def get_Nom(self):
        return self.nom
    def get_pv(self):
        return self.pv
    def get_maxpv(self):
        return self.maxpv

    def Attaque(self):
        '''
        Role:
            gere la puissance d'une attaque
        Params:
            Un objet de type : Pokemon
        Return:
            Un float du nombre de degat
        '''
        bonus = 0
        de1 = randint(1,6)
        if de1 == 2 or de1 == 4 or de1 == 6:
            bonus += de1
        else:
            bonus=-(de1/2)
        return self.att + bonus + (sqrt(self.exp)/2)
    

    def Combattant(self,pk2):
        '''
        Role:
            Verifie le premier ataquant
        Params:
            Un objet de type : Pokemon
        Return:
            le nom du premier attaquant
        '''
        att = '' #Premier attaquant
        if self.vit > pk2.vit:
            att = self.nom
        elif self.vit == pk2.vit:
            pr = randint(0,1)
            if pr == 0:
                att = self.nom
            else :
                att = pk2.nom
        else:
            att = pk2.nom
        return att
    
    def to_dict(self):

        '''
        Role:
            Convertit les stats en dictionnaires 
        Params:
            Un objet de type : Pokemon
        Return:
            Un dictionnaire avec les stats du pokemon en question
        '''
        return {
            "nom": self.nom,
            "pv": self.pv,
            "maxpv": self.maxpv,
            "att": self.att,
            "defs": self.defs,
            "vit": self.vit,
            "exp": self.exp,
            "niv": self.niv
        }

    @staticmethod
    def from_dict(stats):
        '''
        Role:
            Cree un pokemon a partir des stats sauvegarde
        Params:
            Data des stats
        Return:
            Un nouveau pokemon avec des stats sauvegarde
        '''
        p = Pokemon.__new__(Pokemon)  # Cree un pokemon sans le constructeur
        p.nom = stats["nom"]
        p.pv = stats["pv"]
        p.maxpv = stats["maxpv"]
        p.att = stats["att"]
        p.defs = stats["defs"]
        p.vit = stats["vit"]
        p.exp = stats["exp"]
        p.niv = stats["niv"]
        return p
     


#Fonction de SAUVEGARDE
def save_all(filename, dictio):
    '''
        Role:
           Sauvegarde tous les pokemon courrant
        Params:
            Un fichier de sauvegarde (.txt)
            Un dictionnaire contenant tous les pokemons
        Return:
            Un fichier .txt dans le dossier courrant avec les stats des pokemons 


        '''
    data = {name: p.to_dict() for name, p in dictio.items()} #cree un dictionnaire grace a la methode to_dict qui permet de transformer tous les
    with open(filename, "w", encoding="utf-8") as f:#         pokemons dans dictio
        json.dump(data, f, indent=4)
    print(f"Sauvegarde de {len(pokemons)} Pokemons dans le fichier {filename}")

def load_all(filename, dictio):
    '''
        Role:
            Permet de recuperer les pokemon sauvegardes
        Params:
            Fichier de sauvegarde
        Return:
            Un dictionnaire contenant tous les pokemons dans le fichier de sauvegarde
    '''
    print("\t\t\t <!--- Attention ---!> ")
    print("\tCharger des pokemons pourrait supprimer des pokemons non enregistrés ")
    print("\tEtes-vous sûr de vouloir continuer?")
    try:
        continuer = int(input("\t[0]Non\n\t[1]Oui \n\tVotre choix: "))
    except ValueError:
        print("Entrée invalide, opération annulée.")
        return dictio

    if continuer == 1:
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f) #charge les donnees depuis le fichier 
            pokemons = [Pokemon.from_dict(stats) for stats in data.values()] #utilise la methode static qui permet de cree un objet de type pokemon 
            for i in range(len(pokemons)):#                                   a partir des stats dans les valeurs du dictionaire extrait du cichier json
                dictio[i] = pokemons[i]

            print(f"{len(pokemons)} pokemons chargés depuis {filename}")
            global nbrpok
            nbrpok +=len(pokemons)
            return dictio

        except (json.JSONDecodeError, TypeError, KeyError): #verifie si le fichier est compatible
            print(f"Erreur : le fichier {filename} n'est pas compatible (Fichier peut-etre vide).")
            return dictio
        except FileNotFoundError:
            print(f"Erreur : le fichier {filename} est introuvable.")
            return dictio
    else:
        print("Opération annulée.")
        return dictio


def supression():
    """
    Supprime toutes les donnees dans le fichier de sauvegarde
    """
    confirmation = input("\tEtes vous sur de vouloir supprimer tous les pokemon sauvegardes?\n\t [0]Non\n\t [1]Oui \n\tVotre choix:   ")
    
    if confirmation == "1":

        with open("savefile.txt", "w") as file:

                file.write("")
        global pokemons
        pokemons = {}
        print("\tLes pokemons ont ete supprime")
    else:
        print("Operation annulée.")


def menuPrinc():
    ''' Affiche le menu principal'''
    art =  '''  
    ██████╗  ██████╗ ██╗  ██╗███████╗███╗   ███╗ ██████╗ ███╗   ██╗    ███████╗
    ██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝████╗ ████║██╔═══██╗████╗  ██║    ╚══███╔╝
    ██████╔╝██║   ██║█████╔╝ █████╗  ██╔████╔██║██║   ██║██╔██╗ ██║      ███╔╝ 
    ██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║     ███╔╝  
    ██║     ╚██████╔╝██║  ██╗███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║    ███████╗
    ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝                                                                                                                                                                                                                                                                                   
    '''
    print(f'\t\t\t{art}')
    print("\t [0] Creer un nouveau pokemon\n\t [1] Voir l'inventaire des pokemons\n \t [2] Combat \n \t [3] Soigner \n \t [4] Charger des pokemons sauvegardes\n\t [5] Sauvegarde de tous les pokemons courrants\n \t [6] Suppression d'un fichier de sauvegarde \n \t [X] Quitter")

def creer(dictio):
    ''' Permet de creer un pokemon en utilisant le constructeur'''
    global nbrpok
    dictio[nbrpok] = Pokemon()
    print(f'{Pokemon.get_Nom(dictio[nbrpok])} a ete creer')
    nbrpok +=1
    return dictio

def combat(dictio):
    ''' Permet de lancer un combat en utilisant la methode Combat'''
    print('\t\t\t Choix des combatants')
    for i in dictio:
        print(f' [{i}] {Pokemon.get_Nom(dictio[i])}')
    choix1 = int(input('Premier combatant: '))
    choix2 = int(input('Deuxieme combatant: '))
    Pokemon.Combat(dictio[choix1], dictio[choix2])
    
def soigner(dictio):
    ''' Permet de soigner un pokemon en utilisant la methode Soigner'''
    print('\t\t\t Choix du pokemon a soigner')
    for i in dictio:
        print(f' [{i}] {Pokemon.get_Nom(dictio[i])} ({Pokemon.get_pv(dictio[i])} pv) ---> ({Pokemon.get_maxpv(dictio[i])} max pv)')

    choix1 = int(input('Choix: '))
    Pokemon.Soigner(dictio[choix1])
    print(f'{Pokemon.get_Nom(dictio[choix1])} a ete soigné ({Pokemon.get_pv(dictio[choix1])}pv)')


#Requete API pour noms des pokemons
print("Connexion a l'API...")
try:
    response = requests.get("https://pokebuildapi.fr/api/v1/pokemon")
    data = response.json()
    names = [pokemon['name'] for pokemon in data]# extrait que les noms dans toute l'information que renvoi l'api 
except requests.exceptions.ConnectionError:
    print("Il y a un problem lors de la connection à l'API")
else:
    print("Connexion réussie ! ")





pokemons = {}
nbrpok = 0

while True:
    '''
    Boucle pour afficher le menu principal 
    '''
    menuPrinc()
    choix = input('\tVotre choix: ')
    if choix == '0':
        creer(pokemons)
    elif choix == '2':
        combat(pokemons)
    elif choix == '3':
        soigner(pokemons)
    elif choix == '4':
        load_all('savefile.txt', pokemons)
    elif choix =='5':
        save_all('savefile.txt', pokemons)
    elif choix =='1':
        if pokemons == {}:
            print("Il n'y a pas de pokemons cree !")
        else:
            for i in pokemons:
                print(f'\n {pokemons[i]}\n')
    elif choix == '6':
        supression()
    elif choix =='X':
        break
    else:
        print('Choix invalide, veuillez réessayer')
