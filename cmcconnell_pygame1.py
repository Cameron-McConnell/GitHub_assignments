def main():
    #I - Import and initialize
    import pygame
    pygame.init()
    
    #D - Display configuration
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Welcome user!")
    
    #E - Entities
    background = pygame.Surface(screen.get_size())
    backgorund.fill(pygame.Color("green"))
    
    #Action (A.L.T.E.R)
    
        #A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True
        
        #L - Set up main loop
    while keepGoing:
        
        #T - Timer to set frame rate
        clock.tick(30)
        
        #E - Event-handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        #R Refresh display
        screen.blit(background, (0,0))
        pygame.display.flip()
    
    pygame.quit()
    
if__name__ == "__main__":
    main()