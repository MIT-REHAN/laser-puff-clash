# Laser-Puff-Clash - Direct Pygame Version (Most reliable for Mac)
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display - Force window creation
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Laser-Puff-Clash")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Game variables
player1_score = 0
player2_score = 0
game_over = False
winner = None

# Player positions
player1 = pygame.Rect(100, HEIGHT//2 - 25, 50, 50)
player2 = pygame.Rect(WIDTH - 150, HEIGHT//2 - 25, 50, 50)

# Lasers
player1_lasers = []
player2_lasers = []
laser_speed = 8
cooldown = 0
cooldown_max = 20
PLAYER_SPEED = 5

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Restart game
                game_over = False
                player1_score = 0
                player2_score = 0
                winner = None
                player1.x = 100
                player1.y = HEIGHT//2 - 25
                player2.x = WIDTH - 150
                player2.y = HEIGHT//2 - 25
                player1_lasers.clear()
                player2_lasers.clear()
                cooldown = 0
    
    if not game_over:
        # Update cooldown
        if cooldown > 0:
            cooldown -= 1
        
        # Get keyboard state
        keys = pygame.key.get_pressed()
        
        # Player 1 movement (WASD)
        if keys[pygame.K_w] and player1.y > 0:
            player1.y -= PLAYER_SPEED
        if keys[pygame.K_s] and player1.y + 50 < HEIGHT:
            player1.y += PLAYER_SPEED
        if keys[pygame.K_a] and player1.x > 0:
            player1.x -= PLAYER_SPEED
        if keys[pygame.K_d] and player1.x + 50 < WIDTH//2:
            player1.x += PLAYER_SPEED
        
        # Player 2 movement (Arrows)
        if keys[pygame.K_UP] and player2.y > 0:
            player2.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN] and player2.y + 50 < HEIGHT:
            player2.y += PLAYER_SPEED
        if keys[pygame.K_LEFT] and player2.x > WIDTH//2:
            player2.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and player2.x + 50 < WIDTH:
            player2.x += PLAYER_SPEED
        
        # Shooting
        if keys[pygame.K_f] and cooldown == 0:
            player1_lasers.append(pygame.Rect(player1.x + 50, player1.y + 22, 10, 5))
            cooldown = cooldown_max
        
        if keys[pygame.K_SLASH] and cooldown == 0:
            player2_lasers.append(pygame.Rect(player2.x - 10, player2.y + 22, 10, 5))
            cooldown = cooldown_max
        
        # Update player 1 lasers
        for laser in player1_lasers[:]:
            laser.x += laser_speed
            if laser.x > WIDTH:
                player1_lasers.remove(laser)
            elif laser.colliderect(player2):
                player1_lasers.remove(laser)
                player1_score += 1
                player2.x = WIDTH - 150
                player2.y = HEIGHT//2 - 25
        
        # Update player 2 lasers
        for laser in player2_lasers[:]:
            laser.x -= laser_speed
            if laser.x < 0:
                player2_lasers.remove(laser)
            elif laser.colliderect(player1):
                player2_lasers.remove(laser)
                player2_score += 1
                player1.x = 100
                player1.y = HEIGHT//2 - 25
        
        # Win condition
        if player1_score >= 5:
            game_over = True
            winner = "Player 1"
        elif player2_score >= 5:
            game_over = True
            winner = "Player 2"
    
    # Draw everything
    screen.fill(BLACK)
    
    # Draw center line
    for y in range(0, HEIGHT, 20):
        pygame.draw.line(screen, WHITE, (WIDTH//2, y), (WIDTH//2, y+10), 2)
    
    # Draw players
    pygame.draw.rect(screen, RED, player1)
    pygame.draw.rect(screen, WHITE, player1, 2)
    pygame.draw.rect(screen, BLUE, player2)
    pygame.draw.rect(screen, WHITE, player2, 2)
    
    # Draw lasers
    for laser in player1_lasers:
        pygame.draw.rect(screen, RED, laser)
    for laser in player2_lasers:
        pygame.draw.rect(screen, BLUE, laser)
    
    # Draw text
    font = pygame.font.Font(None, 40)
    p1_text = font.render(f"Player 1: {player1_score}", True, RED)
    p2_text = font.render(f"Player 2: {player2_score}", True, BLUE)
    screen.blit(p1_text, (50, 30))
    screen.blit(p2_text, (WIDTH - 250, 30))
    
    # Controls text
    small_font = pygame.font.Font(None, 20)
    controls1 = small_font.render("WASD + F", True, RED)
    controls2 = small_font.render("Arrows + /", True, BLUE)
    screen.blit(controls1, (50, HEIGHT - 40))
    screen.blit(controls2, (WIDTH - 180, HEIGHT - 40))
    
    if game_over:
        game_font = pygame.font.Font(None, 60)
        game_text = game_font.render(f"{winner} WINS!", True, YELLOW)
        text_rect = game_text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(game_text, text_rect)
        
        restart_font = pygame.font.Font(None, 30)
        restart_text = restart_font.render("Press R to restart", True, WHITE)
        restart_rect = restart_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 60))
        screen.blit(restart_text, restart_rect)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()