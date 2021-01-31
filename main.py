import numpy as np

board = np.array( [[0,7,0,3,0,0,0,0,9],
					[5,0,0,0,0,0,8,0,0],
					[3,0,1,0,4,9,0,5,0],
					[0,0,0,0,0,0,0,0,0],
					[9,3,0,2,0,0,4,0,0],
					[1,8,0,6,0,0,9,0,7],
					[8,4,0,9,0,0,0,0,0],
					[0,2,0,0,0,4,0,1,0],
					[0,0,0,0,0,0,5,0,0] ])



def encontra_zero(board):
	for i in range(9):
		for j in range(9):
			if board[i][j] == 0:
				return i,j
	return None


def resolve(board):
	if encontra_zero(board) == None:
		print('z')
		return board
	else:
		linha,coluna = encontra_zero(board)
		for num in range(1,10):
			if valido(board,linha,coluna,num):
				board[linha][coluna] = num
				resolve(board)
		board[linha][coluna] = 0
		return



def valido(board,linha,coluna,num):
	for i in range(9):
		if board[linha][i] == num:
			return False

	for i in range(9):
		if board[i][coluna] == num:
			return False

	a = linha//3
	b = coluna//3
	for i in range(3):
		for j in range(3):
			if board[a*3 + i][b*3 + j] == num:
				return False

	return True
