import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flapper Bird")

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
GREEN = (0, 200, 0)

# Game variables
gravity = 0.5
bird_movement = 0
score = 0
font = pygame.font.SysFont("Arial", 30)

# Bird setup
bird = pygame.Rect(50, HEIGHT//2, 30, 30)

# Pipe setup
pipe_width = 60
pipe_gap = 150
pipes = []

def create_pipe():
    height = random.randint(100, 400)
    top_pipe = pygame.Rect(WIDTH, 0, pipe_width, height)
    bottom_pipe = pygame.Rect(WIDTH, height + pipe_gap, pipe_width, HEIGHT - height - pipe_gap)
    return top_pipe, bottom_pipe

# Clock
clock = pygame.time.Clock()

# Add first pipes
pipes.extend(create_pipe())

# Game loop
running = True
while running:
    screen.fill(BLUE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = -8

    # Bird movement
    bird_movement += gravity
    bird.y += int(bird_movement)

    # Draw bird
    pygame.draw.rect(screen, WHITE, bird)

    # Pipe movement
    for pipe in pipes:
        pipe.x -= 3
        pygame.draw.rect(screen, GREEN, pipe)

    # Add new pipes
    if pipes[-1].x < WIDTH - 200:
        pipes.extend(create_pipe())

    # Remove off-screen pipes
    pipes = [pipe for pipe in pipes if pipe.x + pipe_width > 0]

    # Collision detection
    for pipe in pipes:
        if bird.colliderect(pipe):
            pygame.quit()
            sys.exit()

    if bird.top <= 0 or bird.bottom >= HEIGHT:
        pygame.quit()
        sys.exit()

    # Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.update()
    clock.tick(60)
