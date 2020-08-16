import sys,pygame #
import numpy as np #
import matplotlib.pyplot as plt #o
import keyboard
import time
import asyncio
import random

pygame.init()
pygame.display.set_caption('Mi Juego de la vida')
size = width, height = 600,600

bg = 25,25,25


nX_Cells = 60
nY_Cells = 60

dinCW = (width-1) / nX_Cells
dinCH = (height-1) /nY_Cells

screen = pygame.display.set_mode(size)
screen.fill(bg)





async def main():
	gameState =np.zeros((nX_Cells,nY_Cells))

	pauseExec = True
	while True:		
		screen.fill(bg)
		new_gameState = np.copy(gameState)		
		ev = pygame.event.get()
		for event in ev:
			if event.type == pygame.KEYDOWN:
				pauseExec = not pauseExec

			mouseClick = pygame.mouse.get_pressed()
			if sum(mouseClick) > 0:
				posX, posY = pygame.mouse.get_pos()
				celX = int(np.floor(posX /dinCW))
				celY = int(np.floor(posY/ dinCH))				 
				
				new_gameState[celX,celY] = not mouseClick[2]



		for y in range(0,nY_Cells):
			for x in range(0,nX_Cells):
				if  not pauseExec:					
					n_neigh= gameState[(x-1) % nX_Cells,  (y-1) % nY_Cells] + \
						gameState[(x) % nX_Cells, 	 (y-1) % nY_Cells] + \
						gameState[(x+1) % nX_Cells,	 (y-1) % nY_Cells]+\
						gameState[(x-1) % nX_Cells,	 (y) % nY_Cells]   +\
						gameState[(x+1) % nX_Cells,	 (y) % nY_Cells]   +\
						gameState[(x-1) % nX_Cells,	 (y+1) % nY_Cells] +\
						gameState[(x) % nX_Cells, 	 (y+1) % nY_Cells] +\
						gameState[(x+1) % nX_Cells,  (y+1) % nY_Cells]

					
					#cecula muerta con 3 celulas vecinas vivas nace
					if gameState[x,y] == 0 and n_neigh == 3:
						new_gameState[x,y] = 1			

					elif gameState[x,y] == 1 and (n_neigh < 2  or n_neigh >3):
						new_gameState[x,y] = 0

					#una celula viva con 2 o 3 celulas vecinas vivas isga viviendo , en otro caso muere.
				
				poly = [((x)*dinCW , (y)*dinCH),
						((x+1)*dinCW  , (y)*dinCH ),
						((x+1)*dinCW  , (y+1)*dinCH ),
						((x)*dinCW  ,(y+1)*dinCH )]				
				
				pygame.draw.polygon(screen, (128,128,128), poly,int(abs(1-new_gameState[x,y])))

		gameState = new_gameState
		time.sleep(0.1)
		pygame.display.flip()

asyncio.run(main())