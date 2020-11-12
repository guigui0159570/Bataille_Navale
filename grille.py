from random import*
class Grille():
    """
    Classe qui générère des grilles.
    Un objet grille contient plusieurs listes correspondant à chaque ligne de la bataille navale.
    """
    def __init__(self):
        """
        Méthode constructeur qui créer la grille.
        """
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
        
    def returng(self, lettre, chiffre):
        """
        Méthode qui renvoie ce qu'il y a dans la case de la grille entrée en paramètre.
        """
        if lettre == "A":
            return self.A[chiffre]
        elif lettre == "B":
            return self.B[chiffre]
        elif lettre == "C":
            return self.C[chiffre]
        elif lettre == "D":
            return self.D[chiffre]
        elif lettre == "E":
            return self.E[chiffre]
        elif lettre == "F":
            return self.F[chiffre]
        elif lettre == "G":
            return self.G[chiffre]
        elif lettre == "H":
            return self.H[chiffre]
        elif lettre == "I":
            return self.I[chiffre]
        else:
            return self.J[chiffre]
        
    def modif(self, lettre, chiffre, état):
        """
        Méthode qui modifie ce qu'il y a dans la case de la grille entrée en paramètre avec ce qui a été entrée en paramètre.
        """
        if lettre == "A":
            self.A[chiffre] = état
        elif lettre == "B":
            self.B[chiffre] = état
        elif lettre == "C":
            self.C[chiffre] = état
        elif lettre == "D":
            self.D[chiffre] = état
        elif lettre == "E":
            self.E[chiffre] = état
        elif lettre == "F":
            self.F[chiffre] = état
        elif lettre == "G":
            self.G[chiffre] = état
        elif lettre == "H":
            self.H[chiffre] = état
        elif lettre == "I":
            self.I[chiffre] = état
        else:
            self.J[chiffre] = état
    
    def ret(self):
        """
        Méthode qui réinitialise la grille.
        """
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
    
    def reponse(self, lettre, chiffre):
        """
        Méthode qui affiche uniquement si il y a ou il y a pas de bateau pour la case de la grille entrée en paramètre.
        """
        if lettre == "A":
            ele = self.A[chiffre]
        elif lettre == "B":
            ele = self.B[chiffre]
        elif lettre == "C":
            ele = self.C[chiffre]
        elif lettre == "D":
            ele = self.D[chiffre]
        elif lettre == "E":
            ele = self.E[chiffre]
        elif lettre == "F":
            ele = self.F[chiffre]
        elif lettre == "G":
            ele = self.G[chiffre]
        elif lettre == "H":
            ele = self.H[chiffre]
        elif lettre == "I":
            ele = self.I[chiffre]
        else:
            ele = self.J[chiffre]
        if ele == "X" or ele == "O":
            return False
        else:
            return ele
    
    def choixgrille(self):
        """
        Méthode qui donne une grille.
        """
        pass
