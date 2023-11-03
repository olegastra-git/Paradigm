class Game:
    def __init__(self):
        self.board = self.create_board()
        self.current_player = 'X'

    def create_board(self):
        return [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        print('---------')
        for row in self.board:
            print('|', end='')
            for cell in row:
                print(cell, end='|')
            print('\n---------')

    def is_winner(self, player):
        # Проверка строк
        for row in self.board:
            if row.count(player) == 3:
                return True

        # Проверка столбцов
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == player:
                return True

        # Проверка диагоналей
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

        return False

    def is_draw(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def mark_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def play_game(self):
        while True:
            self.print_board()
            row = int(input('Введите номер строки (0-2): '))
            col = int(input('Введите номер столбца (0-2): '))

            if self.mark_move(row, col):
                if self.is_winner(self.current_player):
                    print(f'Игрок {self.current_player} победил!')
                    break
                elif self.is_draw():
                    print('Ничья!')
                    break
                else:
                    self.current_player = 'O' if self.current_player == 'X' else 'X'
            else:
                print('Не правильно ты дядя Федор ходишь. Попробуй еще раз.')

game = Game()
game.play_game()