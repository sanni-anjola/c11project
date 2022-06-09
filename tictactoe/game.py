from tictactoe.board import Board
from tictactoe.player import Player


class Game:
    def __init__(self, player_one: Player, player_two: Player) -> None:
        self.game_board = Board()
        self.player_one = player_one
        self.player_two = player_two

    def play(self, player: Player, position: int):
        print(f"{player.name}'s turn")
        self.game_board.fill_cell(position, player.sign)

    def show_board(self):
        self.game_board.display_board()

    def determine_winner(self) -> int:
        player_one_winning_score = ord(self.player_one.sign) * 3
        player_two_winning_score = ord(self.player_two.sign) * 3

        for i in range(3):
            row_sum = sum(ord(cell) for idx, cell in enumerate(self.game_board.board) if cell != '' and idx // 3 == i)
            col_sum = sum(ord(cell) for idx, cell in enumerate(self.game_board.board) if cell != '' and idx % 3 == i)

            if row_sum == player_one_winning_score or col_sum == player_one_winning_score:
                return 1
            if row_sum == player_two_winning_score or col_sum == player_two_winning_score:
                return 2

        right_diag_sum = sum(ord(cell) for idx, cell in enumerate(self.game_board.board) if cell != '' and idx % 3 == idx // 3)
        left_diag_sum = sum(ord(cell) for idx, cell in enumerate(self.game_board.board) if cell != '' and (idx % 3) + (idx // 3) == 2)

        if right_diag_sum == player_one_winning_score or left_diag_sum == player_one_winning_score:
            return 1
        if right_diag_sum == player_two_winning_score or left_diag_sum == player_two_winning_score:
            return 2

        return 0

    def announce_winner(self) -> str:
        winner: int = self.determine_winner()

        match winner:
            case 0:
                return "It's a tie"
            case 1:
                return f"{self.player_one.name} won"
            case 2:
                return f"{self.player_two.name} won"
            case _:
                raise NotImplementedError("")


if __name__ == '__main__':
    player1 = Player("Stephen", 'X')
    player2 = Player("Amaka", 'O')
    game = Game(player1, player2)
    game.play(player2, 2)
    game.play(player1, 4)
    game.play(player2, 5)

    game.play(player1, 6)
    game.play(player2, 8)
    game.play(player1, 3)
    game.show_board()
    print(game.announce_winner())
