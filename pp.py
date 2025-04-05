from pygame import *

W = 500
H = 700 

window = display.set_mode((W, H))
display.set_caption('Пинг понг')
background = (24, 10, 92)
window.fill(background)

clock = time.Clock()
FPS = 120

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_up(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < W - 100:
            self.rect.x += self.speed
    def update_down(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < W - 100:
            self.rect.x += self.speed
        
racket1 = Player('Платформа.png', W//2, 10, 100, 25, 10)
racket2 = Player('Платформа.png', W//2, H - 35, 100, 25, 10)
ball = GameSprite('Мяч для пинг понга.jpg', W//2, H//2, 50, 50, 0)

speed_x = 5
speed_y = 5

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(background)
    
    ball.rect.y += speed_y
    ball.rect.x += speed_x

    racket1.update_up()
    racket2.update_down()

    racket1.reset()
    racket2.reset()
    ball.reset()

    if ball.rect.x > W-70 or ball.rect.x < 0:
        speed_y *= -1

    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1
        speed_y *= 1

    display.update()
    clock.tick(FPS)