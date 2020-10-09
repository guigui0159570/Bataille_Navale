class Grille():
    def __init__(self):
        self.A = [None, None, None, None, None, None, None, None, None, None]
        self.B = [None, None, None, None, None, None, None, None, None, None]
        self.C = [None, None, None, None, None, None, None, None, None, None]
        self.D = [None, None, None, None, None, None, None, None, None, None]
        self.E = [None, None, None, None, None, None, None, None, None, None]
        self.F = [None, None, None, None, None, None, None, None, None, None]
        self.G = [None, None, None, None, None, None, None, None, None, None]
        self.H = [None, None, None, None, None, None, None, None, None, None]
        self.I = [None, None, None, None, None, None, None, None, None, None]
        self.J = [None, None, None, None, None, None, None, None, None, None]
        
    def affiche(self, lettre, chiffre):
        L = [0,1,2,3,4,5,6,7,8,9]
        assert chiffre not in 
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
        elif lettre == "J":
            return self.J[chiffre]
        
    def modif(self, lettre, chiffre, état):
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
        elif lettre == "J":
            self.J[chiffre] = état
