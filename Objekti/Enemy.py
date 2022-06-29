import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.x_change = 0
        self.score = 0

    def enemySpawn(self, i, x, x_change, y, img, screen):
        if i < 6:
            if x[i] <= -64 or x[i] >= 900:
                if i % 2 == 1:
                    x[i] = random.randint(-48, 0)
                    x_change[i] = abs(x_change[i])
                else:
                    x[i] = random.randint(834, 900)
                    x_change[i] = -abs(x_change[i])
                y[i] = random.randint(0, 500)
                self.score = 1

        elif 5 < i < 10:
            if x[i] <= -128 or x[i] >= 964:
                if i % 2 == 1:
                    x[i] = random.randint(-96, -48)
                    x_change[i] = abs(x_change[i])
                else:
                    x[i] = random.randint(870, 934)
                    x_change[i] = -abs(x_change[i])
                y[i] = random.randint(0, 500)
                self.score = 2

        elif 9 < i < 14:
            if x[i] <= -192 or x[i] >= 1028:
                if i % 2 == 1:
                    x[i] = random.randint(-192, -96)
                    x_change[i] = abs(x_change[i])
                else:
                    x[i] = random.randint(934, 1028)
                    x_change[i] = -abs(x_change[i])
                y[i] = random.randint(0, 450)
                self.score = 3
        elif i > 13:
            if x[i] <= -384 or x[i] >= 1100:
                if i % 2 == 1:
                    x[i] = random.randint(-384, -192)
                    x_change[i] = abs(x_change[i])
                else:
                    x[i] = random.randint(1028, 1100)
                    x_change[i] = -abs(x_change[i])
                y[i] = random.randint(0, 300)
        screen.blit(img[i], (x[i], y[i]))
        self.rect = img[i].get_rect(topleft = (x[i], y[i]))
        self.mask = pygame.mask.from_surface(img[i])

    def enemyRespawn(self, i, x, x_change, y, img, screen):
        if i < 6:
            if i % 2 == 1:
                x[i] = random.randint(-48, 0)
                x_change[i] = abs(x_change[i])
            else:
                x[i] = random.randint(834, 900)
                x_change[i] = -abs(x_change[i])
            y[i] = random.randint(0, 500)
            self.score = 1

        elif 5 < i < 10:
            if i % 2 == 1:
                x[i] = random.randint(-96, -48)
                x_change[i] = abs(x_change[i])
            else:
                x[i] = random.randint(870, 934)
                x_change[i] = -abs(x_change[i])
            y[i] = random.randint(0, 500)
            self.score = 2

        elif 9 < i < 14:
            if i % 2 == 1:
                x[i] = random.randint(-192, -96)
                x_change[i] = abs(x_change[i])
            else:
                x[i] = random.randint(934, 1028)
                x_change[i] = -abs(x_change[i])
            y[i] = random.randint(0, 450)
            self.score = 3

        elif i > 13:
            if i % 2 == 1:
                x[i] = random.randint(-384, -192)
                x_change[i] = abs(x_change[i])
            else:
                x[i] = random.randint(1028, 1100)
                x_change[i] = -abs(x_change[i])
            y[i] = random.randint(0, 300)
        screen.blit(img[i], (x[i], y[i]))
        self.rect = img[i].get_rect(topleft = (x[i], y[i]))
        self.mask = pygame.mask.from_surface(img[i])