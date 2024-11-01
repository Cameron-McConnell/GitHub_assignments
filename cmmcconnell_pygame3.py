#initialize
import pygame

def main():
    pygame.init()
    
    #Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display,set_caption("UFO")
    
    #Entities
    #blue background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill("blue")
    
    #Load an image
    ufo = pygame.image.load("ufo_game_enemy.png")
    ufo = ufo.convert_alpha()
    ufo = pygame.transform.scale(ufo, (100, 50))
    
    #Set up some ufo varibales
    ufo_x = 0
    ufo_y = 200
    
    #Action
    
        #Assign
    clock = pygame.time.Clock()
    keepGoing = True
    
        #Loop
    while keepGoing:
        
        #Time
        clock.tick(30)
        
        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        #Modify ufo value
        ufo_x += 5
        #Check boundaries
        if ufo_x > screen.get_width():
            ufo_x = 0
            
        #Refresh screen
        screen.blit(background, (0, 0))
        screen.blit(ufo, (ufo_x, ufo_y))
        pygame.display.flip()
        
    pygame.quit()

if__name__ == "__main__":
    main()
            
    
    