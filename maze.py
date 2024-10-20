from pygame import *
'''Kelas wajib'''


#kelas induk untuk sprite
class GameSprite(sprite.Sprite):
    #konstruktor kelas
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        # setiap sprite harus menyimpan properti image - gambar
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        # setiap sprite harus menyimpan properti rect - persegi panjang di mana sprite tersebut dituliskan
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#kelas penerus untuk sprite pemain (dikontrol oleh panah)
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


#kelas penerus untuk sprite musuh (bergerak sendiri)
class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"


        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_widht,wall_height):
        self.color_1 = color_1
        self.color_2 =color_2
        self.color_3 = color_3
        self.widht = wall_widht
        self.height = wall_height
        self.image = Surface([self.widht, self.height])
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.widht, self.height))
w1 = wall(154, 205, 50,100,20,450,10)
w2 = wall(154,205,50,100,480,350,10)
w3 = wall(154,205,50,100,20,10,380)
w4 = wall(154,205,50,200,130,10,350)
w5 = wall(154,205,50,450,130,10,360)
w6 = wall(154,205,50,300,20,10,350)
w7 = wall(154,205,50,390,120,130,10)
#Adegan permainan:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))


#Karakter permainan:
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)


game = True
finish = False
clock = time.Clock()
FPS = 60


#musik
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        monster.update()
        
        player.reset()
        monster.reset()
        final.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()



    display.update()
    clock.tick(FPS)