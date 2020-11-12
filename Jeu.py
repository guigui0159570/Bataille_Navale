# Importation de modules : 
from grille import Grille
import pygame
from pygame.locals import*
from boutons import*
from random import*

# Codes couleurs : 
bleutheme = (51,141,255)
rouge = (255, 0, 0)
vert = (0, 255, 0)
noir = (0, 0, 0)
blanc = (255, 255, 255)
gris = (220, 220, 220)
jaune = (255, 255, 0)
''' utilisation des sons '''
def musique(situation):
    if situation == "BOOM":
        file = explosion
    elif situation == "Victoire":
        file = victoirem
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(1)
''' fonction afin de pouvoir sortir du jeu '''
def arret():
    pygame.quit()
    exit()

def jmp():
    pass

# Importations musiques
theme = "Musiques\epic-background-music-for-video-adventure-trailer-royalty-free-download.mp3"
explosion = "Musiques\bruitage-explosion.mp3"
victoirem = "Musiques\le-son-de-la-victoire-go-habs-go-coupe-stanley-2015-orchestre-symphonique-de-montreal-osm.mp3"

# Initialisation des grilles : 
grille1 = Grille()
grille2 = Grille()

# Initialisation de pygame : 
pygame.init()
pygame.mixer.init()
fenetre = pygame.display.set_mode((1000, 750))
heure = pygame.time.Clock()
heure.tick(60)

# Initialisation des titres :
font = pygame.font.SysFont('comicsans', 150)
font2 = pygame.font.SysFont('comicsans', 75)
titre = font.render("Bataille Navale", 1, blanc)
titrejeu = font2.render("Mise en place du jeu", 1, blanc)
titrej1 = font2.render("Écran du joueur 1", 1, blanc)
titrej2 = font.render("Écran du joueur 2", 1, blanc)
victoire = font.render("VICTOIRE", 1, jaune)

# Menu pricipal :
btjouer = Boutons(gris, 375, 312.5, 250, 250//2, "Jouer", blanc)
btquiter = Boutons(gris, 375, 500, 250, 250//2, "Quitter", blanc)

# Boutons réutilisable :
btok = Boutons(noir, 450, 680, 100, 50,  "Ok", blanc)

''' fonction qui verifie si le jeu doit mettre de la musique ou si la partie n'est pas encore terminé ps: cette fonction s'execute tout le long du jeu ''' 

def fsit(situation):
    pygame.mixer.music.stop()
    pygame.display.update(fenetre.fill(gris))
    if situation == "Menu":
        pygame.display.set_caption("Bataille Navale by GUITOEVC - Menu principal") # Titre
        pygame.mixer.music.load(theme)
        pygame.mixer.music.play(-1)
        fenetre.fill(bleutheme)
        fenetre.blit(titre, (120,20))
        btjouer.draw(fenetre)
        btquiter.draw(fenetre)
        pygame.display.flip()
    elif situation == "Jeu":
        pygame.display.set_caption("Bataille Navale by GUITOEVC - Jeu - Mise en place")
        fenetre.blit(titrejeu, (10,10))
        btok.draw(fenetre)
    elif situation == "Joueur 1" or situation == "Joueur 2":
        pygame.display.set_caption("Bataille Navale by GUITOEVC - Jeu - " + situation)
        if situation == "Joueur 1":
            fenetre.blit(titrej1, (10,10))
            grilleob = grille1
        elif situation == "Joueur 2":
            fenetre.blit(titrej2, (10, 10))
            grilleob = grille2
    elif situation == "Victoire j1" or situation == "Victoire j2":
            if situation == "Victoire j1":
                joueur = "Joueur 1"
            else:
                joueur = "Joueur 2"
            fenetre.fill(bleutheme)
            pygame.display.set_caption("Bataille Navale by GUITOEVC - Victoire - " + joueur)
            fenetre.blit(victoire, (120,20))
            btquiter.draw(fenetre)
            musique("Victoire")
            
        ''' Fonction qui effectue la permutation des joueurs dans le jeu '''
        
def changej(situation):
    if situation == "Joueur 1":
        situation = "Joueur 2"
    elif situation == "Joueur 2":
        situation = "Joueur 1"
    return situation
''' fonction principale sans elle le jeu n'existe pas '''
# Jeu :
situation = "Menu"
fsit(situation)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            arret()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                arret()
            elif event.key == pygame.K_v:
                if situation == "Joueur 1":
                    situation = "Victoire j1"
                elif situation == "Joueur 2":
                    situation = "Victoire j2"
                fsit(situation)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if situation == "Menu":
                if btjouer.isOver(pygame.mouse.get_pos()) == True:
                    situation = "Jeu"
                    fsit(situation)
                elif btquiter.isOver(pygame.mouse.get_pos()) == True:
                    arret()
            elif situation == "Jeu":
                if btok.isOver(pygame.mouse.get_pos()) == True:
                    situation = "Joueur 1"
                    fsit(situation)
            elif situation == "Victoire j1" or situation == "Victoire j2":
                if btquiter.isOver(pygame.mouse.get_pos()) == True:
                    arret()
    pygame.display.update()
