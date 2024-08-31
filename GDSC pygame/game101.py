import pygame
import sys

#statics
pygame.init()

width = 1280
height = 700

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Move Square with Keyboard")

#square
rectangle_color = (255,255,255)
rectangle_width = 100
rectangle_height = 100
rectangle_pos_x = (width//2)-rectangle_width//2
rectangle_pos_y = (height//2)-rectangle_height//2
rectangle_speed = 10

rectangle2_color = (255,0,0)
rectangle2_width = 100
rectangle2_height = 100
rectangle2_pos_x = (width//4)-rectangle_width//2
rectangle2_pos_y = (height//4)-rectangle_height//2
rectangle2_speed = 4
GO = pygame.font.Font(None,30)
text_surface = GO.render('Game Over', True, (255,255,255))
# chara_image = pygame.image.load()
# chara_image_resize = pygame.transform.scale(chara_image,(width,height))
#
# screen.blit(chara_image,(rectangle_pos_x,rectangle_pos_y))

#function
# def is_collision(rect1, rect2):
#     return not (
#         rect1.x > rect2.x + rect2.width or
#         rect1.x + rect1.width < rect2.x or
#         rect1.y > rect2.y + rect2.height or
#         rect1.y + rect1.height < rect2.y
#     )

#loop
while True:
    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quitting")
            pygame.quit()
            exit(0)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if mouse_click[0] == 1:
        rectangle_pos_x = mouse_x
        rectangle_pos_y = mouse_y

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if rectangle_pos_x > 0:
            rectangle_pos_x -= rectangle_speed
    if keys[pygame.K_RIGHT]:
        if rectangle_pos_x < width-rectangle_width:
            rectangle_pos_x += rectangle_speed
    if keys[pygame.K_UP]:
        if rectangle_pos_y > 0:
            rectangle_pos_y -= rectangle_speed
    if keys[pygame.K_DOWN]:
        if rectangle_pos_y < height-rectangle_height:
            rectangle_pos_y += rectangle_speed

    if rectangle2_pos_x<rectangle_pos_x:
        rectangle2_pos_x += rectangle2_speed
    if rectangle2_pos_y<rectangle_pos_y:
        rectangle2_pos_y += rectangle2_speed
    if rectangle2_pos_x>rectangle_pos_x:
        rectangle2_pos_x-=rectangle2_speed
    if rectangle2_pos_y>rectangle_pos_y:
        rectangle2_pos_y-=rectangle2_speed

    if not (
            rectangle_pos_x > rectangle2_pos_x + rectangle2_width or
            rectangle_pos_x + rectangle_width < rectangle2_pos_x or
            rectangle_pos_y > rectangle2_pos_y + rectangle2_height or
            rectangle_pos_y + rectangle_height < rectangle2_pos_y
    ):
        rectangle_color = (255, 255, 255)
        rectangle_width = 100
        rectangle_height = 100
        rectangle_pos_x = (width // 2) - rectangle_width // 2
        rectangle_pos_y = (height // 2) - rectangle_height // 2
        rectangle_speed = 10

        rectangle2_color = (255, 0, 0)
        rectangle2_width = 100
        rectangle2_height = 100
        rectangle2_pos_x = (width // 4) - rectangle_width // 2
        rectangle2_pos_y = (height // 4) - rectangle_height // 2
        rectangle2_speed = 4
        screen.blit(text_surface, (width//2, height//2))
        pygame.display.flip()
        pygame.time.wait(2000)
        print("Game Over")


    #render
    screen.fill((30,40,50))
    pygame.draw.rect(screen, rectangle_color, (rectangle_pos_x, rectangle_pos_y, rectangle_width, rectangle_height))
    pygame.draw.rect(screen, rectangle2_color, (rectangle2_pos_x, rectangle2_pos_y, rectangle2_width, rectangle2_height))
    pygame.display.flip()
    pygame.time.Clock().tick(60)

