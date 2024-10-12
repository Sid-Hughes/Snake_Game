import pygame
pygame.init()
dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake game by Edureka')

class snake:
    def __init__(self):
        self.block_width = 10
        self.block_height = 10
        self.head = pygame.Rect(dis.get_width()/2, dis.get_height()/2, 10, 10)

    def move_up(self):
        self.head.y -= 10
    def move_down(self):
        self.head.y += 10
    def move_left(self):
        self.head.x -= 10
    def move_right(self):
        self.head.x += 10




white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

x1 = 400
y1 = 300

snake = snake()

clock = pygame.time.Clock()
pygame.key.set_repeat(1, 30)
"""
Main game loop
"""
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            snake.move_up()
        if keys[pygame.K_DOWN]:
            snake.move_down()
        if keys[pygame.K_LEFT]:
            snake.move_left()
        if keys[pygame.K_RIGHT]:
            snake.move_right()
        dis.fill(white)
        pygame.draw.rect(dis, blue, snake.head)
        pygame.display.update()

        clock.tick(30)

pygame.quit()
quit()
