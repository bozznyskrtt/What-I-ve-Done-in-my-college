import pygame
import random
import sys
from rect101 import Rectangle

# statics
pygame.init()

width, height = 1280, 700
rect_size_x, rect_size_y = 35, 35
opsset = []
GO = pygame.font.Font(None, 50)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Move Square with Keyboard")
rectangle = Rectangle(10, 10, (width // 2) - (rect_size_x//2), (height // 2) - (rect_size_y//2), rect_size_x, rect_size_y, (118, 181, 232), screen, width, height, 0)
numbers_list_x = list(range(0, width // 2 - 65)) + list(range(width // 2 + 65, 1260))
numbers_list_y = list(range(0, height // 2 - 65)) + list(range(height // 2 + 65, 680))
text = "STUPID?"
text_surface = GO.render(text, True, (255, 255, 255))  # `True` for anti-aliased text
text_rect = text_surface.get_rect()
text_rect.center = (width // 2, height // 2)


def start1():
    opsset.clear()
    for i in range(25):
        ops = Rectangle(random.randint(1, 3), random.randint(1, 3), random.choice(numbers_list_x),
                        random.choice(numbers_list_y), 20, 20, (200, 0, 0), screen, width, height, random.randint(1, 4))
        opsset.append(ops)
    rectangle.x = (width // 2) - (rect_size_x//2)
    rectangle.y = (height // 2) - (rect_size_y//2)


start1()

while True:
    # input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quitting")
            pygame.quit()
            exit(0)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if mouse_click[0] == 1:
        rectangle.x = mouse_x
        rectangle.y = mouse_y

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if rectangle.x > 0:
            rectangle.x -= rectangle.speed_x
    if keys[pygame.K_RIGHT]:
        if rectangle.x < width - rectangle.width:
            rectangle.x += rectangle.speed_x
    if keys[pygame.K_UP]:
        if rectangle.y > 0:
            rectangle.y -= rectangle.speed_y
    if keys[pygame.K_DOWN]:
        if rectangle.y < height - rectangle.height:
            rectangle.y += rectangle.speed_y

    screen.fill((30, 40, 50))
    rectangle.gen()
    for i in opsset:
        i.gen()
        i.move()
    for i in opsset:
        i.bounce()
        if bool(i.collision(rectangle.x, rectangle.y, rectangle.width, rectangle.height)):
            screen.blit(text_surface, text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            start1()

    pygame.display.flip()
    pygame.time.Clock().tick(60)
