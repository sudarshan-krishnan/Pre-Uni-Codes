import pygame
import sys

pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400
GROUND_HEIGHT = 50
WHITE = (255, 255, 255)

# Initialize the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chrome Dino Game')

# Load game assets
dino_img = pygame.image.load('dino.png')
dino_rect = dino_img.get_rect()
dino_rect.bottom = SCREEN_HEIGHT - GROUND_HEIGHT
dino_jump = False
dino_jump_vel = 15

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not dino_jump:
        dino_jump = True

    # Update game state
    if dino_jump:
        dino_rect.y -= dino_jump_vel
        dino_jump_vel -= 1
        if dino_rect.bottom >= SCREEN_HEIGHT - GROUND_HEIGHT:
            dino_jump = False
            dino_jump_vel = 15

    # Draw game objects
    screen.fill(WHITE)
    screen.blit(dino_img, dino_rect)
    pygame.draw.rect(screen, (0, 0, 0), (0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))

    # Update the display
    pygame.display.flip()
    clock.tick(60)
