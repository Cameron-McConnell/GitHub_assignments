import pygame, random, math, time
pygame.init()
pygame.mixer.init()

class Scene(object):
    """ encapsulates the IDEA / ALTER framework """

    def __init__(self, size=(640, 480), player_image="racing car.png", object_image="gas can.png"):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill("green")

        # Set the image paths for the player and falling objects (default to the same directory)
        self.player_image = player_image
        self.object_image = object_image

        # Player Sprite (the character to move)
        self.player = Sprite(self, self.player_image)  # Load player image
        self.player.setSize(50, 50)  # Optional: scale the image if needed
        self.player.y = self.screen.get_height() - 50  # Position at bottom of the screen
        self.player.dx = 50

        # Falling objects
        self.objects = []
        self.spawn_interval = 30
        self.spawn_timer = 0

        # Game score
        self.score = 0
        self.font = pygame.font.SysFont(None, 36)

        # Add player sprite to the main group
        self.sprites = [self.player]
        self.groups = []
    
    def start(self):
        self.mainSprites = pygame.sprite.OrderedUpdates(self.sprites)
        self.groups.append(self.mainSprites)

        self.screen.blit(self.background, (0, 0))
        self.clock = pygame.time.Clock()
        self.keepGoing = True
        while self.keepGoing:
            self.__mainLoop()
        pygame.quit()

    def __mainLoop(self):
        self.clock.tick(30)  # Limit frame rate to 30 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.keepGoing = False

        self.handle_input()
        self.spawn_objects()
        self.update_objects()
        self.check_collisions()

        # Draw everything
        self.screen.fill((0, 0, 0))  # Clear screen with black background
        for group in self.groups:
            group.clear(self.screen, self.background)
            group.update()
            group.draw(self.screen)

        # Draw the score
        self.draw_score()

        pygame.display.flip()

    def handle_input(self):
        # Player movement control (left and right)
        if self.isKeyPressed(pygame.K_LEFT):
            self.player.dx = -5
        elif self.isKeyPressed(pygame.K_RIGHT):
            self.player.dx = 5
        else:
            self.player.dx = 0
        
        self.player.x += self.player.dx

    def spawn_objects(self):
        """ Spawn new falling objects every few frames """
        if self.spawn_timer >= self.spawn_interval:
            new_object = Sprite(self, self.object_image)  # Load object image
            new_object.setSize(30, 30)  # Optional: scale the image if needed
            new_object.x = random.randint(0, self.screen.get_width() - 30)
            new_object.y = 0  # Spawn at the top
            new_object.dy = 5  # Falling speed
            self.objects.append(new_object)
            self.sprites.append(new_object)  # Add to sprite group
            self.spawn_timer = 0  # Reset the spawn timer
        else:
            self.spawn_timer += 1

    def update_objects(self):
        """ Update the positions of all objects """
        for obj in self.objects:
            obj.y += obj.dy  # Fall down

            if obj.y > self.screen.get_height():
                self.objects.remove(obj)  # Remove off-screen objects
                self.sprites.remove(obj)

    def check_collisions(self):
        """ Check if the player caught any objects """
        for obj in self.objects:
            if self.player.collidesWith(obj):
                self.objects.remove(obj)
                self.sprites.remove(obj)
                self.score += 1  # Increase score when catching an object

    def draw_score(self):
        """ Display the current score on the screen """
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))  # Position at top-left

    def isKeyPressed(self, key):
        keysDown = pygame.key.get_pressed()
        return keysDown[key]


class Sprite(pygame.sprite.Sprite):
    """ Basic sprite class with image handling """

    def __init__(self, scene, image_file):
        pygame.sprite.Sprite.__init__(self)
        self.scene = scene
        self.screen = scene.screen

        # Load the image and set the size
        self.image = self.load_image(image_file)  # Load image with path handling
        self.rect = self.image.get_rect()  # Get image rectangle

        # Set position
        self.x = 0
        self.y = 0
        self.dx = 0  # Horizontal speed
        self.dy = 0  # Vertical speed

    def load_image(self, image_file):
        """ Loads the image, checking if it's a relative or absolute path """
        # Check if it's a relative path or an absolute path
        try:
            # If it is a relative path, load the image directly
            return pygame.image.load(image_file).convert_alpha()
        except pygame.error:
            # Handle invalid file paths
            print(f"Error: Could not load image file {image_file}. Check the file path.")
            pygame.quit()
            quit()

    def setSize(self, width, height):
        """ Rescale the image to a new size """
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()  # Update rect to new size

    def collidesWith(self, target):
        """ Check if this sprite collides with another sprite """
        collision = False
        if self.visible:
            if target.visible:
                if self.rect.colliderect(target.rect):
                    collision = True
        return collision

    def process(self):
        pass

    def hide(self):
        self.oldPosition = self.rect.center
        self.x = -1000
        self.y = -1000
        self.visible = False
        
    def show(self):
        self.visible = True
        self.x = self.oldPosition[0]
        self.y = self.oldPosition[1]
        
    def isKeyPressed(self, key):
        return self.scene.isKeyPressed(key)    
    
    def distanceTo(self, point):
        """ returns distance to any point in pixels
            can be used in circular collision detection
        """
        (pointx, pointy) = point
        dx = self.x - pointx
        dy = self.y - pointy
        
        dist = math.sqrt((dx * dx) + (dy * dy))
        return dist
    
    def dirTo(self, point):
        """ returns direction (in degrees) to 
            a point """
        (pointx, pointy) = point
        dx = self.x - pointx
        dy = self.y - pointy
        dy *= -1
        
        radians = math.atan2(dy, dx)
        dir = radians * 180 / math.pi
        dir += 180
        return dir
    
    def drawTrace(self, color=(0x00, 0x00, 0x00)):
        pygame.draw.line(self.scene.background, color, self.oldCenter,
                         self.rect.center, 3)
        self.screen.blit(self.scene.background, (0, 0))
        self.oldCenter = self.position


# Example usage:
if __name__ == "__main__":
    # Set file paths for images
    player_image_path = "racing car.png"  # Change this path if needed
    object_image_path = "gas can.png"  # Change this path if needed

    # Create scene with specified images
    game_scene = Scene(player_image=player_image_path, object_image=object_image_path)
    game_scene.start()
