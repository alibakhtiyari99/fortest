import pygame

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame Game")

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Player settings
player_size = 40
player_x = WIDTH // 2
player_y = HEIGHT - 60
player_speed = 5

# Obstacle settings
obstacle_size = 50
obstacle_x = WIDTH // 2 - 25
obstacle_y = 50

# Game loop
running = True
while running:
    pygame.time.delay(30)  # Delay to control frame rate

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
        player_y += player_speed

    # Collision detection
    if (player_x < obstacle_x + obstacle_size and
        player_x + player_size > obstacle_x and
        player_y < obstacle_y + obstacle_size and
        player_y + player_size > obstacle_y):
        print("Game Over!")  # End game on collision
        running = False

    # Draw game elements
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))  # Player
    pygame.draw.rect(screen, BLUE, (obstacle_x, obstacle_y, obstacle_size, obstacle_size))  # Obstacle

    pygame.display.update()  # Update screen

pygame.quit()
