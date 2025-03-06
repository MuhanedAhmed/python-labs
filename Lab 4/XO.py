import os
from time import sleep

# ====================== Helper Functions ====================== #

def print_delay_alone(msg:str="", delay:int=0, alone:bool=False):
  if (alone):
    os.system("cls" if os.name == "nt" else "clear")
  if (len(msg) > 0):
    print(msg)
  if (delay > 0):
    sleep(delay)

# ==================================== Player Class ==================================== #

class Player:
  
  def __init__(this):
    this.__name = ""
    this.__symbol = ""

  # name property
  @property
  def name(this):
    return this.__name
  
  @name.setter
  def name(this, value):
    this.__name = value

  # symbol property
  @property
  def symbol(this):
    return this.__symbol
  
  @symbol.setter
  def symbol(this, player_symbol):
    this.__symbol = player_symbol
  
# ==================================== Menu Class ==================================== #

class Menu:
  def main_menu(this):
    print_delay_alone(msg="\n#======== Welcome to X-O Game ========#\n", alone=True)
    print("1) Start Game")
    print("2) Quit Game")
    
    while True:
      match(input("\n>>")):
        case "1": return 1
        case "2": return 2
        case _: print("Invalid Option. Choose 1 or 2 !!!")
  
  def end_menu(this):
    print_delay_alone(msg="\n#======== Game Over ========#\n")
    print("1) Restart Game")
    print("2) Quit Game")
    
    while True:
      match(input("\n>>")):
        case "1": return 1
        case "2": return 2
        case _: print("Invalid Option. Choose 1 or 2 !!!")

# ==================================== Board Class ==================================== #

class Board:
  def __init__(this):
    this.game_board = [str(x) for x in range(1, 10)]
    this.available_symbols = {"X" : 1, "O" : 1}
  
  def display_board(this):
    for i in range(9):
      if (i % 3 == 0) or (i % 3 == 1):
        print(f" {this.game_board[i]}",end=" |")
      else:
        print(f" {this.game_board[i]}")
        print("-"*11)

  def update_board(this, symbol, number):
    if (1 <= number <= 9) and (this.game_board[number - 1].isdigit()):
      this.game_board[number - 1] = symbol
      return True
    
    return False
  
  def reset_board(this):
    this.game_board = [str(x) for x in range(1, 10)]

  def untaken_symbols(this):
    return [key for key, value in this.available_symbols.items() if value == 1]

# ==================================== Game Class ==================================== #

class Game:
  def __init__(this):
    this.players = [Player(), Player()]
    this.board = Board()
    this.menu = Menu()
    this.current_player_index = 0

  def start_game(this):
    match(this.menu.main_menu()):
        case 1: 
          this.setup_players()
          this.play_game()
        case 2: 
          this.quit_game()
      
  def setup_players(this):
    print_delay_alone(msg="\n#======== Player Setup ========#\n", alone=True)
    for i in range(2):  
      player_name = input(f"Enter player {i+1} name (legal letters only) : ")
      while not player_name.isalpha():
        print("Error in player name")
        player_name = input(f"Enter player {i+1} name (legal letters only) : ")
      this.players[i].name = player_name

      player_symbol = input(f"Enter player {i+1} symbol {this.board.untaken_symbols()}: ")
      while player_symbol not in this.board.untaken_symbols():
        print("Error in player symbol")
        player_symbol = input(f"Enter player {i+1} symbol {this.board.untaken_symbols()}: ")
      this.players[i].symbol = player_symbol
      this.board.available_symbols[player_symbol] = 0

      print("="*50)

  def play_game(this):
    while True:
      this.play_turn()
      if this.check_win() or this.check_draw():
        match(this.menu.end_menu()):
          case 1: 
            this.restart_game()
            break
          case 2: 
            this.quit_game()
            break

  def quit_game(this):
    print_delay_alone(msg="#======== Thank you for playing X-O Game ========#",delay=3, alone=True)

  def play_turn(this):
    print_delay_alone(alone=True)
    player = this.players[this.current_player_index]
    this.board.display_board()
    print(f"{player.name}'s turn ({player.symbol})")

    choice = int(input("Choose a cell : "))
    while not this.board.update_board(player.symbol,choice):
      print("Invalid Cell !!!")
      choice = input("Choose a cell : ")

    this.current_player_index = 1 - this.current_player_index


  def restart_game(this):
    print_delay_alone(alone=True)
    this.board.reset_board()
    this.current_player_index = 0
    this.play_game()

  def check_win(this):
    win_patterns = [
      [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
      [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
      [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for pattern in win_patterns:
      if (this.board.game_board[pattern[0]] == this.board.game_board[pattern[1]] == this.board.game_board[pattern[2]]):
        print_delay_alone(msg=f"\n***** Congratulations *****\n{this.players[this.current_player_index].name} has won the game !!!\n\n", alone=True)
        this.board.display_board()
        print_delay_alone(delay=3)
        return True

    return False
  
  def check_draw(this):
    if all(not cell.isdigit() for cell in this.board.game_board):
      print_delay_alone(msg=f"\n***** Draw *****\nNo player has won the game !!!\n\n", alone=True)
      this.board.display_board()
      print_delay_alone(delay=3)
      return True

    return False  

# ==================================== Main Program ==================================== #

game = Game()
game.start_game()
