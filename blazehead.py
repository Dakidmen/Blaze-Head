import pygame;
from pygame.locals import *
import random;
import os;
pygame.init();

#SCREEN variables
screen_w = 800;
screen_h = 480;
window = pygame.display.set_mode((screen_w,screen_h)); #window size
pygame.display.set_caption("Blaze Head"); #game name

background = pygame.image.load('data/background/background1.jpg').convert()
bgX = 0;
bgX2 = background.get_width();

clock = pygame.time.Clock()

#SOUND variables
hitSound = pygame.mixer.Sound('data/sound/hit.wav');
bulletSound = pygame.mixer.Sound('data/sound/bullet.wav');
music = pygame.mixer.music.load('data/sound/music.wav');
pygame.mixer.music.play(-1);

class player(object):
    #slide = [pygame.image.load(os.path.join('data', 'S1.png')),pygame.image.load(os.path.join('data', 'S2.png')),pygame.image.load(os.path.join('data', 'S2.png')),pygame.image.load(os.path.join('data', 'S2.png')), pygame.image.load(os.path.join('data', 'S2.png')),pygame.image.load(os.path.join('data', 'S2.png')), pygame.image.load(os.path.join('data', 'S2.png')), pygame.image.load(os.path.join('data', 'S2.png')), pygame.image.load(os.path.join('data', 'S3.png')), pygame.image.load(os.path.join('data', 'S4.png')), pygame.image.load(os.path.join('data', 'S5.png'))]
    jump = pygame.image.load('data/char/standing.png');
    walkRight = [pygame.image.load('data/char/R1.png'),pygame.image.load('data/char/R2.png'),pygame.image.load('data/char/R3.png'),pygame.image.load('data/char/R4.png'),pygame.image.load('data/char/R5.png'),pygame.image.load('data/char/R6.png'),pygame.image.load('data/char/R7.png'),pygame.image.load('data/char/R8.png'),pygame.image.load('data/char/R9.png')];
    walkLeft = [pygame.image.load('data/char/L1.png'),pygame.image.load('data/char/L2.png'),pygame.image.load('data/char/L3.png'),pygame.image.load('data/char/L4.png'),pygame.image.load('data/char/L5.png'),pygame.image.load('data/char/L6.png'),pygame.image.load('data/char/L7.png'),pygame.image.load('data/char/L8.png'),pygame.image.load('data/char/L9.png')]
    char = pygame.image.load('data/char/Standing.png')

    def __init__(self, x, y, w, h):
        '''Hero'''
        self.x = x;
        self.y = y;
        self.w = w; #width
        self.h = h; #height

        self.vel = 5;
        self.isJump = False; #jumping
        self.isSlide = False; #sliding
        self.jumpCount = 10;
        self.runCount = 0;
        self.slideUp = 0;
        self.left = False;
        self.right = False;
        self.standing = True;
        self.move = True;

    def draw(self, window):
        if self.runCount + 1 >= 27:
            self.runCount = 0;
        if not (self.standing):
            if self.left:
                window.blit(self.walkLeft[self.runCount//3], (self.x,self.y))
                self.runCount += 1;
            elif self.right:
                window.blit(self.walkRight[self.runCount//3], (self.x,self.y))
                self.runCount +=1
        else:
            if self.right:
                window.blit(self.walkRight[0], (self.x,self.y));
            else:
                window.blit(self.walkLeft[0], (self.x,self.y));

        #pygame.draw.rect(window,(255,0,0), self.hitbox,2);
        self.hitbox = (self.x +17, self.y +11, 29, 52);

    def hit(self):
        self.isJump = False;
        self.jumpCount = 10;
        self.x = 60;
        self.y = 410;
        self.runCount = 0;
        font1 = pygame.font.SysFont('comicsans', 100);
        text = font1.render('-5',1,(255,0,0));
        window.blit(text, (250-(text.get_width()/2), 200));
        pygame.display.update();
        i = 0;
        while i < 200:
            pygame.time.delay(10);
            i += 1;
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201;
                    pygame.quit()

    def collision(self,tx,ty,tw,th):
        self.isJump = False;
        self.jumpCount = 10;

        if self.y > ty:
            self.y = 410;
        if not(tx-th/2< self.x < tx+th/2) :
            self.y = 410
        

        self.runCount = 0;
        pygame.display.update();

class projectile(object):
    '''Bullet'''
    bullet_right = pygame.image.load('data/bullet/bulletR.png')
    bullet_left = pygame.image.load('data/bullet/bulletL.png')

    def __init__(self,x,y,radius,color,facing):
        self.x = x;
        self.y = y;
        self.radius = radius;
        self.color = color;
        self.facing = facing;
        self.vel = 8 * facing;
    def draw(self,window):
        #pygame.draw.circle(window, self.color, (self.x, self.y), self.radius);
        if hero.left:
            window.blit(self.bullet_left, (self.x-50, self.y-25))
        else:
            window.blit(self.bullet_right, (self.x, self.y-25))

class enemy(object):
    '''Goblin'''
    walkRight = [pygame.image.load('data/enemy/R1E.png'),pygame.image.load('data/enemy/R2E.png'),pygame.image.load('data/enemy/R3E.png'),pygame.image.load('data/enemy/R4E.png'),pygame.image.load('data/enemy/R5E.png'),pygame.image.load('data/enemy/R6E.png'),pygame.image.load('data/enemy/R7E.png'),pygame.image.load('data/enemy/R8E.png'),pygame.image.load('data/enemy/R9E.png'),pygame.image.load('data/enemy/R10E.png'),pygame.image.load('data/enemy/R11E.png')];
    walkLeft = [pygame.image.load('data/enemy/L1E.png'),pygame.image.load('data/enemy/L2E.png'),pygame.image.load('data/enemy/L3E.png'),pygame.image.load('data/enemy/L4E.png'),pygame.image.load('data/enemy/L5E.png'),pygame.image.load('data/enemy/L6E.png'),pygame.image.load('data/enemy/L7E.png'),pygame.image.load('data/enemy/L8E.png'),pygame.image.load('data/enemy/L9E.png'),pygame.image.load('data/enemy/L10E.png'),pygame.image.load('data/enemy/L11E.png')];
    
    def __init__(self, x, y, width, height, end):
        self.x = x;
        self.y = y;
        self.width = width;
        self.height = height;
        self.end = end;
        self.path = [self.x,self.end]
        self.walkCount = 0;
        self.vel = 3;
        self.hitbox = (self.x +17, self.y +2, 31, 57);
        self.health = 10;
        self.visible = True;

    def draw(self,win):
        self.move()
        if self.visible == True:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0;

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1;
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1;
            
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1]-20, 50, 10));
            pygame.draw.rect(win, (0,255,0), (self.hitbox[0], self.hitbox[1]-20, 50-((50/10)*(10-self.health)), 10));
            self.hitbox = (self.x +17, self.y +2, 31, 57);
            #pygame.draw.rect(win,(255,0,0), self.hitbox,2);

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel;
            else:
                self.vel = self.vel * -1;
                self.walkCount = 0;
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1;
                self.walkCount = 0;
    def hit(self):
        if self.health > 0:
            self.health -= 1;
        else:
            self.visible = False;
        
class terrain(object):
    block = pygame.image.load('data/terrain/block1.png')

    def __init__(self,x,y,w,h):
        self.x = x;
        self.y = y;
        self.w = w;
        self.h = h;
    
    def draw(self,window):
        self.hitbox = (self.x + 8, self.y + 6, 50, 66);
        window.blit(self.block,(self.x,self.y));
        pygame.draw.rect(window,(255,0,0), self.hitbox,2);
        pygame.draw.rect(window,(255,0,0), self.hitbox,2);

    def collision(self,what):
        if what.hitbox[1] < self.hitbox[1] + self.hitbox[3] and what.hitbox[1] + what.hitbox[3] > self.hitbox[1]:
            if what.hitbox[0] + what.hitbox[2] > self.hitbox[0] and what.hitbox[0] < self.hitbox[0] + self.hitbox[2]:
                hitSound.play();
                return True
        else:
            return False
        
                

def redrawGame():
    ''' Draws the game '''
    window.blit(background, (bgX,0))
    window.blit(background, (bgX2,0))
    hero.draw(window);
    goblin.draw(window)
    platform.draw(window)
    text = font.render("Score: %s"%score,1,(255,255,255))
    window.blit(text, (370,10));
    for b in blocks:
        b.draw(window);
    for bullet in bullets:
        bullet.draw(window);
    pygame.display.update();

#GAME variables
font = pygame.font.SysFont('comicsans',30,True);
bullets = [];
fps = 30
shootLoop = 0;
score = 0
pygame.time.set_timer(USEREVENT+1,1000*60); #half second = 500
pygame.time.set_timer(USEREVENT+2,2000); 
blocks = []

hero = player(200,410,64,64);
goblin = enemy(400,410,64,64,600) #needs to add random event + coords
platform = terrain(300,300,64,64)


game = True;

while game:
    redrawGame();

    for b in blocks:
        if hero.x > screen_w/2:
            b.x -= 1.4
            if b.x < b.w *-1:
                blocks.pop(blocks.index(b));
        if b.collision(hero):
            hero.collision(b.x,b.y,b.w,b.h)

    #COLLISION platform player
    if hero.hitbox[1] < platform.hitbox[1] + platform.hitbox[3] and hero.hitbox[1] + hero.hitbox[3] > platform.hitbox[1]:
        if hero.hitbox[0] + hero.hitbox[2] > platform.hitbox[0] and hero.hitbox[0] < platform.hitbox[0] + platform.hitbox[2]:
            hero.collision(platform.x,platform.y,platform.w,platform.h)
    #COLLISION goblin player
    if goblin.visible == True:
        #hitbox within x and y = collision
        if hero.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and hero.hitbox[1] + hero.hitbox[3] > goblin.hitbox[1]:
            if hero.hitbox[0] + hero.hitbox[2] > goblin.hitbox[0] and hero.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                hero.hit();
                score -= 5;

    #BULLET COOLDOWN:
    if shootLoop > 0:
        shootLoop += 1;
    if shootLoop > 3:
        shootLoop = 0;

    #BULLETS:
    for bullet in bullets:
        #collision
        if goblin.visible == True:
            #hitbox within x and y = collision
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    hitSound.play();
                    goblin.hit();
                    score += 1;
                    bullets.pop(bullets.index(bullet));
        
        if bullet.x < screen_w and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet));
    #EVENTS +1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False;
            pygame.quit()
            quit()
    if event.type == USEREVENT+1:
        fps += 1
    #EVENTS +2
    if event.type == USEREVENT+2:
        blocks.append(terrain(100,300,64,64))

    #KEYS press
    keys = pygame.key.get_pressed();

    #shoot
    if keys[pygame.K_SPACE] and shootLoop == 0:
        bulletSound.play();
        if hero.left :
            facing = -1
        else:
            facing = 1

        if len(bullets) < 3 :
            bullets.append(projectile(round(hero.x + hero.w //2), round(hero.y+hero.h//2), 6, (0,94,255), facing))
        shootLoop = 1;
    
    #left
    if keys[pygame.K_LEFT] and hero.x > hero.vel:
        hero.left = True;
        hero.x -= hero.vel;
        hero.right = False;
        hero.standing = False;
    
    #right
    elif keys[pygame.K_RIGHT] and hero.x < screen_w - hero.w - hero.vel:
        hero.left = False;
        if hero.move == True:
            hero.x += hero.vel;
        hero.right = True;
        hero.standing = False;

        if hero.x > screen_w/2:
            hero.move = False;
            bgX -= 3.4
            bgX2 -= 3.4
            if bgX < background.get_width() * -1:
                bgX = background.get_width()
            if bgX2< background.get_width() * -1:
                bgX2 = background.get_width()
        else:
            hero.move = True;
    else:
        hero.standing = True;
        hero.runCount = 0
    
    #jump
    if not (hero.isJump):
        if keys[pygame.K_UP]:
            hero.isJump = True;
            hero.right = False;
            hero.left = False;
            hero.runCount = 0;
    else:
        if hero.jumpCount >= -10:
            neg = 1;
            if hero.jumpCount < 0:
                neg = -1
            hero.y -= (hero.jumpCount ** 2) * 0.5 * neg;
            hero.jumpCount -= 1;

        else:
            hero.isJump = False;
            hero.jumpCount = 10;

    #slide
    if keys[pygame.K_DOWN]:
        if not (hero.isSlide):
            hero.isSlide = True
    
    
    clock.tick(fps);
