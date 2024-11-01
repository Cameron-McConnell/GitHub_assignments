import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

class Ufo(pygame.sprite.Sprite):
    def__init__(self):
        super().__init__()
        
        #Set up the image
        self.image = pygame.image.load("ufo_game_enemy.png")
        self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        #Create the corresponding rect
        self.rect = self.image.get_rect()
        self.rect.centerx = 320
        self.rect.centery = 240
        
        #Create the ability to move
        self.dx = 5
        self.dy = 3
 
    #Moving the sprite
    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
    
        #Check boundaries
        if self.rect.right > screen.get_width():
            self.rect.left = 0
        if self.rect.bottom > screen.get_height():
            self.rect.top = 0
            
def main():
    #Set up screen
    pygame.display.set_caption("Sprite")
    background = pyagme.Surface(screen.get_size())
    background.fill("blue")
    screen.blit(background, (0, 0))
        
    #Instantiate ufo
    ufo = Ufo()
    allSprites = pygame.sprite.Group(ufo)
        
    #Set up timing
    clock = pygame.time.Clock()
    keepGoing = True
    while(keepGoing):
        clock.tick(30)
            
        #Check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                    
        #Clear and redraw sprites
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
            
        pygame.display.flip()
        
if__name__ == "__main__":
    main()
    pygame.quit()
        
        
        
        