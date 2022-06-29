import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 420
        self.y = 270
        self.x_change = 0
        self.y_change = 0
        self.direction = 0
        self.lastKey = 'l'
        self.score = 0
        self.height = 128
        self.width = 128
        self.slow = 0
        self.keyInput = True

    def drawImg(self, x, y, img, screen):
        screen.blit(img, (x, y))

    def setDimenzije(self, img):
        self.height = img.get_height()
        self.width = img.get_width()

    def playerMovement(self, img, screen):
        # Provera u koju stranu ide
        pressed = pygame.key.get_pressed()
        if self.keyInput:
            if pressed[pygame.K_LEFT]:
                self.x_change = -1.5 + self.slow
                self.direction = -1
            if pressed[pygame.K_RIGHT]:
                self.x_change = +1.5 - self.slow
                self.direction = 1
            if pressed[pygame.K_LEFT] and pressed[pygame.K_RIGHT]:
                self.x_change = 0
            if not (pressed[pygame.K_LEFT] or pressed[pygame.K_RIGHT]):
                self.x_change = 0
            if pressed[pygame.K_UP]:
                self.y_change = -1.5
            if pressed[pygame.K_DOWN]:
                self.y_change = +1.5
            if pressed[pygame.K_UP] and pressed[pygame.K_DOWN]:
                self.y_change = 0
            if not (pressed[pygame.K_UP] or pressed[pygame.K_DOWN]):
                self.y_change = 0

        self.x += self.x_change
        self.y += self.y_change

        if self.direction == 1 or self.lastKey == 'r':
            img_flip = pygame.transform.flip(img, True, False)
            if self.score < 16:
                img = pygame.transform.scale(img_flip, (32, 32))
                self.setDimenzije(img)
                self.drawImg(self.x, self.y, img, screen)
            if 15 < self.score < 50:
                self.slow = 0.3
                img = pygame.transform.scale(img_flip, (64, 64))
                self.setDimenzije(img)
                self.drawImg(self.x, self.y, img, screen)
            elif self.score > 49:
                self.size = 3
                self.slow = 0.5
                self.setDimenzije(img_flip)
                self.drawImg(self.x, self.y, img_flip, screen)
        elif self.lastKey == 'l':
            if self.score < 16:
                img = pygame.transform.scale(img, (32, 32))
                self.setDimenzije(img)
                self.drawImg(self.x, self.y, img, screen)
            if 15 < self.score < 50:
                self.size = 2
                self.slow = 0.2
                img = pygame.transform.scale(img, (64, 64))
                self.setDimenzije(img)
                self.drawImg(self.x, self.y, img, screen)
            elif self.score > 49:
                self.size = 3
                self.slow = 0.4
                self.setDimenzije(img)
                self.drawImg(self.x, self.y, img, screen)
        if self.x <= -60:
            self.x = 900
        elif self.x >= 900:
            self.x = -60
        if self.y >= 534:
            self.y = 534
        if self.y <= 0:
            self.y = 0
        self.rect = img.get_rect(topleft = (self.x, self.y))
        self.mask = pygame.mask.from_surface(img)