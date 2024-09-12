import pygame
from constants import *
from player import Player

def main():
    #INITIALIZE EVERYTHING
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
   
    #GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)

    #CREATE PLAYER
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #WELCOME MESSAGE
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #INFINITE LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        screen.fill("black")


        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        

        #FRAMERATE
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
