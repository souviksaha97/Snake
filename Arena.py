import pygame

class Arena():
    def __init__(self, height, width, grid_width):
        self.height = height
        self.width = width
        self.grid_width = grid_width
        
    def draw_food(self, coords, background):
        food_blob = pygame.Rect(coords[0], coords[1], self.grid_width, self.grid_width)
        pygame.draw.rect(background, (0, 255, 0), food_blob)
        return food_blob


    def draw_grid(self, background):
        start_horizontal = [(0, i) for i in range(self.grid_width, self.height, self.grid_width)]
        end_horizontal = [(self.height, i) for i in range(self.grid_width, self.height, self.grid_width)]

        start_vertical = [(i, 0) for i in range(self.grid_width, self.height, self.grid_width)]
        end_vertical = [(i, self.width) for i in range(self.grid_width, self.height, self.grid_width)]

        for i in range(int(self.height/self.grid_width - 1)):
            pygame.draw.line(background, (128, 128, 128), start_horizontal[i], end_horizontal[i])
            pygame.draw.line(background, (128, 128, 128), start_vertical[i], end_vertical[i])
        
    def clear_grid(self, background):
        background.fill((0, 0, 0))

