import pygame

pygame.init()
dis = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Snake game by Edureka')

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

x1 = 400
y1 = 300

snake_head = pygame.Rect(x1, y1, 10, 10)

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
            snake_head.move_ip(0, -10)
        if keys[pygame.K_DOWN]:
            snake_head.move_ip(0, 10)
        if keys[pygame.K_LEFT]:
            snake_head.move_ip(-10, 0)
        if keys[pygame.K_RIGHT]:
            snake_head.move_ip(10, 0)
        dis.fill(white)
        pygame.draw.rect(dis, blue, snake_head)
        pygame.display.update()


        clock.tick(30)
pygame.quit()
quit()
