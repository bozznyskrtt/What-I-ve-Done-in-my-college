# main.py

import pygame
from Player import Player

pygame.init()
clock = pygame.time.Clock()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test Sprites")

moving_sprite = pygame.sprite.Group()

player = Player(100, 100)

moving_sprite.add(player)

background = pygame.transform.scale(pygame.image.load("TX Tileset Grass.png"), (800, 600))

print(background.get_size())


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                player.switch_animation()

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    moving_sprite.draw(screen)
    player.update()
    pygame.display.flip()

    clock.tick(60)
