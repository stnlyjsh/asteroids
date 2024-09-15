import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    #INITIALIZE EVERYTHING
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
   
    #GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    #CREATE
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    

    #WELCOME MESSAGE
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #INFINITE LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #UPDATE EVERYTHING
        for obj in updatable:
            obj.update(dt)
        
        for asteroid in asteroids:
            if player.collision(asteroid): #CHECK FOR PLAYER COLLISION
                print("Game over!")
                sys.exit()

            for shot in shots: #CHECK FOR SHOT COLLISION
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")


        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        

        #FRAMERATE
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
