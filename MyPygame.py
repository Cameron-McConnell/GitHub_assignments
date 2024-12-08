import pygame
import random
import time 


pygame.init()
pygame.font.init()

#Creating Window
WIDTH, HEIGHT = 640,480

screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill("blue")


#Creating caption/title
pygame.display.set_caption("My Pygame")

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VELOCITY = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VELOCITY = 3

FONT = pygame.font.SysFont("Yugi Mai", 36)

# Set draw function
def draw(player, elasped_time, stars):
    pygame.surface
    elapsed_time = 0
    
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    screen.blit(time_text, (10,10))
                
    pygame.draw.rect(screen, "yellow", player)
    
    for star in stars:
        pygame.draw.rect(screen, "white",star)
    
    pygame.display.update()


#Set main function
def main():
    game_running = True
    
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,
                         PLAYER_WIDTH,PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    
    star_add_increment = 2000
    star_count = 0
    
    stars = []
    hit = False
    while game_running:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                stars = pygame.rect(star_x, - STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                star.append(star)
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >= 0:
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + player.width <= WIDTH:
            player.x += PLAYER_VELOCITY
            
        for star in stars[:]:
            star.y += STAR_VELOCITY
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        
        if hit:
            lost_text = FONT.render("Game Over!", 1, "white")
            screen.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time,delay(4000)
            break
        
        draw(player, elapsed_time,stars)
        
    pygame.quit()
        
main()
            