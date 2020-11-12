class Flotte():
    """
    Classe qui gère la flotte de bateau du joueur.
    """
    iporte_avion = 5
    icroiseur = 4
    icontre_torpileur = 3
    itorpilleur = 2
    def __init__(self, grille):
        """
        Méthode constructeur qui créer la flotte.
        """
        self.grille = grille
        self.porte_avion = 5
        self.croiseur = 4
        self.contre_torpilleur1 = 3
        self.contre_torpilleur2 = 3
        self.torpilleur = 2
        self.iflotte = 5
    
    def deg(self, ele):
        if ele == "P":
            self.porte_avion -= 1
        elif ele == "C":
            self.croiseur -= 1
        elif ele == "Ct":
            self.contre_torpilleur1 -= 1
        elif ele == "ct":
            self.contre_torpilleur2 -= 1
        elif ele == "T":
            self.torpilleur -= 1
    
    def detruit(self):
        res = False
        if self.porte_avion == 0:
            self.porte_avion = None
            res = True
        elif self.croiseur == 0:
            self.croiseur = None
            res = True
        elif self.contre_torpilleur1 == 0:
            self.contre_torpilleur1 = None
            res = True
        elif self.contre_torpilleur2 == 0:
            self.contre_torpilleur2 = None
            res = True
        elif self.torpilleur == 0:
            self.torpilleur = None
            res = True
        if res == True:
            self.iflotte -= 1
        return res
    
    def victoire(self):
        if self.iflotte == 0:
            return True
    
    def ret(self):
        self.grille = grille
        self.porte_avion = 5
        self.croiseur = 4
        self.contre_torpilleur1 = 3
        self.contre_torpilleur2 = 3
        self.torpilleur = 2
        self.iflotte = 5
