"""Player class representing Pacman"""

import pygame
from src.constants.colors import YELLOW
from src.constants.game_settings import CELL_SIZE, PLAYER_SPEED

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, CELL_SIZE - 2, CELL_SIZE - 2)
        self.speed = PLAYER_SPEED
        self.direction = pygame.math.Vector2(0, 0)
        self.next_direction = pygame.math.Vector2(0, 0)

    def handle_input(self, key):
        if key == pygame.K_LEFT:
            self.next_direction = pygame.math.Vector2(-1, 0)
        elif key == pygame.K_RIGHT:
            self.next_direction = pygame.math.Vector2(1, 0)
        elif key == pygame.K_UP:
            self.next_direction = pygame.math.Vector2(0, -1)
        elif key == pygame.K_DOWN:
            self.next_direction = pygame.math.Vector2(0, 1)

    def update(self, maze):
        # Try to move in the next direction if possible
        next_pos = self.rect.copy()
        next_pos.x += self.next_direction.x * self.speed
        next_pos.y += self.next_direction.y * self.speed
        
        if not maze.check_wall_collision(next_pos):
            self.direction = self.next_direction
        
        # Move in current direction if possible
        next_pos = self.rect.copy()
        next_pos.x += self.direction.x * self.speed
        next_pos.y += self.direction.y * self.speed
        
        if not maze.check_wall_collision(next_pos):
            self.rect = next_pos

    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW, self.rect.center, self.rect.width // 2)