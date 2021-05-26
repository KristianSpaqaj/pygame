import pygame
import time
from pygame.locals import *

pygame.init()

width = 800
height = 800
red = (255, 0, 0)
blue = (0, 0, 255)
x = width/2
y = height/2
x_change = 0
y_change = 0
speed = 30
running = True

surface = pygame.display.set_mode((width,height))
pygame.display.set_caption('Moving about')


font_style = pygame.font.SysFont(None, 50)

def message(msg,color):
    text = font_style.render(msg,True,color)
    surface.blit(text,[width/2,height/2])

clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.key == pygame.K_LEFT:
                    x_change = -10
                    y_change = 0
            elif event.key == pygame.K_RIGHT:
                    x_change = 10
                    y_change = 0
            elif event.key == pygame.K_UP:
                    y_change = -10
                    x_change = 0
            elif event.key == pygame.K_DOWN:
                    y_change = 10
                    x_change = 0
            elif event.key == pygame.K_SPACE:
                    x_change = 0
                    y_change = 0
        if event.type == pygame.QUIT:
            running = False
    if x >= width or x < 0 or y >= height or y < 0:
        y_change = 0
        x_change = 0
        running = False
        
    x += x_change
    y += y_change    
    surface.fill((255, 255, 255))
    pygame.draw.rect(surface, blue,[x, y, 10, 10])
    pygame.display.update()
    clock.tick(speed)

message("You Lost",red)
time.sleep(2)
pygame.quit()
quit()