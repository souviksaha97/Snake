import sys, pygame
import numpy as np
import Snake

pygame.init()

class Arena():
    def __init__(self, height, width, grid_width = 25, frame_rate = 10):
        self.height = height
        self.width = width
        self.field = np.zeros((height, width))
        self.surface = pygame.display.set_mode((self.height, self.width))
        self.clock = pygame.time.Clock()
        self.frame_rate = frame_rate
        self.background = pygame.Surface(self.surface.get_size())
        self.background.fill((0, 0, 0))
        self.grid_width = grid_width
        self.snake = Snake.Snake(self.height, self.width, self.grid_width)
        

    def show_arena(self):
        return self.field
    
    def get_screen_object(self):
        return self.surface, self.background

    def refresh_screen(self):
        self.surface.blit(self.background, (0,0))
        pygame.display.update()
    
    def tick_clock(self):
        self.clock.tick(self.frame_rate)
    
    def draw_grid(self):
        start_horizontal = [(0, i) for i in range(self.grid_width, self.height, self.grid_width)]
        end_horizontal = [(self.height, i) for i in range(self.grid_width, self.height, self.grid_width)]

        start_vertical = [(i, 0) for i in range(self.grid_width, self.height, self.grid_width)]
        end_vertical = [(i, self.width) for i in range(self.grid_width, self.height, self.grid_width)]

        for i in range(int(self.height/self.grid_width - 1)):
            pygame.draw.line(self.background, (255, 255, 255), start_horizontal[i], end_horizontal[i])
            pygame.draw.line(self.background, (255, 255, 255), start_vertical[i], end_vertical[i])
        
    def draw_snake(self):
        old, new = self.snake.plot_snake()
        pygame.draw.rect(self.background, self.snake.color, new)
        print(old, new)

        pygame.draw.rect(self.background, (0,0,0), old)


if __name__ == '__main__':
    a1 = Arena(500, 500)
    while True:
        a1.refresh_screen()
        a1.draw_snake()
        a1.draw_grid()
        a1.tick_clock()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            a1.snake.move_snake('UP')
        elif keys[pygame.K_DOWN]:
            a1.snake.move_snake('DOWN')
        elif keys[pygame.K_LEFT]:
            a1.snake.move_snake('LEFT')
        elif keys[pygame.K_RIGHT]:
            a1.snake.move_snake('RIGHT')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()