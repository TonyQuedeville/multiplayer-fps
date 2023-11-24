
import pygame

# Affiche un texte
def texte(fenetre, texte, position, police="board2D/police/explore.ttf", taille=24, couleurs=((255,255,255), (0,0,0))):
    x, y = position
    color, back_color = couleurs 
    
    font = pygame.font.Font(police, taille)
    if back_color != None:
        text_b = font.render(texte, True, back_color)
        fenetre.blit(text_b, (x+2, y+2))
    text = font.render(texte, True, color)
    fenetre.blit(text, (x, y))
    