import pygame
from rect101 import Rectangle
from ball import Ball
import sys


class Maingame:
    # statics
    pygame.init()

    width = 1280
    height = 700

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Move Square with Keyboard")

    # square
    rectangle_color = (255, 255, 255)
    rectangle_width = 100
    rectangle_height = 100
    rectangle_pos_x = (width // 2) - rectangle_width // 2
    rectangle_pos_y = (height // 2) - rectangle_height // 2
    rectangle_speed = 10


    # chara_image = pygame.image.load()
    # chara_image_resize = pygame.transform.scale(chara_image,(width,height))
    #
    # screen.blit(chara_image,(rectangle_pos_x,rectangle_pos_y))

    # function
    # def is_collision(rect1, rect2):
    #     return not (
    #         rect1.x > rect2.x + rect2.width or
    #         rect1.x + rect1.width < rect2.x or
    #         rect1.y > rect2.y + rect2.height or
    #         rect1.y + rect1.height < rect2.y
    #     )
    # class GameMain:

    # loop
    while True:
        # input
        my_ball = Ball(screen, 50, 50, 50, 50, width, height)
        rectangle = Rectangle(10, 0, 0, 100, 100, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quitting")
                pygame.quit()
                exit(0)

                # mouse_x, mouse_y = pygame.mouse.get_pos()
                # mouse_click = pygame.mouse.get_pressed()
                #
                # if mouse_click[0] == 1:
                #     rectangle_pos_x = mouse_x
                #     rectangle_pos_y = mouse_y

                keys = pygame.key.get_pressed()

                if keys[pygame.K_LEFT]:
                    if rectangle_pos_x > 0:
                        rectangle_pos_x -= rectangle_speed
                if keys[pygame.K_RIGHT]:
                    if rectangle_pos_x < width - rectangle_width:
                        rectangle_pos_x += rectangle_speed
                if keys[pygame.K_UP]:
                    if rectangle_pos_y > 0:
                        rectangle_pos_y -= rectangle_speed
                if keys[pygame.K_DOWN]:
                    if rectangle_pos_y < height - rectangle_height:
                        rectangle_pos_y += rectangle_speed

                # render
                screen.fill((30, 40, 50))
                pygame.draw.rect(screen, rectangle.color, (rectangle.x, rectangle.y, rectangle.width, rectangle.height))
                my_ball.render()
                pygame.display.flip()
                pygame.time.Clock().tick(60)
