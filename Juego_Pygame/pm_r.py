import pygame
import sys
import math


pygame.init()


def punto_medio(p1,p2):

	l=[]
	dx=abs(p2[0]-p1[0])
	dy=abs(p2[1]-p1[1])
	x=p1[0]
	y=p1[1]
	hor=dy<dx
	if hor:		
		d=(2*dy)-dx
		dE=2*dy
		dNE=2*(dy-dx)
	else:
		d=(2*dx)-dy
		dE=2*dx
		dNE=2*(dx-dy)
	if (p2[0]-p1[0])>0:
		dirx=1
	else:
		dirx=-1
	if (p2[1]-p1[1])>0:
		diry=1
	else:
		diry=-1
	l.append((x,y))

	if hor:
		while x!=p2[0]:
			if d<=0:
				d=d+dE
			else:
				d=d+dNE
				y+=diry
			x+=dirx
			l.append((x,y))
	else:
		while y!=p2[1]:
			if d<=0:
				d=d+dE
			else:
				d=d+dNE
				x+=dirx
			y+=diry
			l.append((x,y))
	return l


