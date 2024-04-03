import pygame
import time
import random

WIDTH, HEIGHTH, = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHTH))
pygame.display.set_caption("RunningBack 100yrd Run")

def main():
        run = True

        while run :
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                run = False
                                break
                        
        pygame.quit()

if __name__ == "__main__":
        main()