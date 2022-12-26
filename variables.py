import pygame
import os

pygame.init()

snake_color = (255, 0, 0)
food_color = (0, 188, 227)
grid_color = (128, 128, 128)
background_color = (0, 0,0)

snake_eats_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'files', 'snake_eats.wav'))
snake_dead_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'files', 'snake_dead.wav'))