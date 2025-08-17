import pygame
from constants import*
from player import*
from asteroidfield import*
from asteroid import*
updatable = pygame.sprite.Group()
drawables = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

AsteroidField.containers = (updatable)
Asteroid.containers = (asteroids, updatable, drawables)
Player.containers = (updatable , drawables)
AsteroidField()
def main():
	pygame.init()
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	clock = pygame.time.Clock()
	dt = 0
	player = Player(SCREEN_WIDTH/2 ,SCREEN_HEIGHT/2)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	number = 1
	
	while number > 0:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		updatable.update(dt)
		pygame.Surface.fill(screen,(0,0,0))
		for drawable in drawables:
			drawable.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60)/1000
if __name__ == "__main__":
	main()
