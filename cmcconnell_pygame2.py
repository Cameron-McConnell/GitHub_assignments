#Initialize
import pygame

def main():
    pygame.init()
    
    #Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Moving box")
    
    #Entities
    #green background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 255, 0))
    
    #Make a yellow 25 x 25 box
    box = pygame.Surface((25, 25))
    box = box.convert()
    box.fill((255, 255, 0))
    
    #Set up some box variables
    box_x = 0
    box_y = 200
    
    #Action
    
        #Assign
    clock = pygame.time.Clock()
    keepGoing = True
    
        #Loop
    while keepGoing:
        
        #Time
        clocl.tick(30)
        
        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        #Modify box value
        box_x += 5
        
        #Check boundaries
        if box_x > screen.get_width():
            box_x = 0
            
        #Refresh screen
        screen.blit(background, (0, 0))
        screen.blit(box, (box_x, box_y))
        pygame.display.flip()
        
    pygame.quit()
    
if__name__ == "__main__":
    main()