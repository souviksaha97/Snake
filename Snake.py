import random
import pygame

HEAD = 0

class Snake():
    def __init__(self, height, width, grid_width):
        self.color = (255, 0, 0)
        self.height = height
        self.width = width
        self.grid_width = grid_width
        self.x, self.y = random.choice(range(0, self.height, self.grid_width)), random.choice(range(0, self.width, self.grid_width))
        self.direction = random.choice(['LEFT', 'RIGHT', 'UP', 'DOWN'])
        self.snake = [(pygame.Rect(self.x, self.y , self.grid_width, self.grid_width), HEAD)]
        self.length = 1
    
    def move_snake(self,direction):
        print(self.direction)
        if self.direction == 'UP' and direction == 'DOWN' or self.direction == 'DOWN' and direction == 'UP':
            return
        elif self.direction == 'LEFT' and direction == 'RIGHT' or self.direction == 'RIGHT' and direction == 'LEFT':
            return
        self.direction = direction
     
    def grow_snake(self):
        self.length += 1
        self.snake.append((None, self.length-1))

    def draw_snake_blob(self, background):
        # next_blob, head_blob = self.plot_snake()
        # pygame.draw.rect(background, self.color, new)
        # pygame.draw.rect(background, (0,0,0), old)


        for i in reversed(range(self.length)):
            old_blob = self.snake[i]
            new_blob = self.plot_snake(old_blob)
            self.snake[i] = new_blob
            pygame.draw.rect(background, self.color, new_blob[0])
            if old_blob[0] is not None and old_blob[1] == self.length-1:
                pygame.draw.rect(background, (0,0,0), old_blob[0])
        
        return self.snake[HEAD][0]


    def plot_snake(self, blob):
        x, y, new_x, new_y = 0, 0, 0, 0
        new_location = None
        
        if blob[1] == HEAD:
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
        

            new_x, new_y = blob[0].x + x * self.grid_width , blob[0].y + y * self.grid_width

            if new_x > self.height-self.grid_width:
                new_x = 0
            elif new_x < 0:
                new_x = self.height-self.grid_width

            if new_y > self.width-self.grid_width:
                new_y = 0
            elif new_y < 0:
                new_y = self.width-self.grid_width
            
            new_location = (pygame.Rect(new_x, new_y, self.grid_width, self.grid_width), HEAD)
        else:
            new_location = (self.snake[blob[1]-1][0], blob[1])

        print(new_location, self.direction, len(self.snake))

        return new_location
