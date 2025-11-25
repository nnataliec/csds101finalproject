import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
board = [[None]*3 for _ in range(3)]
def draw_grid():
    SCREEN.fill(WHITE)
    # Vertical lines
    pygame.draw.line(SCREEN, BLACK, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(SCREEN, BLACK, (400, 0), (400, 600), LINE_WIDTH)
    # Horizontal lines
    pygame.draw.line(SCREEN, BLACK, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(SCREEN, BLACK, (0, 400), (600, 400), LINE_WIDTH)
player = "X"
def draw_marks():
    font = pygame.font.Font(None, 150)
    for row in range(3):
        for col in range(3):
            if board[row][col]:
                mark = font.render(board[row][col], True, RED if board[row][col] == "X" else BLUE)
                SCREEN.blit(mark, (col * 200 + 50, row * 200 + 50))
def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] and row[0]:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col]:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2]:
        return board[0][2]
    return None
running = True
while running:
    draw_grid()
    draw_marks()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // 200, x // 200
            if not board[row][col]:
                board[row][col] = player
                winner = check_winner()
                if winner:
                    print(f"{winner} wins!")
                    running = False
                player = "O" if player == "X" else "X"
def reset_game():
    global board, player
    board = [[None]*3 for _ in range(3)]
    player = "X"
