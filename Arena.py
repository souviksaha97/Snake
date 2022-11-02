import sys, pygame
import numpy as np
import Snake


class Arena():
    def __init__(self, height, width, surface, background, grid_width, frame_rate):
        self.height = height
        self.width = width
        self.surface = surface
        self.frame_rate = frame_rate
        self.background = background
        self.background.fill((0, 0, 0))
        self.grid_width = grid_width
        self.snake = Snake.Snake(self.height, self.width, self.grid_width)
        

    def show_arena(self):
        return self.field
    
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

