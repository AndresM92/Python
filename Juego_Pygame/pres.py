# -*- coding: utf-8 -*-
from juegoa import Jugar
import pygame
import random
import sys
import os
from pygame.locals import *


NEGRO  = (   0,   0,   0)
BLANCO = ( 255, 255, 255)
VERDE  = (   0, 255,   0)
ROJO   = ( 255,   0,   0)
ancho = 900
alto = 650



def Menu_principal(n):

  if n==0:
    fondo=pygame.image.load("fondos/prin.jpg")
    fondo=pygame.transform.scale(fondo,[ancho,alto])
    pantalla.blit(fondo,[0,0])
    texto=fuente.render("Menu Principal", True, BLANCO)
    pantalla.blit(texto, [10, 150])
    texto=fuente.render("1. Historia", True, BLANCO)
    pantalla.blit(texto, [150, 300])
    texto=fuente.render("2. Jugar", True, BLANCO)
    pantalla.blit(texto, [150, 350])
    texto=fuente.render("3. Salir", True, BLANCO)
    pantalla.blit(texto, [150, 400])

  if n==1:
    fondo=pygame.image.load("fondos/planeta.jpg")
    fondo=pygame.transform.scale(fondo,[ancho,alto])
    pantalla.blit(fondo,[0,0])
    texto=fuente.render(" La ultima invasion que ha recibido el planeta Kp23.", True, BLANCO)
    pantalla.blit(texto, [10, 150])
    texto=fuente.render(" Fueron los skrulls son una raza alienigena muy importante", True, BLANCO)
    pantalla.blit(texto, [10, 190])
    texto=fuente.render(" cuyo mundo trono fue destruido hace anios por Galactus.", True, BLANCO)
    pantalla.blit(texto, [10, 230])
    texto=fuente.render(" Desde hace tiempo los skrulls tienen en el planeta Kp23 un objetivo muy", True, BLANCO)
    pantalla.blit(texto, [10, 270])
    texto=fuente.render(" importante de invasion y de vez en cuando se infiltran en el planeta", True, BLANCO)
    pantalla.blit(texto, [10, 310])
    texto=fuente.render(" aprovechando que son una raza de metamorfos.", True, BLANCO)
    pantalla.blit(texto, [10, 350])
    texto=fuente.render(" Y asi es como llevaron acabo su Invasion Secreta ", True, BLANCO)
    pantalla.blit(texto, [10, 390])
    texto=fuente.render(" En dicha invasion se descubrio como los skrulls llevaban", True, BLANCO)
    pantalla.blit(texto, [10, 430])
    texto=fuente.render(" anios infiltrados en las altas esferas de la sociedad ", True, BLANCO)
    pantalla.blit(texto, [10, 470])
    texto=fuente.render(" esto para allanar el camino para que llegasen las naves  ", True, BLANCO)
    pantalla.blit(texto, [10, 510])
    texto=fuente.render(" nodrizas y comenzar la invasion al planeta Kp23.", True, BLANCO)
    pantalla.blit(texto, [10, 550])

  if n==2:
    Jugar()


pygame.init()
#dim=[ANCHO, ALTO]
#pantalla=pygame.display.set_mode(dim)
pantalla=pygame.display.set_mode([ancho,alto])
pygame.display.set_caption("Galaxy Kp23")
fuente = pygame.font.Font(None, 36)
terminar=False
ver_pag = True
pag = 0
fin_juego=False
op=1
reloj=pygame.time.Clock()
Menu_principal(0)
  
while not terminar and ver_pag:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        terminar=True
    if event.type == pygame.KEYDOWN:
        if event.key==48:#opcion1
          Menu_principal(0)
        if event.key==49:#opcion2
          Menu_principal(1)
        if event.key==50:#opcion3
          Menu_principal(2)
        if event.key==51:#opcion3
          terminar=True

  #pantalla.fill(NEGRO)
  pygame.display.flip()
