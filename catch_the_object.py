import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Define constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (173, 216, 230)  # Light blue
BASKET_COLOR = (255, 0, 0)  # Red
HEN_COLOR = (255, 255, 255)  # White
BASKET_WIDTH, BASKET_HEIGHT = 100, 20
HEN_WIDTH, HEN_HEIGHT = 40, 40
BASKET_SPEED = 10
HEN_SPEED = 5  # Initialize globally

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Hen!")

# Load the basket and hen images
basket_img = pygame.Surface((BASKET_WIDTH, BASKET_HEIGHT))
basket_img.fill(BASKET_COLOR)
hen_img = pygame.Surface((HEN_WIDTH, HEN_HEIGHT))
hen_img.fill(HEN_COLOR)

# Define the basket and hen positions
basket_x = SCREEN_WIDTH // 2 - BASKET_WIDTH // 2
basket_y = SCREEN_HEIGHT - BASKET_HEIGHT - 10
hen_x = random.randint(0, SCREEN_WIDTH - HEN_WIDTH)
hen_y = 0

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game over flag
game_over = False

# Game clock
clock = pygame.time.Clock()

# Game loop
def game_loop():
    global basket_x, hen_x, hen_y, score, game_over, HEN_SPEED  # Declare HEN_SPEED as global

    while not game_over:
        screen.fill(BACKGROUND_COLOR)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Move the basket
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            basket_x -= BASKET_SPEED
        if keys[pygame.K_RIGHT]:
            basket_x += BASKET_SPEED

        # Keep the basket within screen bounds
        if basket_x < 0:
            basket_x = 0
        if basket_x > SCREEN_WIDTH - BASKET_WIDTH:
            basket_x = SCREEN_WIDTH - BASKET_WIDTH

        # Move the hen
        hen_y += HEN_SPEED

        # Check if hen is caught
        if basket_x < hen_x < basket_x + BASKET_WIDTH and hen_y + HEN_HEIGHT >= basket_y:
            score += 1
            hen_x = random.randint(0, SCREEN_WIDTH - HEN_WIDTH)
            hen_y = 0
            HEN_SPEED += 0.5  # Increase difficulty

        # Check if hen hits the ground
        if hen_y > SCREEN_HEIGHT:
            game_over_screen()
            return

        # Draw the basket and hen
        screen.blit(basket_img, (basket_x, basket_y))
        screen.blit(hen_img, (hen_x, hen_y))

        # Display the score
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.update()

        # Cap the frame rate
        clock.tick(30)

# Game over screen
def game_over_screen():
    global game_over
    screen.fill(BACKGROUND_COLOR)
    game_over_text = font.render("Game Over! Press R to restart or Q to quit", True, (0, 0, 0))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 20))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart game
                    reset_game()
                    return
                elif event.key == pygame.K_q:  # Quit game
                    pygame.quit()
                    sys.exit()

# Reset the game
def reset_game():
    global hen_x, hen_y, score, game_over, HEN_SPEED
    hen_x = random.randint(0, SCREEN_WIDTH - HEN_WIDTH)
    hen_y = 0
    score = 0
    game_over = False
    HEN_SPEED = 5  # Reset the speed
    game_loop()

# Start the game
game_loop()
