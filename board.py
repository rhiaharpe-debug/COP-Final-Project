
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
    # SAANVI I NEED YOU
    def click(self, x, y):
        pass

    # Sketch Numbers
    # SAANVI I NEED YOU
    def sketch(self, value):
        pass

    # Write each Cell.value back to the corresponding position
    # in self.board to make the digital chessboard consistent
    # with the screen.
    # SAANVI I NEED YOU
    def update(self, value):
        pass

    # Press Enter to input sketch number
    # SAANVI I NEED YOU
    def place_number(self, value):
        pass

    # Clear input Sketch
    def clear(self):
        if self.selected is not None:
            row, col = self.selected
            self.cells[row][col].set_sketched_value(0)
        pass

    # Restart the original game
    def reset_to_original(self):
        self.board = [row.copy() for row in self.original_board]

        for row in range(self.rows):
            for col in range(self.cols):
                self.cells[row][col].set_cell_value(self.board[row][col])
                self.cells[row][col].selected = False

        self.selected = None

    # Find an empty cell
    def find_empty(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == 0:
                    return (row, col)

        return None

    # Return False if cell is empty
    def is_full(self):
        return self.selected is None

    # Final check of answers weather input is correct or not
    def check_board(self):
        if not self.is_full():
            return False
        valid_numbers = set(range(1, 10))

        # Check FOr Horizontal lin
        for row in self.board:
            if set(row) != valid_numbers:
                return False

        # Check for Vertical line
        for col in range(self.cols):
            column = []
            for row in range(self.rows):
                column.append(self.board[row][col])
            if set(column) != valid_numbers:
                return False

        # Check for Subgrid
        for start_row in range(0,9,3):
            for start_col in range(0, 9, 3):
                subgrid = []

                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                        subgrid.append(self.board[row][col])

                if set(subgrid) != valid_numbers:
                    return False

        return True
