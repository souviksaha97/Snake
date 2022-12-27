import pygame
import variables

class Arena():
    def __init__(self, height, width, grid_width):
        self.height = height
        self.width = width
        self.grid_width = grid_width
        
    def draw_food(self, coords, background):
        food_blob = pygame.Rect(coords[0], coords[1], self.grid_width, self.grid_width)
        pygame.draw.circle(background, variables.food_color, (coords[0]+self.grid_width//2, coords[1]+self.grid_width//2), self.grid_width//2-0.5)
        
        return food_blob


    def draw_grid(self, background):
        start_horizontal = [(0, i) for i in range(self.grid_width, self.height, self.grid_width)]
        end_horizontal = [(self.height, i) for i in range(self.grid_width, self.height, self.grid_width)]

        start_vertical = [(i, 0) for i in range(self.grid_width, self.height, self.grid_width)]
        end_vertical = [(i, self.width) for i in range(self.grid_width, self.height, self.grid_width)]

        for i in range(int(self.height/self.grid_width - 1)):
            pygame.draw.line(background, variables.grid_color, start_horizontal[i], end_horizontal[i])
            pygame.draw.line(background, variables.grid_color, start_vertical[i], end_vertical[i])
        
    def clear_grid(self, background):
        background.fill(variables.background_color)

    def draw_score(self, window, score):
        text_surf = variables.score_font.render('Score - {}'.format(score), True, variables.text_color, None)
        text_rect = text_surf.get_rect()
        text_rect.bottomright = self.height, self.width
        window.blit(text_surf, text_rect)