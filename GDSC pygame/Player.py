# Player.py

import pygame


class Player(pygame.sprite.Sprite):
  # Mandatory
    def __init__(self, pos_x, pos_y):
        super().__init__()  # Call the constructor of the base class
        self.sprites_idle = []
        self.sprites_idle.append(
            pygame.transform.scale(
                pygame.image.load("sprites/player-idle-1.png"), (200, 200)
            )
        )
        self.sprites_idle.append(
            pygame.transform.scale(
                pygame.image.load("sprites/player-idle-2.png"), (200, 200)
            )
        )
        self.sprites_idle.append(
            pygame.transform.scale(
                pygame.image.load("sprites/player-idle-3.png"), (200, 200)
            )
        )
        self.sprites_idle.append(
            pygame.transform.scale(
                pygame.image.load("sprites/player-idle-4.png"), (200, 200)
            )
        )

        self.sprites_run = []
        self.sprites_run.append(pygame.image.load("sprites/player-run-1.png"))
        self.sprites_run.append(pygame.image.load("sprites/player-run-2.png"))
        self.sprites_run.append(pygame.image.load("sprites/player-run-3.png"))
        self.sprites_run.append(pygame.image.load("sprites/player-run-4.png"))
        self.sprites_run.append(pygame.image.load("sprites/player-run-5.png"))
        self.sprites_run.append(pygame.image.load("sprites/player-run-6.png"))

        self.sprite_mode = 0
        self.current_sprite = 0
        self.image = self.sprites_idle[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

        # Mandatory
    def update(self):
        self.current_sprite += 0.1
        sprite_current = []
        if self.sprite_mode == 0:
            sprite_current = self.sprites_idle
        else:
            sprite_current = self.sprites_run

        if self.current_sprite >= len(sprite_current):
            self.current_sprite = 0

        self.image = sprite_current[int(self.current_sprite)]

        # TODO
        # Fix the code to be more organized (the render function should be here)

    def switch_animation(self):
        if self.sprite_mode == 0:
            self.sprite_mode = 1
        else:
            self.sprite_mode = 0

        self.current_sprite = 0
