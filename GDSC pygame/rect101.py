import pygame


class Rectangle:
    def __init__(self, speed_x, speed_y, x, y, width, height, color, screen, screen_width, screen_height, movepattern):
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.movepattern = movepattern
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def gen(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        if self.movepattern == 1:
            if 0 < self.x < 1260:
                self.x += self.speed_x
            if 0 < self.y < 680:
                self.y += self.speed_y
        if self.movepattern == 2:
            if 0 < self.x < 1260:
                self.x -= self.speed_x
            if 0 < self.y < 680:
                self.y -= self.speed_y
        if self.movepattern == 3:
            if 0 < self.x < 1260:
                self.x -= self.speed_x
            if 0 < self.y < 680:
                self.y += self.speed_y
        if self.movepattern == 4:
            if 0 < self.x < 1260:
                self.x += self.speed_x
            if 0 < self.y < 680:
                self.y -= self.speed_y

    def bounce(self):
        bounced = False
        # Check for left or right boundary collision
        if self.x <= 0 or self.x + self.width >= self.screen_width:
            self.speed_x *= -1
            self.x = max(0, min(self.x, self.screen_width - self.width))
            bounced = True

        # Check for top or bottom boundary collision
        if self.y <= 0 or self.y + self.height >= self.screen_height:
            self.speed_y *= -1
            self.y = max(0, min(self.y, self.screen_height - self.height))
            bounced = True

        # If bounced, adjust position to ensure it's within bounds
        # genius mtf

        if bounced:
            if self.x <= 0:
                self.x = 1
            elif self.x + self.width >= self.screen_width:
                self.x = self.screen_width - self.width - 1

            if self.y <= 0:
                self.y = 1
            elif self.y + self.height >= self.screen_height:
                self.y = self.screen_height - self.height - 1

    def collision(self, recx, recy, rec_width, rec_height):
        if not (self.x > recx + rec_width or
                self.x + self.width < recx or
                self.y > recy + rec_height or
                self.y + self.height < recy):
            return True
