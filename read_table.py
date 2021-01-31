from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import numpy as np


driver = webdriver.Chrome("chromedriver_win32\\chromedriver")
wait = WebDriverWait(driver,3000)


driver.get('https://www.sudokupeople.com/')


element = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[14]')
element.click()
element = driver.find_element_by_xpath('/html/body/div[1]/div[3]/button[6]')
element.click()
time.sleep(2)


board = np.zeros((9,9), dtype=int)

print( board )

global final_board
global finish
finish = False

for p in range(1,4):
	for k in range(1,4):
		for j in range(1,4):
			for i in range(1,4):
				element = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[{}]/div[{}]/div[{}]/div[{}]/div[1]'.format(p,k,j,i))
				print(element.get_attribute('innerHTML'))
				if element.get_attribute('innerHTML') == '':
					print(0)
				else:
					board[(p-1)*3+(j-1)][(k-1)*3+(i-1)]=int(element.get_attribute('innerHTML'))

print(board)


def encontra_zero(board):
	for i in range(9):
		for j in range(9):
			if board[i][j] == 0:
				return i,j
	return None


def resolve(board):
	global final_board 
	global finish
	if encontra_zero(board) == None:
		print('\n...'*4)
		print(board)
		if finish == False:
			final_board = board
			print('tentando tornar global')
			print(final_board)
			finish == True
		return False
	else:
		linha,coluna = encontra_zero(board)
		for num in range(1,10):
			if valido(board,linha,coluna,num):
				board[linha][coluna] = num
				if resolve(board) == False:
					return False
				else:
					board[linha][coluna] = 0
		return True



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

resolve(board)

print('\n\nteste final:::::')
print(final_board)

for p in range(1,4):
	for k in range(1,4):
		for j in range(1,4):
			for i in range(1,4):
				element = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[{}]/div[{}]/div[{}]/div[{}]/div[1]'.format(p,k,j,i))
				print(element)
				if element.get_attribute('innerHTML') == '':
					print('elemento vazio localizado')
					print('inserindo o valor em -- ',(p-1)*3+(j-1),(k-1)*3+(i-1))
					element = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[{}]/div[{}]/div[{}]/div[{}]'.format(p,k,j,i))
					element.click()
					time.sleep(.1)

					number_choice = driver.find_element_by_xpath('html/body/div[2]/div/div[2]/div[{}]'.format(final_board[(p-1)*3+(j-1)][(k-1)*3+(i-1)]))
					number_choice.click()

