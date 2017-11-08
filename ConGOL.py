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
	
#create pulsar seed (requires 15x15 grid)#
def seedPulsar():
	
	grid[3][1] = 1
	grid[4][1] = 1
	grid[5][1] = 1
	grid[9][1] = 1
	grid[10][1] = 1
	grid[11][1] = 1
	grid[1][3] = 1
	grid[6][3] = 1
	grid[8][3] = 1
	grid[13][3] = 1
	grid[1][4] = 1
	grid[6][4] = 1
	grid[8][4] = 1
	grid[13][4] = 1
	grid[1][5] = 1
	grid[6][5] = 1
	grid[8][5] = 1
	grid[13][5] = 1
	grid[3][6] = 1
	grid[4][6] = 1
	grid[5][6] = 1
	grid[9][6] = 1
	grid[10][6] = 1
	grid[11][6] = 1
	grid[3][8] = 1
	grid[4][8] = 1
	grid[5][8] = 1
	grid[9][8] = 1
	grid[10][8] = 1
	grid[11][8] = 1
	grid[1][9] = 1
	grid[6][9] = 1
	grid[8][9] = 1
	grid[13][9] = 1
	grid[1][10] = 1
	grid[6][10] = 1
	grid[8][10] = 1
	grid[13][10] = 1
	grid[1][11] = 1
	grid[6][11] = 1
	grid[8][11] = 1
	grid[13][11] = 1
	grid[3][13] = 1
	grid[4][13] = 1
	grid[5][13] = 1
	grid[9][13] = 1
	grid[10][13] = 1
	grid[11][13] = 1
	
#create blinker seed (requires 5x5 grid)#
def seedBlinker():
	
	grid[2][1] = 1
	grid[2][2] = 1
	grid[2][3] = 1
	
#create Gosper glider gun seed (requires 50x50 grid) WIP#
def seedGG():
	
	grid[1][42] = 1
	grid[1][43] = 1
	grid[2][44] = 1
	grid[2][43] = 1
	grid[11][41] = 1
	grid[11][42] = 1
	grid[11][43] = 1
	grid[12][40] = 1
	grid[12][44] = 1
	grid[13][39] = 1
	grid[13][45] = 1
	grid[14][39] = 1
	grid[14][45] = 1
	grid[15][42] = 1
	grid[16][40] = 1
	grid[16][44] = 1
	grid[17][41] = 1
	grid[17][42] = 1
	grid[17][43] = 1
	grid[18][42] = 1
	grid[21][43] = 1
	grid[21][44] = 1
	grid[21][45] = 1
	grid[22][43] = 1
	grid[22][44] = 1
	grid[22][45] = 1
	grid[23][42] = 1
	grid[23][46] = 1
	grid[25][41] = 1
	grid[25][42] = 1
	grid[25][46] = 1
	grid[25][47] = 1
	grid[35][44] = 1
	grid[35][45] = 1
	grid[36][44] = 1
	grid[36][45] = 1
	
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
grid = np.zeros((50,50))	#All cells initialised as dead (0) (alive = 1)
seedGG()

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

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=1000, interval=25, blit=True)

plt.grid()
plt.show()