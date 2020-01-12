import pygame

class Card(object):
    def __init__(self, cardType, override=False):
        self.type = cardType
        self.override = override
        path = "resources/" + cardType + ".png"
        self.image = pygame.image.load(path).convert_alpha()
    
    def draw(self, screen, cx, cy, scale, angle):
        if self.override:
            self.drawImage = pygame.image.load("resources/back.png").convert_alpha()
        else:
            self.drawImage = self.image
        cardWidth, cardHeight = self.drawImage.get_size()
        scaledWidth = int(cardWidth*scale)
        scaledHeight = int(cardHeight*scale)
        self.image_scale = pygame.transform.scale(self.drawImage, (scaledWidth, scaledHeight))
        self.image_rotate = pygame.transform.rotate(self.image_scale, angle)
        self.image_rect = self.image_rotate.get_rect(center=(cx, cy))
        screen.blit(self.image_rotate, self.image_rect)