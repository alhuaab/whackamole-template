import pygame
import random

#function to generate random position for mole
def random_pos(row, col, cell):
    x = random.randrange(0, col) * cell
    y = random.randrange(0, row) * cell
    return x, y

#function to draw grid
def draw_grid(screen, row, col, cell):
    for x in range(0, col * cell, cell):
        pygame.draw.line(screen, "black", (x, 0), (x, row * cell))
    for y in range(0, row * cell, cell):
        pygame.draw.line(screen, "black", (0, y), (col * cell, y))

def main():
    try:
        pygame.init()
        #grid
        cell = 32
        row = 512 // cell
        col = 640 // cell
        #other game features
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_x = 0
        mole_y = 0
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    mole_click = mole_image.get_rect(topleft=(mole_x, mole_y))
                    if mole_click.collidepoint(mouse_x, mouse_y):
                        mole_x, mole_y = random_pos(row, col, cell)
            screen.fill("light green")
            draw_grid(screen, row, col, cell)
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

