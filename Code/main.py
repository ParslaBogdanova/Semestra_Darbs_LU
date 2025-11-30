import pygame
from OOP.Game import Game

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 720, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pastāvīgais darbs")

clock = pygame.time.Clock()
game = Game()
running = True

while running:
    dt = clock.tick(60)/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game.game_over:
                mouse_pos = pygame.mouse.get_pos()
                if game.circle.is_clicked(mouse_pos):
                    print("Hit")
                    game.circle.hit_count += 1
                    game.circle.level_up()

    if not game.game_over:
        game.circle.update(dt)
        game.check_miss()

    display_surface.fill("white")

    if not game.game_over:
        game.circle.draw(display_surface)
    else:
        font = pygame.font.SysFont(None, 60)
        text = font.render("Game over", True, (133, 197, 232))
        text_rect = text.get_rect()
        text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        display_surface.blit(text, text_rect)

    pygame.display.update()

pygame.quit()
