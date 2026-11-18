
import pygame as p
from cell import Cell


class Board:
    def __init__(self, width, height, screen, difficulty):

        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        self.rows = 9
        self.cols = 9

        # Board size and position
        self.cell_size = self.width // 9
        self.x = (self.screen.get_width() - self.width) // 2
        self.y = 165

        self.selected = None

        # Temporary empty board
        self.board = [
            [0 for col in range(9)]
            for row in range(9)
        ]

        # Save original board
        self.original_board = [
            row.copy() for row in self.board
        ]

        # Create Cell objects
        self.cells = [
            [
                Cell(self.board[row][col], row, col, screen)
                for col in range(9)
            ]
            for row in range(9)
        ]

        # Set size and position for every Cell
        for row in self.cells:
            for cell in row:
                cell.size = self.cell_size
                cell.offset_x = self.x
                cell.offset_y = self.y

        # Load board image
        self.board_image = p.image.load(
            "assets/board.png"
        ).convert_alpha()

        self.board_image = p.transform.smoothscale(
            self.board_image,
            (self.width, self.height)
        )

    def draw(self):

        # Draw board image
        self.screen.blit(
            self.board_image,
            (self.x, self.y)
        )

        # Draw all 81 cells
        for row in self.cells:
            for cell in row:
                cell.draw()

    # Select a cell and input value
    def select(self, row, col):
        if self.selected is not None:
            old_row, old_col = self.selected
            self.cells[old_row][old_col].selected = False

        self.selected = (row, col)
        self.cells[row][col].selected = True

    # Click Cell
    def click(self, x, y):
        pass

    # Sketch Numbers
    def sketch(self, value):
        pass

    # Write each Cell.value back to the corresponding position
    # in self.board to make the digital chessboard consistent
    # with the screen.
    def update(self, value):
        pass

    # Press Enter to input sketch number
    def place_number(self, value):
        pass

    # Clear input Sketch
    def clear(self):
        pass

    # Restart the original game
    def reet_to_original(self):
        pass

    # Find an empty cell
    def find_empty(self):
        pass

    # Return False if cell is empty
    def is_full(self):
        pass

    # Final check of answers weather input is correct or not
    def check_board(self):
        pass
