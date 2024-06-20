import pygame

# ghjkldfghjk

pygame.init()

screen_height = 500
screen_width = 500

screen = pygame.display.set_mode([screen_height, screen_width])


# Class For Surfaces
class surface:
    global screen_height, screen_width, screen

    def __init__(self):
        self.height = 95
        self.width = 95
        self.center = (
            ((screen_height / 2) - (self.height / 2)),
            ((screen_width / 2) - (self.height / 2)),
        )
        self.color = None
        self.surface = pygame.Surface((self.height, self.width))

    def place(self, center, x=0, y=0):
        if center:
            screen.blit(self.surface, self.center)
        else:
            screen.blit(self.surface, (x, y))

    def set_color(self, r, b, g):
        self.surface.fill((r, g, b))


surf_TL = surface()

running = True

while running == True:

    # CHECKS IF USER CLICKED QUIT BUTTON
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surf_TL.place(True)
    surf_TL.set_color(255, 255, 255)
    pygame.display.flip()


pygame.quit()
