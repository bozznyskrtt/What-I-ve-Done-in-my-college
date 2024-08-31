import pygame

class Ball:
    def __init__(self,screen,x,y,width,height,screen_width,screen_height):
        self.screen = screen
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.height = height
        self.width = width
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rect = pygame.Rect(self.x, self.y, self.screen_width, self.height)
    def update(self,dt):
        self.rect.x += self.dx*dt
        self.rect.y += self.dy*dt
    def process_input(self,keys):
        if keys[pygame.K_w]:
            self.dy -= 10
        if keys[pygame.K_s]:
            self.dy += 10
        if keys[pygame.K_a]:
            self.dx -= 10
        if keys[pygame.K_d]:
            self.dx += 10
    def render(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)