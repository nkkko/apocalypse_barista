import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 1280, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Apocalypse Barista")

# Set up the clock for a decent framerate
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define grid size for procedural generation
GRID_SIZE = 800  # The world is divided into GRID_SIZE x GRID_SIZE cells

# Initialize groups
barriers = pygame.sprite.Group()
enemies = pygame.sprite.Group()
items = pygame.sprite.Group()

# Keeps track of generated cells
generated_cells = set()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.velocity = 5
        self.hp = 100
        self.items_collected = 0

class Barrier(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = 2
        self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        self.move_timer = 0
        self.move_interval = random.randint(30, 120)  # Promjena smjera svakih 0.5-2 sekunde

    def update(self):
        self.move_timer += 1
        if self.move_timer >= self.move_interval:
            self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
            self.move_timer = 0
            self.move_interval = random.randint(30, 120)

        self.rect.x += self.direction[0] * self.velocity
        self.rect.y += self.direction[1] * self.velocity

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

def generate_terrain(cell_x, cell_y):
    """ Generate barriers, items, and enemies for the given cell coordinates. """
    # Ensure we don't regenerate the same cell
    if (cell_x, cell_y) in generated_cells:
        return

    # Randomly place some barriers
    for _ in range(5):
        width = random.randint(50, 150)
        height = random.randint(10, 50)
        x = random.randint(cell_x * GRID_SIZE, (cell_x + 1) * GRID_SIZE - width)
        y = random.randint(cell_y * GRID_SIZE, (cell_y + 1) * GRID_SIZE - height)
        barrier = Barrier(x, y, width, height)
        barriers.add(barrier)

    # Randomly place some items
    for _ in range(3):
        x = random.randint(cell_x * GRID_SIZE, (cell_x + 1) * GRID_SIZE - 20)
        y = random.randint(cell_y * GRID_SIZE, (cell_y + 1) * GRID_SIZE - 20)
        item = Item(x, y)
        items.add(item)

    # Randomly place some enemies
    for _ in range(2):
        x = random.randint(cell_x * GRID_SIZE, (cell_x + 1) * GRID_SIZE - 50)
        y = random.randint(cell_y * GRID_SIZE, (cell_y + 1) * GRID_SIZE - 50)
        enemy = Enemy(x, y)
        enemies.add(enemy)

    # Mark this cell as generated
    generated_cells.add((cell_x, cell_y))

# Create the player instance
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

# Offset for scrolling
offset_x = 0
offset_y = 0

# Font for displaying HP and items
font = pygame.font.Font(None, 36)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Store the previous position
    prev_offset_x, prev_offset_y = offset_x, offset_y

    # Update the offsets based on key presses
    if keys[pygame.K_LEFT]:
        offset_x += player.velocity
    if keys[pygame.K_RIGHT]:
        offset_x -= player.velocity
    if keys[pygame.K_UP]:
        offset_y += player.velocity
    if keys[pygame.K_DOWN]:
        offset_y -= player.velocity

    # Check collision with barriers
    for barrier in barriers:
        if player.rect.colliderect(barrier.rect.move(offset_x, offset_y)):
            offset_x, offset_y = prev_offset_x, prev_offset_y
            break

    # Ažuriraj neprijatelje
    enemies.update()

    # Check collision with enemies
    for enemy in enemies:
        screen.blit(enemy.image, (enemy.rect.x + offset_x, enemy.rect.y + offset_y))     # Crtaj neprijatelje s pomacima
        if player.rect.colliderect(enemy.rect.move(offset_x, offset_y)):
            player.hp -= 1
            if player.hp <= 0:
                running = False
            # Move the player away from the enemy
            if offset_x > prev_offset_x:
                offset_x = prev_offset_x - player.velocity
            elif offset_x < prev_offset_x:
                offset_x = prev_offset_x + player.velocity
            if offset_y > prev_offset_y:
                offset_y = prev_offset_y - player.velocity
            elif offset_y < prev_offset_y:
                offset_y = prev_offset_y + player.velocity

    # Check collision with items
    for item in items:
        if player.rect.colliderect(item.rect.move(offset_x, offset_y)):
            player.items_collected += 1
            items.remove(item)

    # Calculate which cell the player is currently in
    cell_x = (-offset_x + WIDTH // 2) // GRID_SIZE
    cell_y = (-offset_y + HEIGHT // 2) // GRID_SIZE

    # Generate terrain for the current cell and neighboring cells
    generate_terrain(cell_x, cell_y)
    generate_terrain(cell_x + 1, cell_y)
    generate_terrain(cell_x, cell_y + 1)
    generate_terrain(cell_x + 1, cell_y + 1)
    generate_terrain(cell_x - 1, cell_y)
    generate_terrain(cell_x, cell_y - 1)
    generate_terrain(cell_x - 1, cell_y - 1)
    generate_terrain(cell_x - 1, cell_y + 1)
    generate_terrain(cell_x + 1, cell_y - 1)

    # Clear the screen
    screen.fill(WHITE)

    # Draw barriers, items, and enemies with offsets
    for barrier in barriers:
        screen.blit(barrier.image, (barrier.rect.x + offset_x, barrier.rect.y + offset_y))

    for item in items:
        screen.blit(item.image, (item.rect.x + offset_x, item.rect.y + offset_y))

    for enemy in enemies:
        screen.blit(enemy.image, (enemy.rect.x + offset_x, enemy.rect.y + offset_y))

    # Draw the player always centered
    player_group.draw(screen)

    # Draw HP and items counter
    hp_text = font.render(f"HP: {player.hp}", True, BLACK)
    items_text = font.render(f"Items: {player.items_collected}", True, BLACK)
    screen.blit(hp_text, (10, 10))
    screen.blit(items_text, (10, 50))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()