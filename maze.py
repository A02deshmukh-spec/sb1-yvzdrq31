import pygame
from settings import *

class Maze:
    def __init__(self):
        self.layout = MAZE_LAYOUT
        self.dots = []
        self.walls = []
        self.setup_maze()

    def setup_maze(self):
        for row in range(len(self.layout)):
            for col in range(len(self.layout[row])):
                x = col * CELL_SIZE
                y = row * CELL_SIZE
                if self.layout[row][col] == 1:  # Wall
                    self.walls.append(pygame.Rect(x, y, CELL_SIZE, CELL_SIZE))
                elif self.layout[row][col] == 2:  # Dot
                    self.dots.append(pygame.Rect(x + CELL_SIZE//2 - 4, 
                                               y + CELL_SIZE//2 - 4, 8, 8))

    def check_wall_collision(self, rect):
        return any(rect.colliderect(wall) for wall in self.walls)

    def check_dot_collision(self, rect):
        for dot in self.dots[:]:
            if rect.colliderect(dot):
                self.dots.remove(dot)
                return dot
        return None

    def draw(self, screen):
        # Draw walls
        for wall in self.walls:
            pygame.draw.rect(screen, BLUE, wall)
        
        # Draw dots
        for dot in self.dots:
            pygame.draw.rect(screen, WHITE, dot)