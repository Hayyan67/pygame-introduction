import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
SCREEN_WIDTH, SCREEN_HEIGHT=500, 500


background_image = pygame.transform.scale(pygame.image.load('car.png').convert(),(SCREEN_WIDTH, SCREEN_HEIGHT))


car_image = pygame.transform.scale(
pygame.image.load('car.png').convert_alpha(), (200, 300))
car_rect = car_image.get_rect(center=(SCREEN_WIDTH // 2,
                                      SCREEN_HEIGHT // 2 - 30 ))

text = pygame.font.Font(None, 36).render('Hello World ',True, pygame.Color('Black'))
text1 = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110 ))

def game_loop():
    clock=pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background_image, (0, 0))
        screen.blit(car_image, car_rect)
        screen.blit(text, text1)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

game_loop()
        