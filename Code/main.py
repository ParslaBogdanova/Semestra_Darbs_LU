import pygame
from OOP.Circle import Circle

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1288, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pastāvīgais darbs")
running = True
circle = Circle()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if circle.is_clicked(mouse_pos):
                print("Hit")

    display_surface.fill("white")
    circle.draw(display_surface)
    pygame.display.update()

pygame.quit()
