class TicTacToe:
    def __init__(self) -> None:
        self.current_player = 'X'
        self.board = self._create_board()
        self.playing = True

    def _create_board(self):
        board = []
        for _ in range(3):
            board.append([None, None, None])
        return board

    def set_spot(self, coordinate):
        # if spot is taken, raise an error
        row, col = coordinate
        if self.board[row][col] is not None:
            raise Exception("Spot is already taken")
        self.board[row][col] = self.current_player

    def _swap_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        elif self.current_player == 'O':
            self.current_player = 'X'

    def check_board_for_winner(self):
        """
        We can 
         - check all rows
         - check all cols
         - check the diagonals
        """
        if self._check_rows():
            return True
        if self._check_cols():
            return True
        if self._check_diagonals():
            return True
        return False


    def _check_rows(self):
        for row in self.board:
            player = row[0]
            if player is None:
                continue
            if all(map(lambda ch: ch == player, row)):
                return True
        return False

    def _check_cols(self):
        for col in range(3):
            tmp_col = []
            for row in self.board:
                tmp_col.append(row[col])

            player = tmp_col[0]
            if player is None:
                continue
            if all(map(lambda ch: ch == player, tmp_col)):
                return True
        return False

    def _check_diagonals(self):
        """
        For a 3x3, we really just need to check two sets of 3.
        """
        diagonal0 = [self.board[0][0], self.board[1][1], self.board[2][2]]
        player = diagonal0[0]
        if all(map(lambda ch: ch == player, diagonal0)) and player is not None:
            return True
        
        diagonal1 = [self.board[2][0], self.board[1][1], self.board[0][2]]
        player = diagonal1[0]
        if all(map(lambda ch: ch == player, diagonal1)) and player is not None:
            return True
       
        return False

    def is_stalemate(self):
        for row in self.board:
            for col in row:
                if col is None:
                    return False
        return True

    def print_board(self):
        for i, row in enumerate(self.board):
            row_builder = []
            for j, val in enumerate(row):
                if val:
                    value = f"[{val}]"
                else: 
                    value = f"[{i},{j}]"
                row_builder.append(value)
            print("\t".join(row_builder))

    def play(self):
        print("Let's play Tic Tac Toe!")
        while self.playing:
            self.print_board()
            coordinates = input(f"Player {self.current_player}, select a square: row,col:")
            coordinates = map(int, coordinates.split(','))
            self.set_spot(coordinates)
            if self.check_board_for_winner():
                print(f"{self.current_player} is the winner!")
                self.print_board()
                self.playing = False
            if self.is_stalemate():
                print(f"Stalemate there is no winner.")
                self.print_board()
                self.playing = False
            self._swap_player()


if __name__ == '__main__':
    tic_tac_toe = TicTacToe()
    tic_tac_toe.play()