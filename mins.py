import random
import os
n = 9									
m = 9	

mat = [['O' for x in range(n)] for y in range(m)]
bombs = [['O' for x in range(n)] for y in range(m)]

def rnd(x1, x2):
	x =random.randrange(x1, x2)
	return x


def check(x, y):
	if bombs[y][x] == '*':
		x = rnd(0, n)
		y = rnd(0, m)
		check(x, y)
	else:
		bombs[y][x] = '*'


def plant(k):
	count = 0
	while count != k:
		x = rnd(0, n)
		y = rnd(0, m)
		check(x, y)
		count += 1


def output(ma):
	print(' ' * 2, end="")
	for i in range(n):
		print(str(i)+' ', end=""),
	print('\n' + ' ' * 2 + '-' * n * 2)
	for ii in range(m):
		print(str(ii) + '|', end="")
		for j in range(n):
			print(str(ma[ii][j]) + ' ', end="")
		print()


def check_bombs(x, y):
	list_coords = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
	count_bombs = 0
	for i in list_coords:
		if i[0] >= 0 and i[1] >= 0:
			x1 = i[0]
			y1 = i[1]
			if x1 > n-1 or y1 > m-1:
				continue
			elif bombs[y1][x1] == '*':
				count_bombs += 1
		else:
			continue
	return count_bombs

def check_near_null():
	for i in range(m):
		for j in range(n):
			if mat[i][j] == 0:
				list_coords = [(j - 1, i - 1), (j, i - 1), (j + 1, i - 1), (j - 1, i), (j + 1, i), (j - 1, i + 1), (j, i + 1), (j + 1, i + 1)]
				for ii in list_coords:
					if ii[0] >= 0 and ii[1] >= 0:
						xx = ii[0]
						yy = ii[1]
						if xx > n-1 or yy > m-1:
							continue
						mat[yy][xx] = check_bombs(xx, yy)



def check_nulls(x, y):
	list_coords = [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]
	for i in list_coords:
		if i[0] >= 0 and i[1] >= 0:
			x1 = i[0]
			y1 = i[1]
			if x1 > n-1 or y1 > m-1:
				continue
			elif check_bombs(x1, y1) == 0:
				if mat[y1][x1] == 0:
					continue
				mat[y1][x1] = 0
				check_nulls(x1, y1)
				check_near_null()

plant(10)
output(mat)

while True:
	a = int(input())
	b = int(input())
	try:
		if mat[b][a] == '*':
			print('YOU ARE LOSE!!!')
			break
		elif check_bombs(a, b) == 0:
			check_nulls(a, b)
		else:
			mat[b][a] = check_bombs(a, b)
	except:
		pass
	output(mat)


'''
for i in range(m):
	for j in range(n):
		if mat[i][j] == '*':
			continue
		else: 
			mat[i][j] = check_bombs(j, i)
			'''
