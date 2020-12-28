import pygame
import settings
from pygame import K_UP, K_DOWN, K_SPACE
from settings import width, height
keys  = [False, False, False]
class event:
    def manage(self,gun,bullet):
        for event in pygame.event.get(): 
            if event.type==pygame.QUIT:
                pygame.quit() 
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key==K_UP:
                    keys[0]=True
                    print("UP pressed")
                elif event.key==K_DOWN:
                    keys[1]=True
                    print("DOWN pressed")
                elif event.key==K_SPACE:
                    keys[2]=True
                    print("SPACE pressed")
            if event.type == pygame.KEYUP:
                if event.key==K_UP:
                    keys[0]=False
                    print("UP released")
                elif event.key==K_DOWN:
                    keys[1]=False
                    print("DOWN released")
                elif event.key==K_SPACE:
                    keys[2]=False
                    print("SPACE released")
                    
        if keys[0]:
            gun.moveUp(gun.position)
        elif keys[1]:
            gun.moveDown(gun.position)
        if keys[2] and not bullet.fired:
            bullet.getFired(gun)
        if bullet.fired and bullet.position[0] > -10:
            bullet.fly()
        elif bullet.position[0] <= -10 and bullet.position[0] != -100:
            bullet.reload()
