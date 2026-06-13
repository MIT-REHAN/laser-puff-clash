# Laser-Puff-Clash - Mac Fixed Version
import pgzrun
import pygame
from pygame.locals import *

# IMPORTANT: Set these BEFORE creating the window
WIDTH = 800
HEIGHT = 600

# Force window to be visible on Mac
pygame.init()
pygame.display.set_caption("Laser-Puff-Clash")
os.environ['SDL_VIDEO_CENTERED'] = '1'

# The rest of your game
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

player1_score = 0
player2_score = 0
game_over = False
winner = None

player1 = Rect(100, HEIGHT//2 - 25, 50, 50)
player2 = Rect(WIDTH - 150, HEIGHT//2 - 25, 50, 50)

player1_lasers = []
player2_lasers = []
laser_speed = 8
cooldown = 0
cooldown_max = 20
PLAYER_SPEED = 5

def draw():
    screen.fill(BLACK)
    
    # Draw center line
    for y in range(0, HEIGHT, 20):
        screen.draw.line((WIDTH//2, y), (WIDTH//2, y+10), WHITE)
    
    # Draw players
    screen.draw.filled_rect(player1, RED)
    screen.draw.rect(player1, WHITE)
    screen.draw.filled_rect(player2, BLUE)
    screen.draw.rect(player2, WHITE)
    
    screen.draw.text("P1", (player1.x + 15, player1.y + 15), fontsize=20, color=WHITE)
    screen.draw.text("P2", (player2.x + 15, player2.y + 15), fontsize=20, color=WHITE)
    
    # Draw lasers
    for laser in player1_lasers:
        screen.draw.filled_rect(Rect((laser.x, laser.y), (10, 5)), RED)
    for laser in player2_lasers:
        screen.draw.filled_rect(Rect((laser.x, laser.y), (10, 5)), BLUE)
    
    # Draw scores
    screen.draw.text(f"Player 1: {player1_score}", (50, 30), fontsize=40, color=RED)
    screen.draw.text(f"Player 2: {player2_score}", (WIDTH - 200, 30), fontsize=40, color=BLUE)
    screen.draw.text("WASD + F", (50, HEIGHT - 40), fontsize=20, color=RED)
    screen.draw.text("Arrows + /", (WIDTH - 180, HEIGHT - 40), fontsize=20, color=BLUE)
    
    if game_over:
        game_over_text = f"{winner} WINS!"
        screen.draw.text(game_over_text, center=(WIDTH//2, HEIGHT//2), 
                        fontsize=60, color=YELLOW, owidth=2, ocolor=BLACK)
        screen.draw.text("Press R to restart", center=(WIDTH//2, HEIGHT//2 + 60),
                        fontsize=30, color=WHITE)

def update():
    global player1_score, player2_score, game_over, winner, cooldown
    
    if game_over:
        return
    
    if cooldown > 0:
        cooldown -= 1
    
    # Player 1 movement (WASD)
    if keyboard.w and player1.y > 0:
        player1.y -= PLAYER_SPEED
    if keyboard.s and player1.y + 50 < HEIGHT:
        player1.y += PLAYER_SPEED
    if keyboard.a and player1.x > 0:
        player1.x -= PLAYER_SPEED
    if keyboard.d and player1.x + 50 < WIDTH//2:
        player1.x += PLAYER_SPEED
    
    # Player 2 movement (Arrows)
    if keyboard.up and player2.y > 0:
        player2.y -= PLAYER_SPEED
    if keyboard.down and player2.y + 50 < HEIGHT:
        player2.y += PLAYER_SPEED
    if keyboard.left and player2.x > WIDTH//2:
        player2.x -= PLAYER_SPEED
    if keyboard.right and player2.x + 50 < WIDTH:
        player2.x += PLAYER_SPEED
    
    # Shooting
    if keyboard.f and cooldown == 0:
        player1_lasers.append(Rect(player1.x + 50, player1.y + 22, 10, 5))
        cooldown = cooldown_max
    
    if keyboard.slash and cooldown == 0:
        player2_lasers.append(Rect(player2.x - 10, player2.y + 22, 10, 5))
        cooldown = cooldown_max
    
    # Update lasers
    for laser in player1_lasers[:]:
        laser.x += laser_speed
        if laser.x > WIDTH:
            player1_lasers.remove(laser)
        elif laser.colliderect(player2):
            player1_lasers.remove(laser)
            player1_score += 1
            player2.x = WIDTH - 150
            player2.y = HEIGHT//2 - 25
    
    for laser in player2_lasers[:]:
        laser.x -= laser_speed
        if laser.x < 0:
            player2_lasers.remove(laser)
        elif laser.colliderect(player1):
            player2_lasers.remove(laser)
            player2_score += 1
            player1.x = 100
            player1.y = HEIGHT//2 - 25
    
    if player1_score >= 5:
        game_over = True
        winner = "Player 1"
    elif player2_score >= 5:
        game_over = True
        winner = "Player 2"

def on_key_down(key):
    global game_over, player1_score, player2_score, winner
    global player1, player2, player1_lasers, player2_lasers, cooldown
    
    if key.name == 'R' or key.name == 'r':
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

pgzrun.go()