from pygame import *

class Gamer(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class player(Gamer):
    def control_1(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= step
        if key_pressed[K_s] and self.rect.y < 620:
            self.rect.y += step
    def control_2(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= step
        if key_pressed[K_DOWN] and self.rect.y < 620:
            self.rect.y += step


clock = time.Clock()
window = display.set_mode((700, 500))
display.set_caption('become a skibidi toilet')
font.init()
font = font.Font(None,43)
background = transform.scale(image.load("Без названия.jpg"), (700, 500))

x1 = 100
y1 = 300
x2 = 500
y2 = 300

game = True
clock = time.Clock()
step = 7
player1 = player('Без названия.png',30,200,10,100,15)
player2 = player('Без названия.png',640,200,10,100,15)
ball = player('pngimg.com - football_PNG52792.png',200,200,50,50,0)
lose1 = font.render('Проиграл 1-ый игрок',True,(255,255,255))
lose2 = font.render('Проиграл 2-ый игрок',True,(255,255,255))
ball_x = 3
ball_y = 3
finish = False
fps = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0,0))
        player1.reset()
        player1.control_1()
        player2.reset()
        player2.control_2()
        ball.reset()
        ball.rect.x += ball_x
        ball.rect.y -= ball_y
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            ball_x *= -1
            ball_y *= 1
        if ball.rect.y < 0 or ball.rect.y > 450:
            ball_y *= -1
        if ball.rect.x < -40:
            finish = True
            window.blit(lose1,(100,200))
        if ball.rect.x > 650:
            finish = True
            window.blit(lose2,(100,200))
        display.update()
    clock.tick(60)
