class TTT:

	def __init__(self):
		self._board = [ [' '] * 3 for j in range(3) ]
		self._player = 'X'

	def mark(self, x_position, y_position):
		if not (0 <= x_position <= 2 and 0 <= y_position <= 2):
			raise ValueError( 'Position out of range' )
		if self._board[x_position][y_position] != ' ':
			raise ValueError( 'Position has been used' )
		if self.find_who_win() is not None:
			raise ValueError( 'Someone has won' )
		self._board[x_position][y_position] = self._player
		if self._player == 'O':
			self._player = 'X'
		else:
			self._player = 'O'
			
	def find_who_win(self):
		for mark in 'XO' :
			if self.check_win(mark):
				return mark
			return None		

	def check_win(self, mark):
		board = self._board
		return (mark == board[0][0] == board[0][1] == board[0][2] or
			mark == board[1][0] == board[1][1] == board[1][2] or
			mark == board[2][0] == board[2][1] == board[2][2] or
			mark == board[0][0] == board[1][0] == board[2][0] or 
			mark == board[0][1] == board[1][1] == board[2][1] or 
			mark == board[0][2] == board[1][2] == board[2][2] or
			mark == board[0][0] == board[1][1] == board[2][2] or 
			mark == board[0][2] == board[1][1] == board[2][0]) 

	def __str__ (self):
		line_in_board = [ '|'.join(self._board[r]) for r in range(3)]
		return '\n-----\n' .join(line_in_board)


game = TTT()

game.mark(1,1)
game.mark(2,2)
game.mark(1,0)
game.mark(0,1)
game.mark(1,2)

print(game)

find_who_win = game.find_who_win()

if find_who_win is None:
	print('Result game: TIE')
else:
	print(find_who_win, 'wins')