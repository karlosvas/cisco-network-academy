from random import randrange

def display_board(board):
   for row in board:
      print(
      f"""      +-------+-------+-------+
      |       |       |       |
      |   {row[0]}   |   {row[1]}   |   {row[2]}   |
      |       |       |       |""")
   print("      +-------+-------+-------+")
      
def determinateYX(index_mov):
   if index_mov % 3 == 0:
      y = index_mov // 3 -1 
   else: 
      y = index_mov // 3
   x = index_mov % 3 -1
   return y, x

def draw_move(board, PLAYER):
   try:
      if PLAYER == "X":
         print("Turno de la maquina")
         while True:
            index_mov = randrange(10)
            if any(index_mov in row for row in board):
               y, x = determinateYX(index_mov)
               board[y][x] = "X"
               break
            elif index_mov < 10 & user_select > 0:
               print(f"Esa casilla ya esta siendo utilizada jugador {PLAYER} 😵")
            else:
               raise ValueError
      else:
         print("Tu turno humano")
         while True:
            user_select = int(input("Ingresa tu movimiento: "))
            if any(user_select in row for row in board):
               y, x = determinateYX(user_select)
               board[y][x] = "O"
               break
            elif user_select < 10 & user_select > 0:
               print(f"Esa casilla ya esta siendo utilizada jugador {PLAYER} 😵")
            else:
               raise ValueError
   except (IndexError, ValueError):
      print("Dato no valido, ingrese un indice correcto, < 10")
      enter_move(board, PLAYER)
        
def make_list_of_free_fields(board):
   for i in range(0, 9, 3):
      if i == 3:
         newRow = [i+1, "X", i+3]
      else:
         newRow = [i+1, i+2, i+3]
      board.append(newRow)

def victory_for(board, PLAYER):
   for i in range(3):
      if board[i][0] == board[i][1] == board[i][2] \
         or board[0][i] == board[1][i] == board[2][i] \
         or board[0][0] == board[1][1] == board[2][2] \
         or board[0][2] == board[1][1] == board[2][0]:
               return PLAYER

def main():
   board = []
   make_list_of_free_fields(board)
   display_board(board)
   PLAYER = "O"

   while True:
      draw_move(board, PLAYER)
      display_board(board)

      winner = victory_for(board, PLAYER)
      if winner == "O":
         print("Ganaste 🎉")
         break
      elif winner == "X":
         print("Perdiste 😭")
         break

      PLAYER = "X" if PLAYER == "O" else "O"

main()
