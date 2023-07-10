import pygame
import sys
import constant as con
from Game import Game


pygame.init()

screen = pygame.display.set_mode((con.WIDTH, con.HEIGHT))
pygame.display.set_caption("Connect 4")

game = Game()
game.start_menu(screen)

pygame.quit()
sys.exit()
