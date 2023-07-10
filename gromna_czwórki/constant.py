import pygame
import os


WIDTH = 700
HEIGHT = 800
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
TOKEN_SIZE = 100

MENU_WIDTH = WIDTH // 6 * 4
MENU_HEIGHT = HEIGHT // 6 * 4
BUTTON_WIDTH = MENU_WIDTH

GRAY = (230, 230, 230)
PINK = (255, 200, 210)
LIGHTBLUE = (158, 209, 225)
BLACK = (100, 100, 100)
RED = (255, 100, 100)
JET_BLACK = (50, 50, 50)
DARK_PINK = (255, 175, 189)
BEIGE = (253, 243, 220)
MEDIUM_BEIGE = (148, 105, 8)
DARK_BEIGE = (100, 71, 6)


BOARD_OFFSET_Y = 200
OUTLINE_WIDTH = 3
RADIUS = 20
MENU_FONT_SIZE = 52

path_images = os.path.join(os.getcwd(), 'images')
image_names = sorted(os.listdir(path_images))

IMAGES = {}
for file_name in image_names:
    image_name = file_name[:-4].upper()
    IMAGES[image_name] = pygame.image.load(os.path.join(path_images, file_name))

pygame.mixer.init()
path_sounds = os.path.join(os.getcwd(), 'sounds')
sound_names = sorted(os.listdir(path_sounds))

SOUNDS = {}
for sounds_name in sound_names:
    sound_name = sounds_name
    sound_path = os.path.join(path_sounds, sound_name)
    SOUNDS[sound_name] = pygame.mixer.Sound(sound_path)

pygame.mixer.quit()
