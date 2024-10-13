import random

import pygame

pygame.init()
dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake game by Edureka')

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
x1 = 400
y1 = 300


class Snake:
    def __init__(self):
        self.block_width = 10
        self.block_height = 10
        self.colour = blue
        self.head = pygame.Rect(dis.get_width() / 2, dis.get_height() / 2, self.block_width, self.block_height)

    def move_up(self):
        if self.head.y <= 0:
            self.head.y = dis.get_height() - self.block_height
        else:
            self.head.y -= self.block_height

    def move_down(self):
        if self.head.y >= dis.get_height():
            self.head.y = self.block_height
        else:
            self.head.y += self.block_height

    def move_left(self):
        if self.head.x <= 0:
            self.head.x = dis.get_width() - self.block_width
        self.head.x -= self.block_width

    def move_right(self):
        if self.head.x >= dis.get_width():
            self.head.x = self.block_width
        self.head.x += self.block_width

    def move(self):
        if up:
            self.move_up()
        elif down:
            self.move_down()
        elif left:
            self.move_left()
        elif right:
            self.move_right()


class Food:
    def __init__(self):
        self.food_rad = 3
        self.colour = red
        self.center_x = round(random.randint(0, dis.get_width()-snake.block_width)/10)*10+5
        self.center_y = round(random.randint(0, dis.get_height()-snake.block_height)/10)*10+5

        self.eaten = False

    def draw_food(self):
        if self.eaten:
            self.center_x = random.randint(0, dis.get_width())
            self.center_y = random.randint(0, dis.get_height())
            self.eaten = False
        pygame.draw.circle(dis, self.colour, (self.center_x, self.center_y), self.food_rad)

    def eat(self):
        self.eaten = True


snake = Snake()
food = Food()

clock = pygame.time.Clock()
pygame.key.set_repeat(1, 20)

up = False
down = False
left = False
right = False

"""
Main game loop
"""
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False

    snake.move()
    dis.fill(white)
    pygame.draw.rect(dis, blue, snake.head)
    food.draw_food()
    pygame.display.update()

    clock.tick(20)

pygame.quit()
quit()

#
# keys = pygame.key.get_pressed()
#     if keys[pygame.K_UP]:
#         snake.move_up()
#         print("Moving Up")
#     if keys[pygame.K_DOWN]:
#         snake.move_down()
#         print("Moving Down")
#     if keys[pygame.K_LEFT]:
#         snake.move_left()
#         print("Moving Left")
#     if keys[pygame.K_RIGHT]:
#         snake.move_right()
#         print("Moving Right")
