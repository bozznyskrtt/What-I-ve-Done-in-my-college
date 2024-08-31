import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Centered Text Example')

# Color definitions
black = (0, 0, 0)
white = (255, 255, 255)

# Create a font object
font_size = 36
font = pygame.font.Font(None, font_size)

# Render the text into an image (surface)
text = "Hello, Pygame!"
text_surface = font.render(text, True, white)  # `True` for anti-aliased text
text_rect = text_surface.get_rect()

# Calculate the position for the text to be centered
text_rect.center = (screen_width // 2, screen_height // 2)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(black)

    # Blit the text surface onto the screen at the calculated position
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
