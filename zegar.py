import pygame
import time
import math

pygame.init()

# Screen dimensions
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Analog Clock Simulation')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Clock settings
center = (width // 2, height // 2)
clock_radius = 250

# Function to draw the clock face
def draw_clock_face():
    pygame.draw.circle(screen, black, center, clock_radius, 5)
    for hour in range(1, 13):
        angle = math.radians(360 / 12 * hour - 90)
        x = center[0] + clock_radius * 0.85 * math.cos(angle)
        y = center[1] + clock_radius * 0.85 * math.sin(angle)
        pygame.draw.circle(screen, black, (int(x), int(y)), 5)

# Function to draw the clock hands
def draw_hand(angle, length, color, width):
    x = center[0] + length * math.cos(angle)
    y = center[1] + length * math.sin(angle)
    pygame.draw.line(screen, color, center, (int(x), int(y)), width)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
    draw_clock_face()

    # Get current time
    now = time.localtime()
    second = now.tm_sec
    minute = now.tm_min
    hour = now.tm_hour % 12

    # Calculate angles for the hands
    second_angle = math.radians(360 / 60 * second - 90)
    minute_angle = math.radians(360 / 60 * minute - 90 + (6 * second / 60))
    hour_angle = math.radians(360 / 12 * hour - 90 + (30 * minute / 60))

    # Draw hands
    draw_hand(second_angle, clock_radius * 0.9, red, 2)
    draw_hand(minute_angle, clock_radius * 0.75, blue, 4)
    draw_hand(hour_angle, clock_radius * 0.5, green, 6)

    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()
