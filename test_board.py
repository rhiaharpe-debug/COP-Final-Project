
#######################################
# THIS IS JUST FOR TESTING
# TEMPORARY
#######################################


import pygame as p
from board import Board

p.init()

# Window settings
WIDTH = 500
HEIGHT = 700
BOARD_SIZE = 396

screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("Board Test")

# Load background
background = p.image.load(
    "assets/background.png"
).convert()

background = p.transform.smoothscale(
    background,
    (WIDTH, HEIGHT)
)

# Create board
board = Board(
    BOARD_SIZE,
    BOARD_SIZE,
    screen,
    "easy"
)

# Temporary test values
board.cells[0][0].set_cell_value(5)
board.cells[4][4].set_sketched_value(3)
board.cells[8][8].selected = True

# Game loop
running = True
clock = p.time.Clock()

while running:

    for event in p.event.get():
        if event.type == p.QUIT:
            running = False

    # Layer 1: Background
    screen.blit(background, (0, 0))

    # Layer 2 and 3: Board and Cells
    board.draw()

    # Update display
    p.display.flip()
    clock.tick(60)

p.quit()
