import pygame
from OOP.Game import Game
from OOP.Analysis import Analysis

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 720, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Semestra darbs")

clock = pygame.time.Clock()
game = Game()
analysis = Analysis()
running = True

while running:
    dt = clock.tick(60)/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game.game_over:
                mouse_pos = pygame.mouse.get_pos()
                if game.circle.is_clicked(mouse_pos, update_spawn=False):
                    reaction_time = pygame.time.get_ticks() - game.circle.spawn_time

                    analysis.record_clicks(
                        game.circle.x,
                        game.circle.y,
                        mouse_pos[0],
                        mouse_pos[1],
                        reaction_time,
                    )

                    game.circle.hit_count += 1
                    game.circle.level_up()
                    game.circle.spawn()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game.game_over:
                analysis.show_results()
                running = False

    if not game.game_over:
        game.circle.update(dt)
        game.check_miss()

    display_surface.fill("white")

    if not game.game_over:
        game.circle.draw(display_surface)
    else:
        font = pygame.font.SysFont(None, 60)
        font2 = pygame.font.SysFont(None, 40)

        text = font.render("Game over", True, (133, 197, 232))
        text_rect = text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 30))
        display_surface.blit(text, text_rect)

        text_R = font2.render(
            "Press 'r' to download your analysis results as .pdf", True, (133, 197, 232))
        text_R_rect = text_R.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 30))
        display_surface.blit(text_R, text_R_rect)

    pygame.display.update()

pygame.quit()
