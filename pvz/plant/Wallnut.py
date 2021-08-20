import pygame


class Wallnut(pygame.sprite.Sprite):
    def __init__(self, rect):

        super(Wallnut, self).__init__()
        self.image = pygame.image.load("..\pvz\png\Wallnut\Wallnut00.png").convert_alpha()
        self.images = [pygame.image.load("..\pvz\png\Wallnut\Wallnut{:02d}.png".format(i)).convert_alpha() for i in
                       range(0, 17)]
        self.Imgs2 = [pygame.image.load("..\pvz\png\Wallnut\Wallnut2_{:02d}.png".format(i)).convert_alpha() for i in
                      range(0, 17)]
        self.Imgs3 = [pygame.image.load("..\pvz\png\Wallnut\Wallnut3_{:02d}.png".format(i)).convert_alpha() for i in
                      range(0, 17)]
        self.rect = self.images[0].get_rect()
        self.rect.left = rect[0]
        self.rect.top = rect[1]
        self.energy = 333
        self.zombies = set()

    def update(self, *args):
        for zombie in self.zombies:
            if not zombie.Alive:
                self.energy += 0
            else:
                self.energy -= 1
        if self.energy <= 0:
            for zombie in self.zombies:
                zombie.GOGO = False
            self.kill()
        elif self.energy >= 222:
            self.image = self.images[args[0] % len(self.images)]
        elif 111 <= self.energy < 222:
            self.image = self.Imgs2[args[0] % len(self.Imgs2)]
        else:
            self.image = self.Imgs3[args[0] % len(self.Imgs3)]
