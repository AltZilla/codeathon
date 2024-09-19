import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
FONT_COLOR = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# Board
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
font = pygame.font.Font(None, 36)

def draw_lines():
    # Draw horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE * 2), (WIDTH, SQUARE_SIZE * 2), LINE_WIDTH)

    # Draw vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE * 2, 0), (SQUARE_SIZE * 2, HEIGHT), LINE_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)

def check_win(player):
    # Check rows
    for row in range(BOARD_ROWS):
        if all([s == player for s in board[row]]):
            return True

    # Check columns
    for col in range(BOARD_COLS):
        if all([board[row][col] == player for row in range(BOARD_ROWS)]):
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(BOARD_ROWS)]) or all([board[i][BOARD_ROWS - 1 - i] == player for i in range(BOARD_ROWS)]):
        return True

    return False

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    global board
    board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def show_winner(winner):
    text = font.render(f"{winner} wins!", True, FONT_COLOR)
    replay_text = font.render("Press R to replay or Q to quit.", True, FONT_COLOR)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 - 20))
    screen.blit(replay_text, (WIDTH // 2 - replay_text.get_width() // 2, HEIGHT // 2 + text.get_height() // 2 + 10))
    pygame.display.update()

def main():
    draw_lines()
    player = 'X'
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                row = mouseY // SQUARE_SIZE
                col = mouseX // SQUARE_SIZE

                if board[row][col] is None:
                    mark_square(row, col, player)
                    if check_win(player):
                        game_over = True
                        show_winner(player)
                    player = 'O' if player == 'X' else 'X'
                    draw_figures()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_over:
                    restart()
                    game_over = False
                    player = 'X'
                elif event.key == pygame.K_q and game_over:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main()
