'''
Tutorial demonstrates how to create a game window with Python Pygame.

Any pygame program that you create will have this basic code
'''

import pygame
import sys

# Initialize Pygame and give access to all the methods in the package
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Tutorial")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

maze_surface = pygame.Surface((800,600))
maze_surface.fill("black")

class Square(pygame.sprite.Sprite):
    def __init__(self,x,y,size_x,size_y,color):
        super(Square, self).__init__()
        self.image = pygame.Surface((size_x,size_y), pygame.SRCALPHA, 32)
        self.image.convert_alpha()
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (x,y))
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        delta_x = 400
        delta_y = 30
    def move(self, deltax, deltay):
        if self.rect.left < 0 or self.rect.right>800:
            deltax *= -3
        if self.rect.top < 0 or self.rect.bottom > 600:
            deltay *= -3

        self.rect.centerx += deltax
        self.rect.centery += deltay


walls = pygame.sprite.Group()
walls.add(Square(300,200,10,20,WHITE))
player = pygame.sprite.Group
player.add(Player())


    

# Create clock to later control frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (e.g., white)
    screen.fill("white")
    screen.blit(maze_surface,(0,0))
    walls.draw(maze_surface)
    player.draw(maze_surface)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        Player.move(-2,0)
    if keys[pygame.K_RIGHT]:
        Player.move(2,0)
    if keys[pygame.K_UP]:
        Player.move(0,-2)
    if keys[pygame.K_DOWN]:
        Player.move(0,2)


    # Update the display
    pygame.display.flip()

    # Set a frame rate to 60 frames per second
    clock.tick(60)

# Quit Pygame properly
pygame.quit()
sys.exit()
