# -*- coding: utf-8 -*-
import pygame
import random
import sys
import os
from pm_c import *
from pm_r import *
from pygame.locals import *
#from ejemplopres import *

alto=650
ancho=900
blanco=(255,255,255)
gris = (100, 100, 100)
negro=(0,0,0)



def load_image(name, colorkey=False):
    fullname = os.path.join("boom", name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print ('No se puede cargar la imagen: ', message)
        #raise SystemExit, message

    image = image.convert()

    if colorkey:
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)

    return (image, image.get_rect())

class jugador(pygame.sprite.Sprite):

    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load(imagen).convert_alpha()
        self.rect = self.image.get_rect()
        self.vida=100

    def chocar(self):
        self.vida-=10

    def vida_(self):
        return self.vida

class enemigo(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load(imagen).convert_alpha()
        self.rect = self.image.get_rect()
        self.direccion=0
        self.disparar=random.randrange(100)
        self.vida_e=30
        self.x=random.randrange(350,ancho-100)
        self.y=random.randrange(alto-100)
        self.puntos=circu((self.x,self.y),80)
        self.ind=0
        self.z=100
        self.p=self.puntos[0]
        self.size=len(self.puntos)


    def chocar_e(self):
        self.vida_e-=10

    def vel_disparar(self,n):
        self.z=n

    def update(self):

        if self.ind < self.size:
            self.p=self.puntos[self.ind]
            self.rect.x=self.p[0]
            self.rect.y=self.p[1]
            self.ind+=1
        else:
            self.ind=0

        self.disparar-=1
        if self.disparar<0:
            self.disparar=random.randrange(self.z)


class Bala(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load(imagen).convert_alpha()
        self.rect = self.image.get_rect()
        self.jugador=0
        self.i=0
        self.size=0
        self.p_objetivo=[]

    def apuntar(self,posicion,objetivo):
        self.rect.x=posicion[0]
        self.rect.y=posicion[1]
        self.size=len(objetivo)
        self.p_objetivo=objetivo


    def update(self):
        if self.jugador==0:
            self.rect.x+=5
        else:
            p=self.p_objetivo[self.i]
            self.rect.x=p[0]
            self.rect.y=p[1]
            if self.i < self.size-1:
                self.i+=1



class Boom(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self._load_images()
        self.step = 0
        self.delay = 2
        (self.image, self.rect) = load_image('1.png', True)
        self.rect.center = (x, y)

    def _load_images(self):
        """Carga la lista 'self.frames' con todos los cuadros de animacion"""

        self.frames = []

        for n in range(1, 8):
            path = '%d.png'
            new_image = load_image(path % n, True)[0]
            self.frames.append(new_image)

    def update(self):
        self.image = self.frames[self.step]

        if self.delay < 0:
            self.delay = 2
            self.step += 1

            if self.step > 6:
                self.kill()
        else:
            self.delay -= 1


def Crear_enemigos(num, l_e, l_t):
    for i in range(num):
       nave2=enemigo('nave2.png')
       nave2.rect.x=random.randrange(200, ancho-60)
       nave2.rect.y=random.randrange(alto-130)
       l_e.add(nave2)
       l_t.add(nave2)
    return l_e, l_t

def score(fuente, screen, puntos, nivel,vida,b,time):

    if b!=1:
        puntos_imagen = fuente.render('Puntos ' + str(puntos), 1, blanco)
        nivel_imagen = fuente.render('Nivel ' + str(nivel), 1, blanco)
        vida_imagen = fuente.render('Vida ' + str(vida), 1, blanco)
        tiempo_imagen = fuente.render('Tiempo ' + str(time), 1, blanco)
        screen.blit(vida_imagen, (5, 5))
        screen.blit(puntos_imagen, (100, 5))
        screen.blit(nivel_imagen, (230, 5))
        screen.blit(tiempo_imagen, (320, 5))

def pausa():
    pausado=True
    while pausado:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pausado==False
    pygame.display.update()
    #reloj.tick(5)


def Jugar():
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])


    fondo=pygame.image.load('fondos/fondo.jpg')
    pantalla.blit(fondo,(0,0))#posiciona la imagen y la actualiza

    pygame.mouse.set_visible(False)#no muestra el puntero en pantalla

    pos=pygame.mouse.get_pos()
    xnave=0
    ynave=500

    puntos=0
    balax=0
    balay=0

    b=0
    terminar=False
    disparo=False
    num_enemigos=6
    cont=8
    puntos=0
    nivel=1


    time_ini=110
    cont_=0
    seg=0


    #Fuentes y puntaje
    fuente = pygame.font.Font(None, 30)

    s_bala=pygame.mixer.Sound('sonidos/laser.wav')
    e_explosion=pygame.mixer.Sound('sonidos/explode1.wav')
    music=pygame.mixer.Sound('sonidos/Drive.ogg')
    j_explosion=pygame.mixer.Sound('sonidos/explode.ogg')
    over=pygame.mixer.Sound('sonidos/over.wav')

    ls_todos=pygame.sprite.Group()
    ls_enemigo=pygame.sprite.Group()
    ls_balas=pygame.sprite.Group()
    ls_balase=pygame.sprite.Group()
    ls_jugadores=pygame.sprite.Group()

    nave=jugador('personajes/nave1.png')#carga la imagen
    nave.rect.x=pos[0]
    nave.rect.y=pos[1]

    ls_jugadores.add(nave)
    ls_todos.add(nave)

    #ls_enemigo,ls_todos= Crear_enemigos(num_enemigos, ls_enemigo, ls_todos)

    for i in range(6):
    	nave2=enemigo('personajes/nave2.png')
    	#nave2.rect.x=random.randint(100,ancho-20)
    	#nave2.rect.y=random.randint(0,alto-20)
    	ls_enemigo.add(nave2)
    	ls_todos.add(nave2)

    pygame.display.flip()

    music.play(3)


    reloj=pygame.time.Clock()
    while not terminar:
        pos=pygame.mouse.get_pos()
        xnave=pos[0]
        ynave=pos[1]

        for event in pygame.event.get():
            if event.type==pygame.QUIT :
                terminar=True
            elif event.type==pygame.MOUSEBUTTONDOWN:
                #print 'pulsado'
                bala=Bala('balas/bala.png')
                bala.rect.x=pos[0]
                bala.rect.y=pos[1]+20
                ls_balas.add(bala)
                ls_todos.add(bala)
                s_bala.play()

        pantalla.blit(fondo,(0,0))
        nave.rect.x=pos[0]
        nave.rect.y=pos[1]
        #ls_enemigo.draw(pantalla)

        for b in ls_balas:
            ls_impactos=pygame.sprite.spritecollide(b,ls_enemigo,True)
            for impacto in ls_impactos:
                ls_balas.remove(b)
                ls_todos.remove(b)
                e_explosion.play()
                (x, y)= b.rect.center
                ls_todos.add(Boom(x, y))
                puntos+=10
                num_enemigos-=1

    #cuando se encuentras las balas desaparecen
        for b in ls_balas:
            ls_impac_b=pygame.sprite.spritecollide(b,ls_balase,True)
            for impacto in ls_impac_b:
            	(x, y)= b.rect.center
            	ls_todos.add(Boom(x, y))
            	ls_balas.remove(b)
            	ls_todos.remove(b)



        ls_choque=pygame.sprite.spritecollide(nave,ls_enemigo,False)

        for elemento in ls_choque:
            #print 'choque'
            nave.chocar()
            #print nave.vida

        for be in ls_balase:
            impactos=pygame.sprite.spritecollide(be,ls_jugadores,False)
            for imp in impactos:
                nave.chocar()
                #print nave.vida
                j_explosion.play()
                ls_balase.remove(be)
                ls_todos.remove(be)

        #tiempo del juego
        total_segundos = time_ini - (cont_ // 60)
        if total_segundos <= 0:
              total_segundos = 0

        minutos = total_segundos // 60
        segundos = total_segundos % 60
        seg=segundos
        time= "{0:02}:{1:02}".format(minutos, segundos)


        for e in ls_enemigo:
            if e.disparar==0:
                bala2=Bala('balas/bala3.png')
                (x,y)=(e.rect.x, e.rect.y)
                j=pos
                objetivo=punto_medio((x,y),pos)
                bala2.apuntar((x,y),objetivo)
               # bala2.nave=(pos)
                bala2.jugador=1
                #bala2.rect.x=e.rect.x
                #bala2.rect.y=e.rect.y
                ls_todos.add(bala2)
                ls_balase.add(bala2)


        if num_enemigos<2:
            if cont>0:
                for i in range(5):
                    nave2=enemigo('personajes/nave2.png')
                    #nave2.rect.x=random.randrange(300,ancho-20)
                    #nave2.rect.y=random.randrange(alto-20)
                    ls_enemigo.add(nave2)
                    ls_todos.add(nave2)
                    num_enemigos=6
                cont-=1

        if (nave.vida_()==0 or total_segundos==0):
            music.stop()
            over.play()
            ls_todos.empty()
            ls_enemigo.empty()
            pantalla.fill(negro)
            fondo=pygame.image.load('fondos/over.png')
            pantalla.blit(fondo,(100,90))#posiciona la imagen y la actualiza
            pygame.display.flip()
            b=1
            pygame.time.delay(3600)
            over.stop()
            terminar=True

        if puntos>=100:
            nivel=2
            nave2.vel_disparar(50)
            #num_enemigos=num_enemigos+3

        if num_enemigos==0:
            music.stop()
            ls_todos.empty()
            pantalla.fill(blanco)
            fondo=pygame.image.load('fondos/win.png')
            pantalla.blit(fondo,(0,100))#posiciona la imagen y la actualiza
            pygame.display.flip()
            pygame.time.delay(1600)
            terminar=True


        score(fuente, pantalla, puntos, nivel,nave.vida_(),b,time)
        ls_todos.update()
        ls_todos.draw(pantalla)

        cont_+=1
        pygame.display.flip()
        reloj.tick(60)
