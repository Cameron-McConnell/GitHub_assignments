# FINAL PROJECT
README.md
  The objective for this game is to dodge the stars that are falling from the sky by moving the player left and right with the arrow keys. If your player is hit by a star the game is over and you will restart. There is a point system to the game where each star you dodge earns you 10 points, but this function I could not get to work.

  I have learned a lot about programming this semster, but I cannot figure out how to get things going or where I went wrong. I learned what lists, tupules, and dictionaries are and why they are important when programming. I have also learned the differnce of for and while loops, while also learning about boolean which can either be true or false. 
  Throughout the semester I was able to get my code running and working, but once we shifted to game development my codes have never been able to run. This part has been frustrating and confusing at times where the code and algorithm line u but my input error has  set me back along the way. I would like to imporve in game development aspect of computer programming and also be able to know where i went wrong and how to fix it. 
  I would focus on one thing at a time instead of trying to understand the whole thing at once, I belive my problem from not retaining any informaiton was becasue I was focused on the entire project when I should have broken it down into steps first; meaning I should have understood one thing first before going on to the next topic. In all honesty, I tried to stay on topic and on time with the rubric, but my biggest issue was trying to upload images for background and for sprites. I was able to download them, but when I tried to put the images in to load, they would not load or would not be found in the working directory. I watched countless of YouTube videos and read a vast majority of articles on how to do so, but I would always come up short. This was a major set back and my game did not go as planned, so I had to come up with a plan B that did not need images, or sounds, but to just make a game that would work or at least pop up. 

Documentation CS120 Final Game
Import pygame
Import time
Import random
Pygame.font.init() 

#Creating the window
Width, Height = 640, 480
Window (Win)  = pygame.display.set_mode((Width, Height))
Pygame.display.set_caption(“Dodge the stars”)

#Adding background image
Background(BG) =pygame.transform.scale pygame.image.load(“image”)
Player_width = 40
Player_height = 60 
Player_velocity = 5
Star_width = 10
Star_height = 20
Star_velocity = 3

Font = pygame.font.SysFont(“comicsans”, 30)

Def draw(player, elapsed_time, stars):
Win.blit(BG, (0,0))
Time_text = Font.render(f”Time: {round(elapsed_time)}s”, 1, “white”)
Win.blit(time_text, (10,10))
Pygame.draw.rect(Win, “blue”, player)

For star in stars:
Pygame.draw.rect(Win, “white”, star)
Pygame.display.update()

Def main():
Run = true
Player = pygame.rect(200, Height – player_height, player_width, player_height)
Clock = pygame.time.Clock()
Start_time = time.time()
Elapsed_time = 0

Star_add_increment = 2000
Star_count = 0

Stars = []
Hit = False

While run:
Star_count += Clock.tick(60)
Elapsed_time = time.time() - start_time

If star_count > star_add_increment:
for_in range(3):
star_x = random.randint(0, Width – Star_width)
star = pygame.Rect(star_x, -Star_Height, Star_width, Star_height)
stars.append(star)

star_add_increment = max(200, star_add_increment – 50)
star_count = 0

for event in pygame.event.get():
if event.type ==pygame.QUIT:
run = False
Break

Keys = pygame.key.get_pressed()
If keys[pygame.K_Left] and player.x - Player_velocity >=0:
Player.x - = Player_veloctiy
If keys[pygame.K_Right] and player.x + Player_velocity + player_width <= Width:
Player.x += Player_velocity

For star in stars[:]: 
Star.y += star_velocity
If star.y  > height:
stars.remove(star)
Elif star.y >= player.y and star.colliderect(player):
stars.remove(star)
hit = True
break

If hit:
lost_text = Font.render(“You Lost!”, 1, “white”)
Win.blit(lost_text, (Width/2 - lost_text.get_width()/2, Height/2 - lost_text.get_height()/2))
Pygame.display.update()
Pygame.time.delay(4000)
break

Draw(player, elapsed_time, stars)
Pygame.quit()

If__name__== “__main__”:
Main()
