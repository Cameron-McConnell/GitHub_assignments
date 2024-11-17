import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Game Settings
WIDTH, HEIGHT = 800, 600
FPS = 60
CAR_SPEED = 5
GRAVITY = 0.5
JUMP_FORCE = -10
BOOST_AMOUNT = 3
HILL_SPEED = 3
TIMER_START = 60

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hill Racing Game')

# Load assets
car_image = pygame.image.load("red rallye car straight0015.bmp")
car_image = car_image.convert_alpha()
car_image = pygame.transform.scale(car_image, (50, 30))

boost_image = pygame.image.load("groggy0000.bmp")
boost_image = boost_image.convert_alpha()
boost_image = pygame.transform.scale(boost_image, (30, 30))

obstacle_image = pygame.image.load("fir A ani0000.bmp")
obstacle_image = obstacle_image.convert_alpha()
obstacle_image = pygame.transform.scale(obstacle_image, (30, 30))

obstacle_image2 = pygame.image.load("jumping stone0000.bmp")
obstacle_image2 = obstacle_image2.convert_alpha()
obstacle_image2 = pygame.transform.scale(obstacle_image2, (30, 30))

font = pygame.font.SysFont(None, 36)

# Game Variables
car_x, car_y = 100, HEIGHT - 80
car_velocity = 0
car_speed = CAR_SPEED
timer = TIMER_START
score = 0
distance = 0
is_game_over = False
boost_available = False
obstacles = []
boosts = []
hill_speed = HILL_SPEED

def initialize_game():
    global car_x, car_y, car_velocity, car_speed, timer, score, distance, is_game_over, boost_available, obstacles, boosts
    car_x, car_y = 100, HEIGHT - 80
    car_velocity = 0
    car_speed = CAR_SPEED
    timer = TIMER_START
    score = 0
    distance = 0
    is_game_over = False
    boost_available = False
    obstacles.clear()
    boosts.clear()
    setup_obstacles()

def display_start_screen():
    screen.fill(WHITE)
    start_text = font.render("Press Start to Begin", True, BLACK)
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2))
    pygame.display.update()

def display_game_over_screen():
    screen.fill(WHITE)
    game_over_text = font.render("Game Over!", True, BLACK)
    score_text = font.render(f"Score: {score}", True, BLACK)
    restart_text = font.render("Press Restart to Play Again", True, BLACK)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 4))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 1.5))
    pygame.display.update()

def handle_input():
    global car_velocity
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and car_y == HEIGHT - 80:  # Only allow jump when on the ground
        car_velocity = JUMP_FORCE

def update_car_position():
    global car_y, car_velocity, car_x
    car_velocity += GRAVITY
    car_y += car_velocity
    if car_y >= HEIGHT - 80:  # If the car hits the ground
        car_y = HEIGHT - 80
        car_velocity = 0

    car_x += car_speed

def setup_obstacles():
    global obstacles, boosts
    for _ in range(5):  # Spawn 5 obstacles at random positions
        obstacles.append(pygame.Rect(WIDTH + random.randint(0, 500), HEIGHT - 80, 50, 50))
        boosts.append(pygame.Rect(WIDTH + random.randint(0, 500), HEIGHT - 200, 30, 30))

def update_obstacles():
    global obstacles, boosts
    for obs in obstacles:
        obs.x -= hill_speed
        if obs.x < 0:
            obstacles.remove(obs)
            obstacles.append(pygame.Rect(WIDTH + random.randint(0, 500), HEIGHT - 80, 50, 50))

    for boost in boosts:
        boost.x -= hill_speed
        if boost.x < 0:
            boosts.remove(boost)
            boosts.append(pygame.Rect(WIDTH + random.randint(0, 500), HEIGHT - 200, 30, 30))

def check_collisions():
    global is_game_over, car_x, car_y
    car_rect = pygame.Rect(car_x, car_y, 50, 30)
    for obs in obstacles:
        if car_rect.colliderect(obs):
            handle_crash()

    for boost in boosts:
        if car_rect.colliderect(boost):
            activate_boost()
            boosts.remove(boost)
            boosts.append(pygame.Rect(WIDTH + random.randint(0, 500), HEIGHT - 200, 30, 30))

def handle_crash():
    global car_speed, is_game_over
    car_speed = 0  # Stop the car
    is_game_over = True

def activate_boost():
    global car_speed, boost_available
    if boost_available:
        car_speed += BOOST_AMOUNT
        boost_available = False

def update_distance():
    global distance, car_speed
    distance += car_speed / FPS  # Update distance

def update_score():
    global score, distance, timer
    score = (timer * 10) + (distance * 5)

def check_game_over():
    global is_game_over, timer
    if timer <= 0 or is_game_over:
        is_game_over = True
        display_game_over_screen()

def game_loop():
    global timer, score, distance, car_x, car_y, is_game_over, car_speed, boost_available
    clock = pygame.time.Clock()
    initialize_game()

    while not is_game_over:
        delta_time = clock.tick(FPS) / 1000  # Time in seconds
        screen.fill(WHITE)

        # Game Logic
        if timer > 0:
            timer -= delta_time
            handle_input()
            update_car_position()
            check_collisions()
            update_obstacles()
            update_distance()
            update_score()
            check_game_over()
        else:
            is_game_over = True

        # Render Game
        screen.fill(WHITE)

        # Draw the car
        screen.blit(car_image, (car_x, car_y))

        # Draw obstacles
        for obs in obstacles:
            screen.blit(obstacle_image, (obs.x, obs.y))

        # Draw boost powerups
        for boost in boosts:
            screen.blit(boost_image, (boost.x, boost.y))

        # Display timer and score
        timer_text = font.render(f"Timer: {int(timer)}", True, BLACK)
        score_text = font.render(f"Score: {int(score)}", True, BLACK)
        screen.blit(timer_text, (10, 10))
        screen.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))

        pygame.display.update()

        if is_game_over:
            display_game_over_screen()

# Main Program
def main():
    display_start_screen()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # Press Enter to start the game
                game_loop()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:  # Press R to restart
                initialize_game()
                game_loop()

    pygame.quit()

if __name__ == "__main__":
    main()
