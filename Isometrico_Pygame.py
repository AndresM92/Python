import pygame
import math
from pygame.locals import *
red=(255,0,0)
azul=(0,0,255)
salir=False
blanco=(255,255,255)
verde=(0,255,0)

ancho=800
alto=800
ox=ancho/2
oy=alto/2
pygame.init()
pantalla=pygame.display.set_mode([ancho,alto])
x=0
y=0
s="1"
origen=(ox,oy)


def Traspu(ox,oy,dx,dy):
    nx=ox+dx
    ny=oy-dy
    return (nx,ny)

def cooraux(punto):
 x1= int (punto[0]-ox)
 y1= int (oy-punto[1])
 return (x1,y1)

def rotacion(v,p,grados):
 r=cooraux(v)
 x1=r[0]
 y1=r[1]
 nx = int((x1+math.cos(math.radians(grados))*(p[0]-x1))-(math.sin(math.radians(grados))*(p[1]-y1)))
 ny = int((y1+math.sin(math.radians(grados))*(p[0]-x1))+(math.cos(math.radians(grados))*(p[1]-y1)))
 return Traspu(ox,oy,nx,ny)

pygame.init()
pantalla=pygame.display.set_mode([ancho,alto])
pantalla.fill(blanco)

pr=rotacion((ox,oy), (20,0), 90)
pygame.draw.line(pantalla, azul, (ox,oy), pr, 2)

#linea derecha
pr1=rotacion((ox,oy), (100,0), 30)
pygame.draw.line(pantalla, azul, (ox,oy), pr1, 2)

#linea izquierda
pr2=rotacion((ox,oy), (80,0), 120)
pygame.draw.line(pantalla, azul, (ox,oy), pr2, 2)


#linea derecha
pt=cooraux(pr1)
pr4=rotacion(pr1, (pt[0]+20,pt[1]), 90)
pygame.draw.line(pantalla, azul, pr4, pr1, 2)

pygame.draw.line(pantalla, azul, pr4, pr, 2)


#linea izquierda
pt1=cooraux(pr2)
pr3=rotacion(pr2, (pt1[0]+20,pt1[1]), 90)
pygame.draw.line(pantalla, azul, pr3, pr2, 2)

pygame.draw.line(pantalla, azul, pr3, pr, 2)


#diagonal derecha
pt2=cooraux(pr3)
pr5=rotacion(pr2, (pt2[0]+80,pt2[1]),30)
pygame.draw.line(pantalla, azul, pr3, pr5, 2)

pt3=cooraux(pr5)
pr8=rotacion(pr5, (pt3[0]+30,pt3[1]),300)
pygame.draw.line(pantalla, azul, pr8, pr5, 2)

pt4=cooraux(pr5)
pr7=rotacion(pr5, (pt4[0]+20,pt4[1]),90)
pygame.draw.line(pantalla, azul, pr7, pr5, 2)

pygame.draw.line(pantalla, azul, pr7, pr8, 2)

pt5=cooraux(pr7)
pr9=rotacion(pr7, (pt5[0]+30,pt5[1]),30)
pygame.draw.line(pantalla, azul, pr9, pr7, 2)


pt6=cooraux(pr8)
pr6=rotacion(pr8, (pt6[0]+30,pt6[1]),30)
pygame.draw.line(pantalla, azul, pr8, pr6, 2)


pygame.draw.line(pantalla, azul, pr9, pr6, 2)
pygame.draw.line(pantalla, azul, pr4, pr6, 2)


pygame.display.flip()

while salir != True:
    tecla=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True
        if tecla[pygame.K_ESCAPE]:
            salir = True
    pygame.display.update()
pygame.quit()
