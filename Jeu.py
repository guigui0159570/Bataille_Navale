from grille import Grille

def choix(grille):
    lettres = ["a","b","c","d","e","f","g","h","i","j","A","B","C","D","E","F","G","H","I","J"]
    chiffres = ["0","1","2","3","4","5","6","7","8","9"]
    while True:
        choix = input("Quelles sont les coordonnées de la frappe : ")
        if len(choix) == 2:
            ele1 = choix[0]
            ele2 = choix[1]
            if ele1 in lettres:
                if ele2 in chiffres:
                    lettre = ele1
                    chiffre = ele2
                    print(grille.affiche(lettre, int(chiffre)))

grille1 = Grille()
grille2 = Grille()
choix(grille1)
