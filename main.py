from player import *
from constants import *
from turtledemo.penrose import draw
import pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0   
    player = Player(SCREEN_WIDTH / 2 ,SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
     
        pygame.display.flip()
        player.draw(screen)
        
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
    