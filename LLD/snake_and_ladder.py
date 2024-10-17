"""
Designing Snake and Ladder Game
Requirements:
The game should be played on a board with numbered cells, typically with 100 cells.
The board should have a predefined set of snakes and ladders, connecting certain cells.
The game should support multiple players, each represented by a unique game piece.
Players should take turns rolling a dice to determine the number of cells to move forward.
If a player lands on a cell with the head of a snake, they should slide down to the cell with the tail of the snake.
If a player lands on a cell with the base of a ladder, they should climb up to the cell at the top of the ladder.
The game should continue until one of the players reaches the final cell on the board.
The game should handle multiple game sessions concurrently, allowing different groups of players to play independently.
"""

import random
import threading

class GamePiece:
    # SOLID: Single Responsibility Principle - Represents a game piece with a specific color
    def __init__(self, color: str):
        self.color = color

class Player:
    # SOLID: Single Responsibility Principle - Represents a player with a name, game piece, and position
    def __init__(self, name, piece: GamePiece):
        self.name = name
        self.piece = piece
        self.currentPosition = 0

    def movePiece(self, diceValue):
        if self.currentPosition + diceValue > 100:
            return
        self.currentPosition += diceValue

class Cell:
    # SOLID: Single Responsibility Principle - Represents a cell on the board
    def __init__(self, number: int):
        self.number = number

class Snake:
    # SOLID: Single Responsibility Principle - Represents a snake with a head and a tail cell
    def __init__(self, head: Cell, tail: Cell):
        self.head = head
        self.tail = tail

class Ladder:
    # SOLID: Single Responsibility Principle - Represents a ladder with a top and base cell
    def __init__(self, top: Cell, base: Cell):
        self.top = top
        self.base = base

class Board:
    # SOLID: Single Responsibility Principle - Represents the board with snakes and ladders
    BOARD_SIZE = 100

    def __init__(self, snakes: list[Snake], ladders: list[Ladder]):
        self.cells = [Cell(i) for i in range(1, self.BOARD_SIZE + 1)]
        self.snakes = snakes
        self.ladders = ladders

    def getNewPositionAfterSnakesAndLadders(self, position):
        for snake in self.snakes:
            if snake.head.number == position:
                print(f"Snake Bites {snake.head.number} to {snake.tail.number}")
                return snake.tail.number

        for ladder in self.ladders:
            if ladder.base.number == position:
                print(f"Ladder Moves {ladder.base.number} to {ladder.top.number}")
                return ladder.top.number

        return position

class Game:
    # Design Pattern: Light weight Facade - Simplifies the process of starting and managing the game
    # SOLID: Single Responsibility Principle - Manages a game session
    def __init__(self, players, board):
        self.players = players
        self.board = board
        self.currentPlayerIndex = 0

    def startGame(self):
        while not self.checkWinner():
            diceValue = self.rollDice()
            self.moveCurrentPlayer(diceValue)
            self.currentPlayerIndex = (self.currentPlayerIndex + 1) % len(self.players)

    def rollDice(self):
        return random.randint(1, 6)

    def moveCurrentPlayer(self, diceValue):
        player = self.players[self.currentPlayerIndex]
        player.movePiece(diceValue)
        newPosition = player.currentPosition
        player.currentPosition = self.board.getNewPositionAfterSnakesAndLadders(newPosition)

    def checkWinner(self):
        for player in self.players:
            if player.currentPosition == self.board.BOARD_SIZE:
                print(f"{player.name} wins!")
                return True
        return False

class GameManager:
    # Design Pattern: Singleton - Ensures only one instance of GameManager exists
    # SOLID: Single Responsibility Principle - Manages multiple game sessions
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        self.games = []

    @staticmethod
    def get_instance():
        if not GameManager._instance:
            with GameManager._lock:
                if not GameManager._instance:
                    GameManager._instance = GameManager()
        return GameManager._instance

    def startNewGame(self, players):
        snakes = [Snake(Cell(15), Cell(5)), Snake(Cell(40), Cell(20))]
        ladders = [Ladder(Cell(30), Cell(10)), Ladder(Cell(60), Cell(35))]
        board = Board(snakes, ladders)
        game = Game(players, board)
        self.games.append(game)
        threading.Thread(target=game.startGame).start()

if __name__ == "__main__":
    game_manager = GameManager.get_instance()
    player_1 = Player("Player 1", GamePiece("red"))
    player_2 = Player("Player 2", GamePiece("blue"))
    player_3 = Player("Player 3", GamePiece("green"))

    players_A = [player_1, player_2, player_3]

    # Start game 1
    game_manager.startNewGame(players_A)

    player_1 = Player("Player 4", GamePiece("red"))
    player_2 = Player("Player 5", GamePiece("blue"))
    player_3 = Player("Player 6", GamePiece("green"))
    player_4 = Player("Player 7", GamePiece("yellow"))
    players_B = [player_1, player_2, player_3, player_4]

    # Start game 2
    game_manager.startNewGame(players_B)


"""
Explaination:

Classes, Interfaces and Enumerations:
The Board class represents the game board with a fixed size (e.g., 100 cells). It contains the positions of snakes and ladders and provides methods to initialize them and retrieve the new position after encountering a snake or ladder.
The Player class represents a player in the game, with properties such as name and current position on the board.
The Snake class represents a snake on the board, with properties for the start and end positions.
The Ladder class represents a ladder on the board, with properties for the start and end positions.
The Dice class represents a dice used in the game, with a method to roll the dice and return a random value between 1 and 6.
The SnakeAndLadderGame class represents a single game session. It initializes the game with a board, a list of players, and a dice. The play method handles the game loop, where players take turns rolling the dice and moving their positions on the board. It checks for snakes and ladders and updates the player's position accordingly. The game continues until a player reaches the final position on the board.
The GameManager class is a singleton that manages multiple game sessions. It maintains a list of active games and provides a method to start a new game with a list of player names. Each game is started in a separate thread to allow concurrent game sessions.
The SnakeAndLadderDemo class demonstrates the usage of the game by creating an instance of the GameManager and starting two separate game sessions with different sets of players.
"""