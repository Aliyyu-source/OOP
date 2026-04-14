import pygame
import math
import time

pygame.init()

# Window setup
WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lunar 7 and Lunar 9 travel to the moon!")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Fonts
font = pygame.font.SysFont("Arial", 24)
small_font = pygame.font.SysFont("Arial", 16)

# Coordinate system margins
LEFT_MARGIN = 50
BOTTOM_MARGIN = 550
RIGHT_MARGIN = 650
TOP_MARGIN = 50

# Convert plot coordinates (0–100) to screen pixels
def to_screen_coords(x, y):
    sx = LEFT_MARGIN + (x / 100) * (RIGHT_MARGIN - LEFT_MARGIN)
    sy = BOTTOM_MARGIN - (y / 100) * (BOTTOM_MARGIN - TOP_MARGIN)
    return [sx, sy]

# Logical positions in plot space
lunar7_start = (20, 0)
lunar9_start = (40, 0)
moon_plot = (60, 80)

# Convert to screen coordinates
lunar7_pos = to_screen_coords(*lunar7_start)
lunar9_pos = to_screen_coords(*lunar9_start)
moon_pos = to_screen_coords(*moon_plot)

# Distance tracking
lunar7_distance = 0.0
lunar9_distance = 0.0

# ⭐ Slower movement speed
SPEED = 0.7

# Draw axes with ticks and numbers
def draw_axes():
    pygame.draw.line(screen, WHITE, (LEFT_MARGIN, BOTTOM_MARGIN), (RIGHT_MARGIN, BOTTOM_MARGIN), 2)
    pygame.draw.line(screen, WHITE, (LEFT_MARGIN, BOTTOM_MARGIN), (LEFT_MARGIN, TOP_MARGIN), 2)

    # X ticks
    for i in range(0, 101, 10):
        x = LEFT_MARGIN + (i / 100) * (RIGHT_MARGIN - LEFT_MARGIN)
        pygame.draw.line(screen, WHITE, (x, BOTTOM_MARGIN - 5), (x, BOTTOM_MARGIN + 5), 2)
        screen.blit(small_font.render(str(i), True, WHITE), (x - 8, BOTTOM_MARGIN + 8))

    # Y ticks
    for i in range(0, 101, 10):
        y = BOTTOM_MARGIN - (i / 100) * (BOTTOM_MARGIN - TOP_MARGIN)
        pygame.draw.line(screen, WHITE, (LEFT_MARGIN - 5, y), (LEFT_MARGIN + 5, y), 2)
        screen.blit(small_font.render(str(i), True, WHITE), (LEFT_MARGIN - 30, y - 8))

# Euclidean distance
def dist(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

# Countdown
def countdown():
    for i in range(3, 0, -1):
        screen.fill(BLACK)
        draw_axes()
        text = font.render(f"Launching in {i}...", True, WHITE)
        screen.blit(text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
        pygame.display.update()
        time.sleep(1)

# Run countdown
countdown()

# “Here you go!” screen
screen.fill(BLACK)
draw_axes()
msg = font.render("Here you go!", True, WHITE)
msg_rect = msg.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(msg, msg_rect)
pygame.display.update()
time.sleep(1)

running = True
mission_complete = False
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    draw_axes()

    # Draw moon
    pygame.draw.circle(screen, YELLOW, (int(moon_pos[0]), int(moon_pos[1])), 18)

    # Move rockets
    if not mission_complete:
        # Lunar 7
        dx = moon_pos[0] - lunar7_pos[0]
        dy = moon_pos[1] - lunar7_pos[1]
        d = math.sqrt(dx*dx + dy*dy)
        if d > 1:
            step_x = (dx / d) * SPEED
            step_y = (dy / d) * SPEED
            lunar7_pos[0] += step_x
            lunar7_pos[1] += step_y
            lunar7_distance += math.sqrt(step_x**2 + step_y**2)

        # Lunar 9
        dx2 = moon_pos[0] - lunar9_pos[0]
        dy2 = moon_pos[1] - lunar9_pos[1]
        d2 = math.sqrt(dx2*dx2 + dy2*dy2)
        if d2 > 1:
            step_x2 = (dx2 / d2) * SPEED
            step_y2 = (dy2 / d2) * SPEED
            lunar9_pos[0] += step_x2
            lunar9_pos[1] += step_y2
            lunar9_distance += math.sqrt(step_x2**2 + step_y2**2)

        # Prevent collision
        if dist(lunar7_pos, lunar9_pos) < 25:
            lunar9_pos[0] += 2

        # Check arrival
        if dist(lunar7_pos, moon_pos) < 20 and dist(lunar9_pos, moon_pos) < 20:
            mission_complete = True

    # Draw rockets
    pygame.draw.circle(screen, RED, (int(lunar7_pos[0]), int(lunar7_pos[1])), 8)
    pygame.draw.circle(screen, GREEN, (int(lunar9_pos[0]), int(lunar9_pos[1])), 8)

    # Legend
    screen.blit(small_font.render("Lunar 7", True, RED), (450, 80))
    screen.blit(small_font.render("Lunar 9", True, GREEN), (450, 100))
    screen.blit(small_font.render("Moon", True, YELLOW), (450, 120))

    # Distances
    screen.blit(small_font.render(f"Lunar 7 distance: {round(lunar7_distance, 2)} px", True, WHITE), (450, 150))
    screen.blit(small_font.render(f"Lunar 9 distance: {round(lunar9_distance, 2)} px", True, WHITE), (450, 170))

    # Title
    screen.blit(font.render("Lunar 7 and Lunar 9 travel to the moon!", True, WHITE), (80, 10))

    # Centered success message
    if mission_complete:
        msg = font.render("MISSION SUCCESSFUL!", True, WHITE)
        msg_rect = msg.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(msg, msg_rect)

    pygame.display.update()

pygame.quit()