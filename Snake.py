import random
from re import L
import pygame
import queue

class Snake():
    def __init__(self, height, width, grid_width):
        self.color = (255, 0, 0)
        self.snake = queue.Queue()
        self.height = height
        self.width = width
        self.grid_width = grid_width
        self.x, self.y = random.choice(range(0, self.height, self.grid_width)), random.choice(range(0, self.width, self.grid_width))
        # self.snake.put(pygame.Rect(random.choice(range(0, height, grid_width)), random.choice(range(0, width, grid_width)), grid_width, grid_width))
        self.direction = random.choice(['LEFT', 'RIGHT', 'UP', 'DOWN'])
    
    def move_snake(self,direction):
        if self.direction == 'UP' and direction == 'DOWN' or self.direction == 'DOWN' and direction == 'UP':
            return
        elif self.direction == 'LEFT' and direction == 'RIGHT' or self.direction == 'RIGHT' and direction == 'LEFT':
            return
        self.direction = direction
     
    def grow_snake(self,):
        pass


    def plot_snake(self):
        if not self.snake.empty():
            old_location = self.snake.get()
        else:
            old_location = pygame.Rect(self.x, self.y, self.grid_width, self.grid_width)

        if self.direction == 'RIGHT':
            x = 1
            y = 0
        elif self.direction == 'LEFT':
            x = -1
            y = 0
        elif self.direction == 'UP':
            x = 0
            y = -1
        elif self.direction == 'DOWN':
            x = 0
            y = 1
        
        self.x, self.y = self.x + x * self.grid_width, self.y + y * self.grid_width

        if self.x > self.height:
            self.x = 0
        elif self.x < 0:
            self.x = self.height

        if self.y > self.width:
            self.y = 0
        elif self.y < 0:
            self.y = self.width

        new_location = pygame.Rect(self.x, self.y, self.grid_width, self.grid_width)
        self.snake.put(new_location)
        return old_location, new_location
        # pygame.draw.rect(self.a1.get_screen_object()[0], self.color, snake_head)

        # self.a1.get_screen_object()[1].blit(self.a1.get_screen_object()[0], (0,0))


# if __name__ == '__main__':
#     # a1 = Arena(1000, 500)
#     snake = Snake()
#     while True:
#         snake.a1.refresh_screen()
#         snake.a1.draw_grid()
#         snake.draw_snake()
#         snake.a1.tick_clock()