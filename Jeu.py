# Importation de modules : 
from grille import Grille
import pygame
from pygame.locals import*
from boutons import*
from random import*
from flotte import Flotte

# Codes couleurs : 
bleutheme = (51,141,255)
rouge = (255, 0, 0)
vert = (0, 255, 0)
noir = (0, 0, 0)
blanc = (255, 255, 255)
gris = (220, 220, 220)
jaune = (255, 255, 0)

def musique(situation):
    """
    Fonction qui joue la musique en fonction de ce que qui dois être lu.
    """
    if situation == "BOOM":
        file = "Musiques/alarme-destroyer-us-navy.mp3"
    elif situation == "Victoire":
        file = "Musiques/son victoire.mp3"
    elif situation == "Explosion":
        file = "Musiques/bruitage-explosion.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(1)

def arret():
    """
    Fonction qui arrête la fenêtre pygame et qui ferme le programme.
    """
    pygame.quit()
    exit()

# Importations musiques
theme = "Musiques\epic-background-music-for-video-adventure-trailer-royalty-free-download.mp3"

# Initialisation des grilles : 
grille1 = Grille()
grille2 = Grille()

flotte1 = Flotte(grille1)
flotte2 = Flotte(grille2)
# Initialisation de pygame :
resolution = (1000,750)
pygame.init()
pygame.mixer.init()
fenetre = pygame.display.set_mode(resolution)
heure = pygame.time.Clock()
heure.tick(60)

# Initialisation des titres :
font = pygame.font.SysFont('comicsans', 150)
font2 = pygame.font.SysFont('comicsans', 75)
titre = font.render("Bataille Navale", 1, blanc)
titrejeu1 = font2.render("Mise en place du Jeu - Joueur 1", 1, blanc)
titrejeu2 = font2.render("Mise en place du Jeu - Joueur 2", 1, blanc)
titrej1 = font2.render("Écran du joueur 1", 1, blanc)
titrej2 = font2.render("Écran du joueur 2", 1, blanc)
victoire = font.render("VICTOIRE", 1, jaune)
vj1 = font.render("Joueur 1", 1, jaune)
vj2 = font.render("Joueur 2", 1, jaune)
# Menu pricipal :
btjouer = Boutons(gris, 375, 312.5, 250, 250//2, "Jouer", blanc)
btquiter = Boutons(gris, 375, 500, 250, 250//2, "Quitter", blanc)

# Mise en place du jeu :
btrec = Boutons(noir, 250, 680, 200, 50, "Changer", blanc)

# Boutons réutilisable :
btok = Boutons(noir, 650, 680, 100, 50,  "Ok", blanc)

def prgrille(affichage=None, grille=None):
    """
    Fonction qui dessine la grille sur la fenêtre.
    """
    fontgrille = pygame.font.SysFont('comicsans', 50)
    listelettre = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for x in range(250, 800, 50):
        if x == 250 or x == 750:
            color = vert
        elif x == 500:
            color = rouge
        else:
            color = blanc
        pygame.draw.line(fenetre, color, (x, 125), (x, 625),2)
    for y in range(125, 675, 50):
        if y == 125 or y == 625:
            color = vert
        elif y == 375:
            color = rouge
        else:
            color = blanc
        pygame.draw.line(fenetre, color, (250, y), (750, y),2)
    listelettre = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    if affichage != None:
        for ligne in listelettre:
            indice = listelettre.index(ligne)
            for chiffre in range(10):
                if affichage == "Mis en place":
                    text = grille.returng(ligne, chiffre)
                    color = blanc
                elif affichage == "Jeu":
                    text = grille.reponse(ligne, chiffre)
                    if text == "X":
                        color = rouge
                    else:
                        color = bleutheme
                case = fontgrille.render(text, 1, color)
                fenetre.blit(case, (10+250+(50*chiffre),10+125+(50*indice)))

def clic(pos):
    """
    Fonction qui regarde dans quelle case de la grille le joueur clic.
    Fonctionne seulement si la grille est affiché.
    """
    x,y = pos
    ix = [250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
    iy = [125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625]
    if 250 <= x <= 750 and 125 <= y <= 625 and x not in ix and y not in iy:
        if 250 <= x <= 300:
            chiffre = 0
        elif 300 <= x <= 350:
            chiffre = 1
        elif 350 <= x <= 400:
            chiffre = 2
        elif 400 <= x <= 450:
            chiffre = 3
        elif 450 <= x <= 500:
            chiffre = 4
        elif 500 <= x <= 550:
            chiffre = 5
        elif 550 <= x <= 600:
            chiffre = 6
        elif 600 <= x <= 650:
            chiffre = 7
        elif 650 <= x <= 700:
            chiffre = 8
        elif 700 <= x <= 750:
            chiffre = 9
        if 125 <= y <= 175:
            lettre = "A"
        elif 175 <= y <= 225:
            lettre = "B"
        elif 225 <= y <= 275:
            lettre = "C"
        elif 275 <= y <= 325:
            lettre = "D"
        elif 325 <= y <= 375:
            lettre = "E"
        elif 375 <= y <= 425:
            lettre = "F"
        elif 425 <= y <= 475:
            lettre = "G"
        elif 475 <= y <= 525:
            lettre = "H"
        elif 525 <= y <= 575:
            lettre = "I"
        elif 575 <= y <= 625:
            lettre = "J"
        return (True, lettre, chiffre)
    else:
        return (False, None, None)

def fsit(situation):
    """
    Fonction qui affiche les interfaces.
    """
    pygame.mixer.music.stop()
    pygame.display.update(fenetre.fill(gris))
    if situation == "Menu":
        pygame.display.set_caption("Bataille Navale by GUITOEV - Menu principal") # Titre
        pygame.mixer.music.load(theme)
        pygame.mixer.music.play(-1)
        fenetre.fill(bleutheme)
        fenetre.blit(titre, (120,20))
        btjouer.draw(fenetre)
        btquiter.draw(fenetre)
        pygame.display.flip()
    elif situation == "Jeu j1" or situation == "Jeu j2":
        if situation == "Jeu j1":
            joueur = "Joueur 1"
            fenetre.blit(titrejeu1, (0,0))
            egrille = grille1
        else:
            joueur = "Joueur 2"
            fenetre.blit(titrejeu2, (0,0))
            egrille = grille2
        pygame.display.set_caption("Bataille Navale by GUITOEV - Jeu - Mise en place - " + joueur)
        egrille.choixgrille()
        prgrille("Mis en place", egrille)
        btrec.draw(fenetre)
        btok.draw(fenetre)
    elif situation == "Joueur 1" or situation == "Joueur 2":
        pygame.display.set_caption("Bataille Navale by GUITOEV - Jeu - " + situation)
        if situation == "Joueur 1":
            fenetre.blit(titrej1, (10,10))
            grilleob = grille1
            prgrille("Jeu", grille2)
        elif situation == "Joueur 2":
            fenetre.blit(titrej2, (10, 10))
            grilleob = grille2
            prgrille("Jeu", grille1)
    elif situation == "Victoire j1" or situation == "Victoire j2":
        fenetre.fill(bleutheme)
        if situation == "Victoire j1":
            joueur = "Joueur 1"
            fenetre.blit(vj1, (230, 150))
        else:
            joueur = "Joueur 2"
            fenetre.blit(vj2, (230, 150))
        pygame.display.set_caption("Bataille Navale by GUITOEV - Victoire - " + joueur)
        fenetre.blit(victoire, (230,20))
        btquiter.draw(fenetre)
        btjouer.draw(fenetre)
        musique("Victoire")

def aide():
    """
    Fonction qui affiche sur la console les règles du jeu.
    """
    res = '\n' + "==========Règles du jeu==========" + '\n'
    res += "La bataille navale" + '\n'
    res += "La bataille navale est un jeu de stratégie, le jeu consiste à être le premier à détruire les bateaux adverses." + '\n'
    res += "Pour cela, vous avez une grille de 10x10." + '\n'
    res += "Vous tirez dans une case où peut se trouver un navire ennemi." + '\n'
    res += "Si vous en touchez un, vous rejouez !" + '\n'
    res += "==========Règles du jeu==========" + '\n'
    res += "by GUITOEV, GUIllaume ThOmas et EVan, trois élèves de NSI en terminale :)" + '\n'
    res += "Notre github du projet : " + "https://github.com/guigui0159570/Bataille_Navale" + '\n'
    print(res)

# Jeu :
situation = "Menu"
fsit(situation)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            arret()
        elif event.type == pygame.KEYDOWN: # Touche clavier
            if event.key == pygame.K_x:
                arret()
            elif event.key == pygame.K_v: # Touche V
                if situation == "Joueur 1":
                    situation = "Victoire j1"
                elif situation == "Joueur 2":
                    situation = "Victoire j2"
                fsit(situation)
            elif event.key == pygame.K_g: # Touche G
                if situation == "Joueur 1":
                    grille2.printgrille()
                elif situation == "Joueur 2":
                    grille1.printgrille()
            elif event.key == pygame.K_h: # Touche H
                aide()
            elif event.key == pygame.K_RETURN: # Touche ENTRER
                situation = "Jeu j1"
                grille1.ret()
                grille2.ret()
                flotte1.ret()
                flotte2.ret()
                fsit(situation)
        elif event.type == pygame.MOUSEBUTTONDOWN: # Clic souris
            if situation == "Menu": # Verification des boutons du Menu
                if btjouer.isOver(pygame.mouse.get_pos()) == True: # Lancement du jeu
                    situation = "Jeu j1"
                    fsit(situation)
                elif btquiter.isOver(pygame.mouse.get_pos()) == True: # Arret du jeu
                    arret()
            elif situation == "Jeu j1" or situation == "Jeu j2":
                if situation == "Jeu j1":
                    egrille = grille1
                else:
                    egrille = grille2
                if btok.isOver(pygame.mouse.get_pos()) == True:
                    if situation == "Jeu j1":
                        situation = "Jeu j2"
                    else:
                        situation = "Joueur 1"
                    fsit(situation)
                elif btrec.isOver(pygame.mouse.get_pos()) == True:
                    egrille.ret()
                    egrille.choixgrille()
                    fsit(situation)
            elif situation == "Victoire j1" or situation == "Victoire j2":
                if btjouer.isOver(pygame.mouse.get_pos()) == True: # Lancement du jeu
                    situation = "Jeu j1"
                    grille1.ret()
                    grille2.ret()
                    fsit(situation)
                elif btquiter.isOver(pygame.mouse.get_pos()) == True:
                    arret()
            elif situation == "Joueur 1" or situation == "Joueur 2":
                tclic = clic(pygame.mouse.get_pos())
                if situation == "Joueur 1":
                    egrille = grille2
                    eflotte = flotte2
                else:
                    egrille = grille1
                    eflotte = flotte1
                if tclic[0] == True:
                    ele = egrille.returng(tclic[1], tclic[2])
                    if ele != None:
                        if ele != "O":
                            eflotte.deg(ele)
                            sit = eflotte.detruit()
                            if sit == True:
                                musique("Explosion")
                            else:
                                musique("BOOM")
                            egrille.modif(tclic[1], tclic[2], "X")
                            prgrille("Jeu", egrille)
                            if eflotte.victoire() == True:
                                situation = "Victoire j1"
                                fsit(situation)
                    elif ele == None:
                        egrille.modif(tclic[1], tclic[2], "O")
                        prgrille("Jeu", egrille)
                        if situation == "Joueur 1":
                            situation = "Joueur 2"
                        elif situation == "Joueur 2":
                            situation = "Joueur 1"
                        fsit(situation)
    pygame.display.update()
