import pygame

# ghjkldfghjk

pygame.init()

screen_height = 505
screen_width = 505

screen = pygame.display.set_mode([screen_height, screen_width])


# Class For Surfaces
class surface:
    global screen_height, screen_width, screen

    def __init__(self):
        # self.center = (
        #     ((screen_height / 2) - (self.height / 2)),
        #     ((screen_width / 2) - (self.height / 2)),
        # )
        self.color = None
        self.surface = pygame.Surface((95, 95))
        self.Xpos = None
        self.Ypos = None

    def place(self):
        x = (((self.Xpos) - 1) * 100) + 5
        y = (((self.Ypos) - 1) * 100) + 5
        screen.blit(self.surface, (x, y))

    # def place_center(self):
    #     screen.blit(self.surface, self.center)

    def set_color(self, r, b, g):
        self.surface.fill((r, g, b))

    def set_pos(self, x, y):
        self.Xpos = x
        self.Ypos = y


surface_dict = {}
surface_names = []

for y in range(5):
    for x in range(5):
        surface_names.append(f"Surface{x+1}{y+1}")
# print(surface_names)

for name in surface_names:
    temp = surface()
    temp.set_pos(int(name[-2]), int(name[-1]))
    temp.set_color(255, 255, 255)
    surface_dict[name] = temp

running = True

print(surface_dict)

while running == True:

    # CHECKS IF USER CLICKED QUIT BUTTON
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for key in surface_dict:
        surface_dict[key].place()

    # surf_11.place

    # surf_11.set_color(255, 255, 255)
    pygame.display.flip()


pygame.quit()
