#Connway's Game of Life#
#Jamie Bull#
#14/10/2017#

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

#count alive neighbours around given cell#
def countNeighbours(i, j):

	neighbours = 0
	for n in range (i-1, i+2):
		for m in range (j-1, j+2):
			if n != i or m != j:
				if n != grid.shape[0] and m != grid.shape[1] and n >= 0 and m >= 0:
					neighbours += grid[n][m]
	return neighbours
	
#update cell#
def updateCell(i, j):

	n = countNeighbours(i, j)
	if grid[i][j] == 1:
		if n == 2 or n == 3:
			return 1
		elif n < 2 or n > 3:
			return 0
			
	elif grid[i][j] == 0:
		if n == 3:
			return 1
		else:
			return 0
	
#Read seed specified by user to initialise cells#
def readSeed():

	print("Enter the file name of the seed you would like to use:\n"
	      "(expecting format of .lif 1.06 which can be found on conwaylife.com/wiki)\n")
	
	exit = 0
	
	while 1:
		try:
			filename = input()
			if filename == "exit":	#lets user exit program if problem with filename
				exit = 1	#Cannot exit in try
				break
			
			f = open(filename, "r")
			break
			
		except:
			print("Error: invalid filename. Try again:\n(Type \"exit\" to leave the program)")
	if exit == 1:
		exit()
		
	for line in f:
		if( line[0] != '#' ):	#check for comments
			i,j = line.split()
			i = int(i) + (gridSize / 2)
			j = int(j) + (gridSize / 2)
			grid[int(i)][int(j)] = 1	#Make sure int as can be float depending on gridsize
		
	f.close()
		
#Updates all cells at once#
def updateAll():
	
	newGrid = np.zeros((grid.shape[0], grid.shape[1]))

	for i in range (0, grid.shape[0]):
		for j in range (0, grid.shape[1]):
			newGrid[i][j] = updateCell(i, j)
		
	for i in range (0, grid.shape[0]):
		for j in range (0, grid.shape[1]):
			grid[i][j] = newGrid[i][j]

#global#
gridSize = 50	#50 should be enough for most simple seeds
grid = np.zeros((gridSize, gridSize))	#All cells initialised as dead (0) (alive = 1)
readSeed()	#Initialisation seed

fig = plt.figure()
ax = plt.axes(xlim = (-1, grid.shape[0]), ylim = (-1, grid.shape[1]))
cells, = ax.plot([], [], 'cs', ms=5)

#initialise animation#
def init():
	cells.set_data([],[])
	return cells,

#Animation function#
def animate(i):

	x = []
	y = []
	
	for i in range (0, grid.shape[0]):
		for j in range (0, grid.shape[1]):
			if grid[i][j] == 1:
				x.append(i)
				y.append(j)
	cells.set_data(x,y)
	updateAll()
	return cells,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=25, blit=True)

plt.grid()
plt.show()