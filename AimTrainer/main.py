#pip install pygame
import pygame
import random
import math
import time

pygame.init()

WIDTH, HEIGHT = 800,600

WIN = pygame.display.set_mode((WIDTH,HEIGHT))#inicializes window
pygame.display.set_caption("Aim Trainer")#window name

def main():
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break 
    pygame.quit()   
     
if __name__ == "__main__":
    main()   





