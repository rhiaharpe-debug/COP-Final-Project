"""Sudoku game entry point. The TODOs in the three screen functions are for the team to complete."""

import pygame as p

from board import Board


# These dimensions are examples. Board currently draws the top edge of the grid at y = 165.
WINDOW_SIZE = (600, 750)
BOARD_SIZE = 450


def choose_difficulty(screen):
    """Show the start screen and return "easy", "medium", or "hard". Return None if the window closes."""
    # TODO: Draw the title and the three difficulty buttons.
    # TODO: Wait for a button click in the event loop and return the selected difficulty.
    pass


def play_game(screen, board):
    """Run one game. Return "win" or "lose" when the board is full, "restart" on Restart, or None on exit."""
    # TODO: Each frame, call board.draw(), draw the Reset, Restart, and Exit buttons, then refresh the screen.
    # TODO: On a board click, call board.click(x, y). If it returns a row and column, pass them to board.select(row, col).
    # TODO: Use the arrow keys to move the selection. Keep both the row and column between 0 and 8.
    # TODO: When the player presses a number key from 1 to 9, call board.sketch(value).
    # TODO: On Enter, read the selected cell's sketched_value. If it is nonzero, pass it to board.place_number().
    # TODO: After placing a number, call board.is_full(). If the board is full, return "win" if board.check_board() is true or "lose" otherwise.
    # TODO: On Reset, call board.reset_to_original() and continue the current game.
    # TODO: On Restart, return "restart". On Exit or window close, return None.
    pass


def show_result(screen, result):
    """Show the win or loss screen. Return "restart" if the player chooses to play again, or None on exit."""
    # TODO: Draw the screen for "win" or "lose", then wait for a button click or the window to close.
    pass


def main():
    """Set up the window, let the player choose a difficulty, run the game, and show the result when the board is full."""
    p.init()
    screen = p.display.set_mode(WINDOW_SIZE)
    p.display.set_caption("Sudoku")

    while True:
        difficulty = choose_difficulty(screen)
        if difficulty is None:
            break

        board = Board(BOARD_SIZE, BOARD_SIZE, screen, difficulty)
        result = play_game(screen, board)
        if result is None:
            break
        if result == "restart":
            continue

        if show_result(screen, result) != "restart":
            break

    p.quit()


if __name__ == "__main__":
    main()



