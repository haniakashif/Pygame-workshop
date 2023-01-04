import pygame
pygame.init()

class Block:
    x_position = 0
    y_position = 0
    x_speed = 0
    y_speed = 0
    texture = pygame.image.load("koya.png")

    def __init__(self, thisxpos, thisypos, thisxspeed, thisyspeed):
        self.x_position = thisxpos
        self.y_position = thisypos
        self.x_speed = thisxspeed
        self.y_speed = thisyspeed
        
    def updateBlock(self):
        self.x_position += self.x_speed
        self.y_position += self.y_speed

Block1 = Block(0,0,2,2)
Block2 = Block(100, 0, -2, 2)
Block1.texture = pygame.transform.scale(Block1.texture, (20,20))
Block2.texture = pygame.transform.scale(Block2.texture, (20,20))

screen = pygame.display.set_mode((500, 500))
background = pygame.image.load("blue.png")
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    screen.blit(background, (0,0))
    screen.blit(Block1.texture, (Block1. x_position, Block1.y_position))
    screen.blit(Block2.texture,(Block2. x_position, Block2.y_position))
    Block1.updateBlock()
    Block2.updateBlock()
    pygame.display.update()
