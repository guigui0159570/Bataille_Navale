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
        if lettre == "A" or lettre == "a":
            return self.A[chiffre]
        elif lettre == "B" or lettre == "b":
            return self.B[chiffre]
        elif lettre == "C" or lettre == "c":
            return self.C[chiffre]
        elif lettre == "D" or lettre == "d" :
            return self.D[chiffre]
        elif lettre == "E" or lettre == "e":
            return self.E[chiffre]
        elif lettre == "F" or lettre == "f":
            return self.F[chiffre]
        elif lettre == "G" or lettre == "g":
            return self.G[chiffre]
        elif lettre == "H" or lettre == "h":
            return self.H[chiffre]
        elif lettre == "I" or lettre == "i":
            return self.I[chiffre]
        elif lettre == "J" or lettre == "j":
            return self.J[chiffre]
        
    def modif(self, lettre, chiffre, état):
        if lettre == "A" or lettre == "a":
            self.A[chiffre] = état
        elif lettre == "B" or lettre == "b":
            self.B[chiffre] = état
        elif lettre == "C" or lettre == "c":
            self.C[chiffre] = état
        elif lettre == "D" or lettre == "d":
            self.D[chiffre] = état
        elif lettre == "E" or lettre == "e":
            self.E[chiffre] = état
        elif lettre == "F" or lettre == "f":
            self.F[chiffre] = état
        elif lettre == "G" or lettre == "g":
            self.G[chiffre] = état
        elif lettre == "H" or lettre == "h":
            self.H[chiffre] = état
        elif lettre == "I" or lettre == "i":
            self.I[chiffre] = état
        elif lettre == "J" or lettre == "j":
            self.J[chiffre] = état
