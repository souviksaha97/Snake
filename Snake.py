import random
import pygame
import variables

HEAD = 0

class Snake():
    def __init__(self, height, width, grid_width):
        self.color = variables.snake_color
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

    def check_food_collision(self, head_blob, food_blob):
        return pygame.Rect.colliderect(head_blob, food_blob)
    
    def check_self_collision(self, blob):
        return blob[0].collidelist([i[0] for i in self.snake[1:]])

    def draw_snake_blob(self, background):

        for i in reversed(range(self.length)):
            old_blob = self.snake[i]
            new_blob = self.plot_snake(old_blob)
            self.snake[i] = new_blob
            if new_blob[1] == HEAD:
                if self.direction == 'LEFT':
                    pygame.draw.rect(background, self.color, new_blob[0], border_bottom_left_radius=self.grid_width//2, border_top_left_radius=self.grid_width//2)
                elif self.direction == 'RIGHT':
                    pygame.draw.rect(background, self.color, new_blob[0], border_bottom_right_radius=self.grid_width//2, border_top_right_radius=self.grid_width//2)
                elif self.direction == 'UP':
                    pygame.draw.rect(background, self.color, new_blob[0], border_top_left_radius=self.grid_width//2, border_top_right_radius=self.grid_width//2)
                else:
                    pygame.draw.rect(background, self.color, new_blob[0], border_bottom_left_radius=self.grid_width//2, border_bottom_right_radius=self.grid_width//2)
            
            else:
                pygame.draw.rect(background, self.color, new_blob[0])
            
            if old_blob[0] is not None and old_blob[1] == self.length-1:
                pygame.draw.rect(background, variables.background_color, old_blob[0])
        
        if self.check_self_collision(self.snake[HEAD]) != -1:
            return False

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

        return new_location
