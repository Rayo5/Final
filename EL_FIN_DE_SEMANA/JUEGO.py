import pygame
import os
import random
import sys
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("musica.ogg")
# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('EL FIN DE SEMANA')

BG = pygame.image.load(os.path.join("Track.png"))

RUNNING = [pygame.image.load(os.path.join("DinoRun1.png")),
           pygame.image.load(os.path.join("DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join("DinoDuck1.png")),
           pygame.image.load(os.path.join("DinoDuck2.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("SmallCactus1.png")),
                pygame.image.load(os.path.join("SmallCactus2.png")),
                pygame.image.load(os.path.join("SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("LargeCactus1.png")),
                pygame.image.load(os.path.join("LargeCactus2.png")),
                pygame.image.load(os.path.join("LargeCactus3.png"))]

SMALL_CACTUS_2 = [pygame.image.load(os.path.join("Small1.png")),
                pygame.image.load(os.path.join("Small2.png")),
                pygame.image.load(os.path.join("Small3.png"))]
LARGE_CACTUS_2 = [pygame.image.load(os.path.join("Large1.png")),
                pygame.image.load(os.path.join("Large2.png")),
                pygame.image.load(os.path.join("Large3.png"))]

SMALL_CACTUS_3 = [pygame.image.load(os.path.join("S1.png")),
                pygame.image.load(os.path.join("S2.png")),
                pygame.image.load(os.path.join("S3.png"))]
LARGE_CACTUS_3 = [pygame.image.load(os.path.join("L1.png")),
                pygame.image.load(os.path.join("L2.png")),
                pygame.image.load(os.path.join("L3.png"))]

BIRD = [pygame.image.load(os.path.join("Bird1.png")),
        pygame.image.load(os.path.join("Bird2.png"))]

Paj = [pygame.image.load(os.path.join("Bird1.png")),
        pygame.image.load(os.path.join("Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("Cloud.png"))
Avion = pygame.image.load(os.path.join("Avion.png"))


FONDO = pygame.image.load(os.path.join("Fondo.png"))

fondo2 = pygame.image.load("Fondo_2.png")
fondo3 = pygame.image.load("Fondo_3_B.png")

ICONO = pygame.image.load("LOGO_JUEGO_B.jpg")

TWK = pygame.image.load("TWK_2.png")
TWK1 = pygame.image.load("LOGO_D.png")
TWK2 = pygame.image.load("infi.png")

pygame.display.set_icon(ICONO)
class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Cloud2:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = Avion
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    avion = Cloud2()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0
    pygame.mixer.music.play(1)

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        if points <= 1000:
            text = font.render("Puntos: " + str(points), True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (1000, 40)
            SCREEN.blit(text, textRect)
        elif points >= 1000:
            if points <= 2000:
                text = font.render("Puntos: " + str(points), True, (255, 0, 0))
                textRect = text.get_rect()
                textRect.center = (1000, 40)
                SCREEN.blit(text, textRect)
            elif points >= 2000:
                text = font.render("Puntos: " + str(points), True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (1000, 40)
                SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    def pausa2():
        pausado = True
        death_count = 0
        while pausado:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    salida()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        pausado = False
                    if event.key == pygame.K_d:
                        death_count += 1
                        menu(death_count)
            SCREEN.fill((255, 0, 0))
            font = pygame.font.Font('freesansbold.ttf', 30)
            text = font.render("Presiona A para ir al nivel 2 o Presiona D para terminar", True, (255, 255, 255))
            text_2 = font.render("¡FELICIDADES POR SUPERAR EL NIVEL 1!", True, (255, 255, 255))
            score = font.render("Puntaje obtenido: " + str(points), True, (255, 255, 255))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
            textRect = text.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            SCREEN.blit(text, textRect)
            text_2Rect = text_2.get_rect()
            text_2Rect.center= (550,118)
            SCREEN.blit(text_2,text_2Rect)
            SCREEN.blit(TWK, (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
            pygame.display.update()

    def pausa3():
        pausado = True
        death_count = 0
        while pausado:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    salida()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        pausado = False
                    if event.key == pygame.K_d:
                        death_count += 1
                        menu(death_count)
            SCREEN.fill((24, 4, 42))
            font = pygame.font.Font('freesansbold.ttf', 30)
            text = font.render("Presiona A para ir al nivel 3 o Presiona D para terminar", True, (255, 255, 255))
            text_2 = font.render("¡FELICIDADES POR SUPERAR EL NIVEL 2!", True, (255, 255, 255))
            score = font.render("Puntaje obtenido: " + str(points), True, (255, 255, 255))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
            textRect = text.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            SCREEN.blit(text, textRect)
            text_2Rect = text_2.get_rect()
            text_2Rect.center = (550, 118)
            SCREEN.blit(text_2, text_2Rect)
            SCREEN.blit(TWK2, (SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2 - 140))
            pygame.display.update()


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if points <= 1000:
            SCREEN.blit(FONDO, (0, 0))
        elif points >= 1000:
            if points <= 2000:
                SCREEN.blit(fondo2, (0, 0))
            elif points >= 2000:
                SCREEN.blit(fondo3, (0, 0))
        userInput = pygame.key.get_pressed()

        background()

        if points <= 1000:
            cloud.draw(SCREEN)
            cloud.update()
        elif points >= 1000:
            avion.draw(SCREEN)
            avion.update()

        player.draw(SCREEN)
        player.update(userInput)

        if points <= 1000:
            if len(obstacles) == 0:
                if random.randint(0, 2) == 0:
                    obstacles.append(SmallCactus(SMALL_CACTUS))
                elif random.randint(0, 2) == 1:
                    obstacles.append(LargeCactus(LARGE_CACTUS))
                elif random.randint(0, 2) == 2:
                    obstacles.append(Bird(BIRD))
        elif points >= 1000:
            if points <= 2000:
                if len(obstacles) == 0:
                    if random.randint(0, 2) == 0:
                        obstacles.append(SmallCactus(SMALL_CACTUS_2))
                    elif random.randint(0, 2) == 1:
                        obstacles.append(LargeCactus(LARGE_CACTUS_2))
                    elif random.randint(0, 2) == 2:
                        obstacles.append(Bird(Paj))
            elif points >= 2000:
                if len(obstacles) == 0:
                    if random.randint(0, 2) == 0:
                        obstacles.append(SmallCactus(SMALL_CACTUS_3))
                    elif random.randint(0, 2) == 1:
                        obstacles.append(LargeCactus(LARGE_CACTUS_3))
                    elif random.randint(0, 2) == 2:
                        obstacles.append(Bird(Paj))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                death_count += 1
                menu(death_count)

        if points <= 1000:
            text2 = font.render("Nivel 1", True, (0, 0, 0))
            textRect2 = text2.get_rect()
            textRect2.center = (100, 40)
            SCREEN.blit(text2, textRect2)
            text5 = font.render("El siguiente nivel se desbloqueará a los 1000pts", True, (0, 0, 0))
            textRect5 = text5.get_rect()
            textRect5.center = (550, 40)
            SCREEN.blit(text5, textRect5)
        elif points >= 1000:
            if points >= 2000:
                text4 = font.render("Nivel 3", True, (255, 255, 255))
                textRect4 = text4.get_rect()
                textRect4.center = (100, 40)
                SCREEN.blit(text4, textRect4)
                text7 = font.render("Este nivel es INFINITO ¡Logra tu mejor puntaje!", True, (255, 255, 255))
                textRect7 = text7.get_rect()
                textRect7.center = (550, 40)
                SCREEN.blit(text7, textRect7)
            elif points >= 1000:
                text3 = font.render("Nivel 2", True, (255, 0, 0))
                textRect3 = text3.get_rect()
                textRect3.center = (100, 40)
                SCREEN.blit(text3, textRect3)
                text6 = font.render("¡FELICIDADES! El siguiente nivel se desbloqueará a los 2000pts", True,(255, 255, 255))
                textRect6 = text6.get_rect()
                textRect6.center = (550, 40)
                SCREEN.blit(text6, textRect6)

        if points == 1000:
            pausa2()

        if points == 2000:
            pausa3()

        score()

        clock.tick(30)
        pygame.display.update()

def salida():
    pygame.quit()
    sys.exit()
def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Presiona cualquier tecla para iniciar el juego", True, (0, 0, 0))
            text1 = font.render("¡BIENVENIDO!", True, (0, 0, 0))
        elif death_count > 0:
            text1 = font.render("¡TE ESTAMPASTE!", True, (0, 0, 0))
            text = font.render("Presiona cualquier tecla para reiniciar", True, (0, 0, 0))
            score = font.render("Puntaje obtenido: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        textRect1 = text1.get_rect()
        textRect1.center = (550, 118)
        SCREEN.blit(text1, textRect1)
        SCREEN.blit(TWK1, (485, 300-167))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                salida()
            if event.type == pygame.KEYDOWN:
                main()

menu(death_count=0)

