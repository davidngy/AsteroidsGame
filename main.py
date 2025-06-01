from player import *
from player import Player
from constants import *
from turtledemo.penrose import draw
import pygame
from operator import contains

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2 ,SCREEN_HEIGHT / 2)
    dt = 0  
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        
        updateable.update(dt)
       
        for drawable_element in drawable:
            drawable_element.draw(screen)
            
        pygame.display.flip()
        #drawable.draw(screen)
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
    