# Alternative version using shapes instead of images
# Replace the draw() function with this one if you don't have images

def draw():
    """Draw everything on screen (shape-based version)"""
    screen.fill(BLACK)
    
    # Draw center line
    for y in range(0, HEIGHT, 20):
        screen.draw.line((WIDTH//2, y), (WIDTH//2, y+10), WHITE)
    
    # Draw players as circles (instead of images)
    screen.draw.filled_circle((player1.x, player1.y), 25, RED)
    screen.draw.filled_circle((player2.x, player2.y), 25, BLUE)
    
    # Draw player labels
    screen.draw.text("P1", (player1.x - 15, player1.y - 8), fontsize=20, color=WHITE)
    screen.draw.text("P2", (player2.x - 15, player2.y - 8), fontsize=20, color=WHITE)
    
    # Draw lasers as small rectangles
    for laser in player1_lasers:
        screen.draw.filled_rect(Rect((laser.x - 5, laser.y - 3), (10, 6)), RED)
    for laser in player2_lasers:
        screen.draw.filled_rect(Rect((laser.x - 5, laser.y - 3), (10, 6)), BLUE)
    
    # Draw scores
    screen.draw.text(f"Player 1: {player1_score}", (50, 30), fontsize=40, color=RED)
    screen.draw.text(f"Player 2: {player2_score}", (WIDTH - 200, 30), fontsize=40, color=BLUE)
    
    # Draw game over message if needed
    if game_over:
        game_over_text = f"{winner} WINS!"
        screen.draw.text(game_over_text, center=(WIDTH//2, HEIGHT//2), 
                        fontsize=60, color=YELLOW, owidth=2, ocolor=BLACK)
        screen.draw.text("Press R to restart", center=(WIDTH//2, HEIGHT//2 + 60),
                        fontsize=30, color=WHITE)