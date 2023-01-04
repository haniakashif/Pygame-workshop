import pygame
pygame.init()

class Block:
    X_position = 0
    Y_position = 0
    X_speed = 0
    Y_speed = 0
    Texture = pygame.image.load("koya.png")
    #image

    def __init__(self, thisXPos, thisYPos, thisXSpeed, thisYSpeed):
        self.X_position = thisXPos
        self.Y_position = thisYPos
        self.X_speed = thisXSpeed
        self.Y_speed = thisYSpeed

    def updateBlock (self):
        self.X_position += self.X_speed
        self.Y_position += self.Y_speed

Block1 = Block(0,500,0,-2)
Block2 = Block(450,0,0,2)
Block1.Texture = pygame.transform.scale(Block1.Texture, (50, 50))
Block2.Texture = pygame.transform.scale(Block2.Texture, (50, 50))

screen = pygame.display.set_mode((500,500))
background = pygame.image.load("blue.png")
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    screen.blit(background,(0,0))
    screen.blit(Block1.Texture, (Block1.X_position, Block1.Y_position))
    screen.blit(Block2.Texture, (Block2.X_position, Block2.Y_position))
    Block1.updateBlock()
    Block2.updateBlock()
    pygame.display.update()
