# Importation de modules
from grille import Grille
import pygame
from pygame.locals import*

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

def titrefenetre(situation):
    if situation == "Menu":
        nom = "Menu principal"
    titre = "Bataille Navale by GUITOEVC - " + nom
    return titre

def musique(situation):
    if situation == "BOOM":
        file = explosion
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(1)

def arret():
    pygame.quit()
    exit()

# Importations musiques
theme = "Musiques\epic-background-music-for-video-adventure-trailer-royalty-free-download.mp3"
explosion = 'Musiques\bruitage-explosion.mp3'

# Codes couleurs
bleutheme = (51,141,255)
rouge = (255, 0, 0)
vert = (0, 255, 0)
noir = (0, 0, 0)
blanc = (255, 255, 255)

# Initialisation des grilles
grille1 = Grille()
grille2 = Grille()

# Initialisation de pygame
pygame.init()
pygame.mixer.init()
fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
heure = pygame.time.Clock()
heure.tick(60)

# Jeu
pygame.display.set_caption(titrefenetre("Menu")) # Titre
pygame.mixer.music.load(theme)
pygame.mixer.music.play(-1)
fenetre.fill(bleutheme)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            arret()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                musique("BOOM")
            elif event.key == pygame.K_x:
                arret()
    pygame.display.update()
