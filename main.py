import pygame
import random
from Objekti.Player import Player
from Objekti.Enemy import Enemy
from pygame import mixer


def showScore(x, y, font, screen, scoreValue):
    score = font.render("Score: " + str(scoreValue), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text(screen, font):
    over_text1 = font.render("GAME OVER", True, (255, 255, 255))
    over_text2 = font.render("Press Enter to restart", True, (255, 255, 255))
    over_text3 = font.render("Backspace to exit", True, (255, 255, 255))
    screen.blit(over_text1, (290, 220))
    screen.blit(over_text2, (190, 270))
    screen.blit(over_text3, (230, 320))


enemyImg = []

player = Player()
enemy = Enemy()
enemySprite = pygame.sprite.Group()

def main():
    # Inicijalizacija
    pygame.init()

    clock = pygame.time.Clock()

    num_of_enemies = 16

    font = pygame.font.Font('freesansbold.ttf', 32)
    over_font = pygame.font.Font('freesansbold.ttf', 48)

    # kreiram ekran
    screen = pygame.display.set_mode((900, 600))

    # Pozadina
    pozadina = pygame.image.load("Slike/pozadina.png")

    #Pozadinska muzika
    mixer.music.load('Audio/FastFeelBananaPeel-320bit.mp3')
    mixer.music.play(-1)

    # Naslov i ikona
    pygame.display.set_caption("Slike/Gladna ajkula")
    icon = pygame.image.load("Slike/sharkIcon.png")
    pygame.display.set_icon(icon)

    enemyImg0 = pygame.image.load("Slike/fish1smol-left.png").convert_alpha()
    enemyImg1 = pygame.image.load("Slike/fish1smol-right.png").convert_alpha()

    enemyImg2 = pygame.image.load("Slike/fish2smol-left.png").convert_alpha()
    enemyImg3 = pygame.image.load("Slike/fish2smol-right.png").convert_alpha()

    enemyImg4 = pygame.image.load("Slike/fish3smol-left.png").convert_alpha()
    enemyImg5 = pygame.image.load("Slike/fish3smol-right.png").convert_alpha()

    enemyImg6 = pygame.image.load("Slike/fish1med-left.png").convert_alpha()
    enemyImg7 = pygame.image.load("Slike/fish1med-right.png").convert_alpha()

    enemyImg8 = pygame.image.load("Slike/fish3med-left.png").convert_alpha()
    enemyImg9 = pygame.image.load("Slike/fish3med-right.png").convert_alpha()

    enemyImg10 = pygame.image.load("Slike/enemy-shark-left.png").convert_alpha()
    enemyImg11 = pygame.image.load("Slike/enemy-shark-right.png").convert_alpha()

    enemyImg12 = pygame.image.load("Slike/enemy2-shark-left.png").convert_alpha()
    enemyImg13 = pygame.image.load("Slike/enemy2-shark-right.png").convert_alpha()

    enemyImg14 = pygame.image.load("Slike/orca-left.png").convert_alpha()
    enemyImg15 = pygame.image.load("Slike/orca-right.png").convert_alpha()

    enemyImg = [enemyImg0, enemyImg1, enemyImg2, enemyImg3, enemyImg4, enemyImg5, enemyImg6, enemyImg7, enemyImg8,
                enemyImg9, enemyImg10, enemyImg11, enemyImg12, enemyImg13, enemyImg14, enemyImg15]

    # Igrac
    playerImgLevo1 = pygame.image.load("Slike/SharkScaleLeft.png").convert_alpha()

    player.keyInput = True
    player.score = 0

    enemyList = []
    enemyX = []
    enemyY = []
    enemyX_change = []

    for i in range(num_of_enemies):
        if i % 2 == 1:
            enemyX.append(random.randint(-64, 0))
            if i < 6:
                enemyX_change.append(1.7)
            elif 5 < i < 10:
                enemyX_change.append(1.5)
            elif 9 < i < 14:
                enemyX_change.append(1.3)
            elif i > 13:
                enemyX_change.append(1.1)
        else:
            enemyX.append(random.randint(850, 900))
            if i < 6:
                enemyX_change.append(-1.7)
            elif 5 < i < 10:
                enemyX_change.append(-1.5)
            elif 9 < i < 14:
                enemyX_change.append(-1.3)
            elif i > 13:
                enemyX_change.append(-1.1)
        enemyY.append(random.randint(0, 500))
        enemyList.append(enemy)

    running = True
    while running:
        clock.tick(60)
        # Pozadina
        screen.blit(pozadina, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.playerMovement(playerImgLevo1, screen)

        # Enemy
        for i in range(num_of_enemies):
            enemyX[i] += enemyX_change[i]
            enemy.enemySpawn(i, enemyX, enemyX_change, enemyY, enemyImg, screen)
            enemySprite.add(enemy)


            mob_hits = pygame.sprite.spritecollide(player, enemySprite, False, pygame.sprite.collide_mask)
            if mob_hits:
                if player.width >= enemyImg[i].get_width():
                    if random.randint(1,2) == 1:
                        biteSound = mixer.Sound('Audio/Bite1.mp3')
                    else:
                        biteSound = mixer.Sound('Audio/Bite2.mp3')
                    biteSound.play()
                    enemy.enemyRespawn(i, enemyX, enemyX_change, enemyY, enemyImg, screen)
                    player.score += enemy.score
                else:
                    for j in range(num_of_enemies):
                        enemyX_change[j] = 0
                    player.keyInput = False
                    mixer.music.stop()
                    player.x_change = 0
                    player.y_change = 0
                    enemy.speed = 0
                    game_over_text(screen, over_font)
                    pressed = pygame.key.get_pressed()
                    if pressed[pygame.K_BACKSPACE]:
                        running = False
                    elif pressed[pygame.K_RETURN]:
                        main()

        showScore(10, 10, font, screen, player.score)
        pygame.display.update()


if __name__ == "__main__":
    main()

# Fast Feel Banana Peel by Alexander Nakarada | https://www.serpentsoundstudios.com
# Music promoted on https://www.chosic.com/free-music/all/
# Creative Commons Attribution 4.0 International (CC BY 4.0)
# https://creativecommons.org/licenses/by/4.0/



