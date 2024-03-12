import random

class Game:
    def __init__(self):
        self.board = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()

    def add_random_tile(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] == 0]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = 2 if random.random() < 0.9 else 4

    def move(self, direction):
        if direction == 'up':
            self.board = self.transpose(self.board)
            self.board = self.move_left(self.board)
            self.board = self.transpose(self.board)
        elif direction == 'down':
            self.board = self.transpose(self.board)
            self.board = self.reverse_rows(self.board)
            self.board = self.move_left(self.board)
            self.board = self.reverse_rows(self.board)
            self.board = self.transpose(self.board)
        elif direction == 'left':
            self.board = self.move_left(self.board)
        elif direction == 'right':
            self.board = self.reverse_rows(self.board)
            self.board = self.move_left(self.board)
            self.board = self.reverse_rows(self.board)

        self.add_random_tile()

    def move_left(self, board):
        new_board = []
        for row in board:
            row = [val for val in row if val != 0]
            row += [0] * (4 - len(row))

            for i in range(len(row) - 1):
                if row[i] == row[i + 1]:
                    row[i], row[i + 1] = row[i] * 2, 0
                    self.score += row[i]

            row = [val for val in row if val != 0]
            row += [0] * (4 - len(row))
            new_board.append(row)
        return new_board

    def reverse_rows(self, board):
        return [row[::-1] for row in board]

    def transpose(self, board):
        return [list(row) for row in zip(*board)]

# Example usage:
# game = Game()
# print(game.board)
# game.move('up')
# print(game.board)
