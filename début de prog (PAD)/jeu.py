class bateau(): # A verifier
    def __init__(self, taille, nom):
        self.bat1 = taille = 5, nom = "porte_avion"
        slef.bat2 = taille = 4, nom = "croiseur"
        self.bat3 = taille = 3, nom = "contre_torpilleur"
        self.bat4 = taille = 3, nom = "sous_marin"
        self.bat5 = taille = 2, nom = "torpilleur
        
def frappe(): # NE MARCHE PAS
    x = int(input("Indiquer votre ligne (entre 0 et 9)"))
    if x > 9 :
        raise ZeroDivisionError('votre nombre n est pas compris entre 0 et 9')
    y = input("Indiquer votre colone (entre A et J)")
    if y != 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I' or 'J' or 'a' or 'b' or 'c' or 'd' or 'e' or 'f' or 'g' or 'h' or 'i' or 'j':
        raise ZeroDivisionError('votre lettre n est pas compris entre A et J')
    
print(frappe())
