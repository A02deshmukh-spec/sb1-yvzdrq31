"""Main game class handling the game loop and core logic"""

import pygame
from src.entities.player import Player
from src.entities.ghost import Ghost
from src.entities.maze import Maze
from src.constants.colors import BLACK, WHITE, RED, PINK
from src.constants.game_settings import (
    SCREEN_WIDTH, SCREEN_HEIGHT, 
    PLAYER_START_X, PLAYER_START_Y,
    GHOST_START_X, GHOST_START_Y,
    DOT_POINTS, FPS
)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pacman")
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.maze = Maze()
        self.player = Player(PLAYER_START_X, PLAYER_START_Y)
        self.ghosts = [
            Ghost(GHOST_START_X, GHOST_START_Y, RED),  # Red ghost
            Ghost(GHOST_START_X + 32, GHOST_START_Y, PINK)  # Pink ghost
        ]
        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.player.handle_input(event.key)

    def update(self):
        self.player.update(self.maze)
        for ghost in self.ghosts:
            ghost.update(self.maze)
            
        # Check collision with dots
        dot = self.maze.check_dot_collision(self.player.rect)
        if dot:
            self.score += DOT_POINTS
            
        # Check collision with ghosts
        for ghost in self.ghosts:
            if self.player.rect.colliderect(ghost.rect):
                self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.maze.draw(self.screen)
        self.player.draw(self.screen)
        for ghost in self.ghosts:
            ghost.draw(self.screen)
            
        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {self.score}', True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()