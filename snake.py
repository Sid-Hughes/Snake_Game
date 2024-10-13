import random
from copy import deepcopy
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
    snake_length = 1

    def __init__(self):
        self.block_width = 10
        self.block_height = 10
        self.colour = blue
        self.head = pygame.Rect(dis.get_width() / 2, dis.get_height() / 2, self.block_width, self.block_height)
        self.prev_head = None
        self.score = 0
        self.body = []

    def draw_snake(self):
        pygame.draw.rect(dis, blue, self.head)
        if self.body:
            for body in self.body:
                body.draw()

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

    def move_head(self, up, down, left, right):
        self.prev_head = deepcopy(self.head)
        if up:
            self.move_up()
            self.move_body()
            print(f"Head of snake: {self.head}")
        elif down:
            self.move_down()
            self.move_body()
            print(f"Head of snake: {self.head}")
        elif left:
            self.move_left()
            self.move_body()
            print(f"Head of snake: {self.head}")
        elif right:
            self.move_right()
            self.move_body()
            print(f"Head of snake: {self.head}")


    def move_body(self):
        if self.body:
            for body in self.body:
                body.move()

    def eat(self):
        self.score += 1
        self.snake_length += 1
        print("NOM")
        if not self.body:
            self.body.append(SnakeBody(self, self.snake_length))
        else:
            self.body.append(SnakeBody(self.body[-1], self.snake_length))
        print(self.body)


class SnakeBody:
    def __init__(self, snake_head, body_num):
        print(f"Initialising SnakeBody {body_num-1}")
        self.pos = snake_head.prev_head
        self.snake_head = snake_head
        print(f"Position {self.pos}")
        self.prev_head = None
        self.body_num = body_num - 1

    def move(self):
        self.prev_head = deepcopy(self.pos)
        self.pos = self.snake_head.prev_head
        print(f"Body of snake{self.body_num}: {self.pos}")

    def draw(self):
        pygame.draw.rect(dis, blue, self.pos)



class Food:
    def __init__(self):
        self.food_rad = 3
        self.colour = red
        self.center_x = round(random.randint(0, dis.get_width() - snake.block_width) / 10) * 10 + 5
        self.center_y = round(random.randint(0, dis.get_height() - snake.block_height) / 10) * 10 + 5
        self.eaten = False

    def draw_food(self):
        if self.eaten:
            self.center_x = round(random.randint(0, dis.get_width() - snake.block_width) / 10) * 10 + 5
            self.center_y = round(random.randint(0, dis.get_height() - snake.block_height) / 10) * 10 + 5
            self.eaten = False
        pygame.draw.circle(dis, self.colour, (self.center_x, self.center_y), self.food_rad)

    def is_eaten(self, snake):
        if snake.head.x < self.center_x < snake.head.x + snake.block_width:
            if snake.head.y < self.center_y < snake.head.y + snake.block_height:
                self.eaten = True
                return True
        return False


snake = Snake()
food = Food()

clock = pygame.time.Clock()
pygame.key.set_repeat(1, 20)

score_font = pygame.font.SysFont("comicsansms", 35)


def your_score(score):
    value = score_font.render(f"Score: {score}", True, yellow)
    dis.blit(value, [0, 0])


"""
Main game loop
"""


def game_loop():
    up = False
    down = False
    left = False
    right = False
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

        snake.move_head(up, down, left, right)
        eat = food.is_eaten(snake)
        if eat:
            snake.eat()

        dis.fill(white)
        your_score(snake.score)
        snake.draw_snake()
        food.draw_food()
        pygame.display.update()

        clock.tick(20)

    pygame.quit()
    quit()


game_loop()
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
