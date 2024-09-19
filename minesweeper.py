import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Define constants
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
GRID_SIZE = 10  # 10x10 grid
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE
NUM_MINES = 10

# Colors
BACKGROUND_COLOR = (189, 189, 189)
LINE_COLOR = (0, 0, 0)
HIDDEN_COLOR = (160, 160, 160)
MINE_COLOR = (255, 0, 0)
TEXT_COLOR = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Minesweeper")

# Font for rendering text
font = pygame.font.Font(None, 36)

# Create grid
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
revealed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
mines = set()

# Place mines randomly
while len(mines) < NUM_MINES:
    x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
    if (x, y) not in mines:
        mines.add((x, y))

# Set mine indicators
for mine_x, mine_y in mines:
    for i in range(mine_x - 1, mine_x + 2):
        for j in range(mine_y - 1, mine_y + 2):
            if 0 <= i < GRID_SIZE and 0 <= j < GRID_SIZE and (i, j) not in mines:
                grid[i][j] += 1

# Game over flag
game_over = False

# Draw the grid lines and cells
def draw_grid():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            rect = pygame.Rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if revealed[i][j]:
                if (i, j) in mines:
                    pygame.draw.rect(screen, MINE_COLOR, rect)  # Draw mines as red
                else:
                    pygame.draw.rect(screen, BACKGROUND_COLOR, rect)
                    if grid[i][j] > 0:
                        text = font.render(str(grid[i][j]), True, TEXT_COLOR)
                        screen.blit(text, (i * CELL_SIZE + 10, j * CELL_SIZE + 5))
            else:
                pygame.draw.rect(screen, HIDDEN_COLOR, rect)
            pygame.draw.rect(screen, LINE_COLOR, rect, 1)

# Reveal cells recursively (flood fill) for empty spaces
def reveal_cell(x, y):
    if revealed[x][y] or (x, y) in mines:
        return
    revealed[x][y] = True
    if grid[x][y] == 0:
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < GRID_SIZE and 0 <= j < GRID_SIZE:
                    reveal_cell(i, j)

# Check for game over
def check_game_over():
    for mine in mines:
        if revealed[mine[0]][mine[1]]:
            return True
    return False

# Check if the player has won (all non-mine cells are revealed)
def check_win():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (i, j) not in mines and not revealed[i][j]:
                return False
    return True

# Game loop
def game_loop():
    global game_over
    while True:
        screen.fill(BACKGROUND_COLOR)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouse_x, mouse_y = event.pos
                grid_x, grid_y = mouse_x // CELL_SIZE, mouse_y // CELL_SIZE
                
                if event.button == 1:  # Left click
                    if (grid_x, grid_y) in mines:  # If clicked on a mine
                        reveal_all_mines()  # Show all mines
                        game_over_screen("Game Over")
                        return
                    else:
                        reveal_cell(grid_x, grid_y)
                
                # Check if player has won
                if check_win():
                    reveal_all_mines()  # Optional, to reveal everything
                    game_over_screen("You Won!")
                    return

        # Draw the game grid
        draw_grid()

        # Update the display
        pygame.display.update()

# Reveal all mines in case of game over or win
def reveal_all_mines():
    global revealed
    for mine in mines:
        revealed[mine[0]][mine[1]] = True

# Display game over or win message
def game_over_screen(message):
    screen.fill(BACKGROUND_COLOR)
    text = font.render(message, True, TEXT_COLOR)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

# Start the game
game_loop()
