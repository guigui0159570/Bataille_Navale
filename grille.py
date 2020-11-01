class Grille():
    """
    Classe qui générère des grilles.
    Un objet grille contient plusieurs listes correspondant à chaque ligne de la bataille navale.
    """
    def __init__(self):
        self.A = [None] * 10
        self.B = [None] * 10
        self.C = [None] * 10
        self.D = [None] * 10
        self.E = [None] * 10
        self.F = [None] * 10
        self.G = [None] * 10
        self.H = [None] * 10
        self.I = [None] * 10
        self.J = [None] * 10
        self.dict = {"A":self.A, "B":self.B, "C":self.C, "D":self.D, "E":self.E, "F":self.F, "G":self.G, "H":self.H, "I":self.H, "J":self.J}
        
    def returng(self, lettre, chiffre):
        return self.dict[lettre][chiffre]
    
    def printg(self, lettre, chiffre):
        print(self.dict[lettre][chiffre])
        
    def modif(self, lettre, chiffre, état):
        self.dict[lettre][chiffre] = état
