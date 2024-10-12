import pygame
pygame.init()
dis = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Snake game by Edureka')

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        pygame.draw.rect(dis, blue, [400, 300, 10, 10])
        pygame.display.update()
        print(event)
pygame.quit()
quit()

