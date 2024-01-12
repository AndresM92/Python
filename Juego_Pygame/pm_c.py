import pygame
import sys
import math
import timeit


pygame.init()

def translacion(origen,punto):
    x2=origen[0]+punto[0]
    y2=origen[1]-punto[1]
    return (x2,y2)

def circu(centro,r):
    l=[]
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    l5=[]
    l6=[]
    l7=[]
    l8=[]
    x=0
    y=r
    d=5/4-r
    punto=translacion(centro,(x,y))
    l1.append(punto)
    punto=translacion(centro,(x,-y))
    l2.append(punto)
    punto=translacion(centro,(-x,y))
    l3.append(punto)
    punto=translacion(centro,(-x,-y))
    l4.append(punto)
    punto=translacion(centro,(y,x))
    l5.append(punto)
    punto=translacion(centro,(y,-x))
    l6.append(punto)
    punto=translacion(centro,(-y,x))
    l7.append(punto)
    punto=translacion(centro,(-y,-x))
    l8.append(punto)
    

    while y>x:
        if d<0:
            d=d+x*2+3
            x=x+1
        else:
            d=d+2*(x-y)+5
            x=x+1
            y=y-1

        punto=translacion(centro,(x,y))
        l1.append(punto)
        punto=translacion(centro,(x,-y))
        l2.append(punto)
        punto=translacion(centro,(-x,y))
        l3.append(punto)
        punto=translacion(centro,(-x,-y))
        l4.append(punto)
        punto=translacion(centro,(y,x))
        l5.append(punto)
        punto=translacion(centro,(y,-x))
        l6.append(punto)
        punto=translacion(centro,(-y,x))
        l7.append(punto)
        punto=translacion(centro,(-y,-x))
        l8.append(punto)
    l5.reverse()
    l2.reverse()
    l8.reverse()
    l3.reverse()

    l=l1+l5+l6+l2+l4+l8+l7+l3
    return l
