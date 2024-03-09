from pygame import *

class Game(sprite.Sprite):
    def __init__(self,player_image, p_x, p_y, p_s):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(50,50))
        self.speed = p_s
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Move(Game):
    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
class Enemy (Game):
    d ="left"
    def move2(self):
        if self.rect.x<=470:
            self.d = "right"
        if self.rect.x >=620:
            self.d="left"

        if self.d=="left":
            self.rect.x -=self.speed
        else:
            self.rect.x+= self.speed
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x,wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1=color_1
        self.color_2=color_2
        self.color_3=color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x=wall_x
        self.rect.y= wall_y
    
    def draw_wall(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
    def hide(self):
        self.rect.x = -100
        self.rect.y = -100

        


window = display.set_mode((700,500))
display.set_caption("ЛАБІРИНТ")

bg = transform.scale(image.load("bg2.png"),(700,500))
bg2 = transform.scale(image.load("bg1.jpg"),(700,500))
player = Move("mouse.png",5,420,4)
enemy = Enemy("cat.jpg",620,280,2)
gold = Game("cheese.png",580,420,0)
w1= Wall(154,205,50,100,20,450,10)
w2= Wall(154,205,50,100,20,10,80)
w3 = Wall(154,205,50,100,100,300,10)
w4= Wall(154,205,50,400,100,10,80)
w5 = Wall(154,205,50,400,20,300,10)
w6= Wall(154,205,50,100,20,10,80)
w7 = Wall(154,205,50,100,20,300,10)

FPS = 60
clock = time.Clock()

game = True

font.init()
font = font.Font(None,70)
win = font.render("YOU WIN!", True, (255,215,0))
lose = font.render("GAME OVER", True, (180,0,0))



mixer.init()
mixer.music.load("hghgh.mp3")
mixer.music.play()
finish = False
a = 0
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(bg,(0,0))
        player.move()
        enemy.move2()
        player.reset()
        enemy.reset()
        gold.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()

        if sprite.collide_rect(player,enemy):
            finish = True
            window.blit(lose, (200,200))
        if sprite.collide_rect(player,gold):
            #finish = True
            #window.blit(win, (200,200))
            a = 1
        if a==1:
            window.blit(bg2,(0,0))
            player.reset()
            w1.hide()
            w2.hide()
            w3.hide()


        if sprite.collide_rect(player,w1)   or   sprite.collide_rect(player,w2):

            player.rect.x = 5
            player.rect.y = 420
            player.reset()

    display.update()
    clock.tick(FPS)