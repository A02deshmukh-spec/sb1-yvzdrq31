"""Ghost class representing the enemies"""

import pygame
import random
from src.constants.game_settings import CELL_SIZE, GHOST_SPEED

class Ghost:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, CELL_SIZE - 2, CELL_SIZE - 2)
        self.color = color
        self.speed = GHOST_SPEED
        self.direction = pygame.math.Vector2(1, 0)
        self.move_timer = 0

    def update(self, maze):
        self.move_timer += 1
        if self.move_timer >= 60:  # Change direction every 60 frames
            self.move_timer = 0
            possible_directions = [
                pygame.math.Vector2(1, 0),
                pygame.math.Vector2(-1, 0),
                pygame.math.Vector2(0, 1),
                pygame.math.Vector2(0, -1)
            ]
            random.shuffle(possible_directions)
            
            for new_dir in possible_directions:
                next_pos = self.rect.copy()
                next_pos.x += new_dir.x * self.speed
                next_pos.y += new_dir.y * self.speed
                
                if not maze.check_wall_collision(next_pos):
                    self.direction = new_dir
                    break
        
        # Move in current direction
        next_pos = self.rect.copy()
        next_pos.x += self.direction.x * self.speed
        next_pos.y += self.direction.y * self.speed
        
        if not maze.check_wall_collision(next_pos):
            self.rect = next_pos

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.rect.width // 2)