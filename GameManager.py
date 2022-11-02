import pygame
import sys
import Snake
import Arena
pygame.init()


class GameManager():
    def __init__(self, height, width, grid_width = 25, frame_rate = 10):
        self.height = height
        self.width = width
        self.grid_width = grid_width
        self.frame_rate = frame_rate
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((self.height, self.width))
        self.background = pygame.Surface(self.surface.get_size())
        self.arena = Arena.Arena(self.height, self.width, self.surface, self.background, self.grid_width, self.frame_rate)
        
    
    def tick_clock(self):
        self.clock.tick(self.frame_rate)
    
    def refresh_screen(self):
        self.surface.blit(self.background, (0,0))
        pygame.display.update()
    
    def get_key_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.arena.snake.move_snake('UP')
        elif keys[pygame.K_DOWN]:
            self.arena.snake.move_snake('DOWN')
        elif keys[pygame.K_LEFT]:
            self.arena.snake.move_snake('LEFT')
        elif keys[pygame.K_RIGHT]:
            self.arena.snake.move_snake('RIGHT')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def mainloop(self):
        while True:
            self.refresh_screen()
            self.arena.draw_snake()
            self.arena.draw_grid()
            self.get_key_input()
            self.tick_clock()

            

if __name__ == '__main__':
    game = GameManager(1000, 1000)
    game.mainloop()