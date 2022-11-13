import pygame
import os

class Audio():
    def __init__(self):
        self.audio = os.path.join(os.getcwd(), 'audio')
        self.pwr_up = pygame.mixer.Sound(os.path.join(self.audio, 'pwr_up.wav'))
    
    def snake_lvl_up(self):
        self.play_short_audio(self.pwr_up)

    def play_short_audio(self, audio_obj):
        pygame.mixer.Sound.play(audio_obj)
        pygame.mixer.music.stop()
