from pygame import *

import math
import pygame
import time
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Location(object):
     def __init__(self, x=0,y=0,locmin=0, g=0):
        self.X=x
        self.Y=y
        self.G=g
        self.locmin=locmin
     def mincol(self):
        return self.locmin                
     def setloc(self,loc):
        self.locmin=loc
     def getxy(self):
         return self.X, self.Y
     def gets(self):
         return self.G
#4,2
maps=[[1,0,0,99,0,0,0],  #
      [0,0,0,99,0,0,0],
      [0,0,0,99,99,0,0],
      [0,0,0,99,0,0,0],
      [0,0,0,99,99,99,0],
      [0,0,0,0,0,0,0], # [0,0,0,0,0,5,0],
      [0,0,0,99,0,0,0]]

class Astar(object):
     def __init__(self, X=0,Y=0,x2=0, y2=0,G=0):
         self.xCoord=X
         self.yCoord=Y

         self.endx=x2
         self.endy=y2
         ##self.h_old=G
     def  getXstart(self):
         return self.xCoord
     def  getYstart(self):
         return self.yCoord
     
     def  getXend(self):
         return self.endx
     def  getYend(self):
         return self.endy
     #def  G(self):
         #return self.G
     def  getXYG(self):
         return self.xCoord, self.yCoord, self.G
     def setX(self, A):
         self.xCoord=A
     def setY(self, B):
         self.yCoord=B
     #def setZ(self, G2):
         #self.G=G2     
     def distanceTO(self,x,y):         
         return  math.sqrt(((x-self.endx)**2) +((y-self.endy)**2))
            
                    

         
k=Astar(0,0,2,5)
G=0
s=0
for i in range(200):
    #print(i)
    X=[]
    Y=[]
    G_H=[]
    
    for j in range(-2,2):
        for j1 in range(-2,2):
            ##print(k.getYstart()+j)
           # print(s)
            if(k.getXstart()+j1>=0 and k.getYstart()+j>=0):
                
                
                #print( k.getYstart()+j, k.getXstart()+j1)
                try:
                    if maps[k.getXstart()+j1][k.getYstart()+j]==0:
                        G=1
                        h=k.distanceTO(k.getXstart()+j1,k.getYstart()+j)
                        #print( k.getYstart()+j, k.getXstart()+j1,h)

                        s+=1
                        X.append(k.getXstart()+j1)
                        Y.append(k.getYstart()+j)
                        G_H.append(h+G)
                        
                except:
                    pass
    ks=0
    for k1 in range(1, len(G_H)):
        ks=G_H[0]
        #print(ks)
        if(ks>G_H[k1]):
            ks=G_H[k1]
    print(ks)
    for k1 in range(len(G_H)):
        if G_H[k1]==ks:
            k.setX(X[k1])
            k.setY(Y[k1])
            #
            maps[X[k1]][Y[k1]]=1
            print(k.getXend(),k.getYend(),  X[k1] , Y[k1])
        if k.getXend()==X[k1] and k.getYend()==Y[k1]:
            s=1
            break
            
    if s==1:
        print("end", i)
        break
       
print(maps)
                
pygame.init()

WIDTH = 30
HEIGHT = 30
 
# This sets the margin between each cell
MARGIN = 5 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
while done==False:
    clock.tick(40)
    for event in pygame.event.get(): # Пользователь что-то сделал
        if event.type == pygame.QUIT: # Если пользователь щёлкнул на кнопки закрытия
            done=True # Поставить значение done, чтобы выйти из цикла
    screen.fill(BLACK)
    for row in range(len(maps)):
        for column in range(len(maps[row])):
            color = WHITE
            if maps[row][column] == 1:
                color = GREEN
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
            if maps[row][column] == 99:
                color = BLACK
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
            if maps[row][column] == 0:
                color = WHITE
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
        
    clock.tick(40)
    pygame.display.flip()
pygame.quit()
'''  
for event in pygame.event.get():
    if event.type == pygame.QUIT:
# Go ahead and update the screen with what we've drawn.
pygame.display.flip()
pygame.quit()
#k=k.action(maps)       
#print(maps[0][3])        
'''
