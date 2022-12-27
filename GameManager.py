import pygame
import sys
import Snake
import Arena

import variables
import random
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
        self.arena = Arena.Arena(self.height, self.width, self.grid_width)
        self.snake = Snake.Snake(self.height, self.width, self.grid_width)

        self.grid_flag = True
        self.food_flag = False

        self.food_coords = (0,0)

        self.tick_counter = 0

        self.score = 0
    
    def get_random_coordinates(self):
        return random.choice(range(0, self.height, self.grid_width)), random.choice(range(0, self.width, self.grid_width))

    def tick_clock(self):
        self.clock.tick(self.frame_rate)
    
    def refresh_screen(self):
        self.surface.blit(self.background, (0,0))
        self.arena.draw_score(self.surface, self.score)
        pygame.display.update()

    
    def get_key_input(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.snake.move_snake('UP')
        elif keys[pygame.K_DOWN]:
            self.snake.move_snake('DOWN')
        elif keys[pygame.K_LEFT]:
            self.snake.move_snake('LEFT')
        elif keys[pygame.K_RIGHT]:
            self.snake.move_snake('RIGHT')
        elif keys[pygame.K_q] and self.tick_counter % 2 == 0:
            self.grid_flag = not self.grid_flag
            self.arena.clear_grid(self.background)
            self.arena.draw_food(self.food_coords, self.background)

        self.tick_counter+=1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def mainloop(self):
        while True:
            self.refresh_screen()
            head_blob = self.snake.draw_snake_blob(self.background)
            if not head_blob:
                pygame.mixer.Sound.play(variables.snake_dead_sound)
                pygame.time.wait(int(variables.snake_dead_sound.get_length() * 1000))
                pygame.quit()
                print('Game Over')
                sys.exit()

            if self.grid_flag:
                self.arena.draw_grid(self.background)
            if not self.food_flag:
                self.food_coords = self.get_random_coordinates()
                food_blob = self.arena.draw_food(self.food_coords, self.background)
                self.food_flag = True
            else:
                if self.snake.check_food_collision(head_blob, food_blob):
                    self.food_flag = False
                    self.score += 1
                    self.snake.grow_snake()
                    pygame.mixer.Sound.play(variables.snake_eats_sound)
                    self.frame_rate += 0.5
            

            self.get_key_input()
            self.tick_clock()

            

if __name__ == '__main__':
    game = GameManager(1000, 1000)
    game.mainloop()