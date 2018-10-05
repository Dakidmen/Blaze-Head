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

background = pygame.image.load('data/background.jpg').convert()
bgX = 0;
bgX2 = background.get_width();

clock = pygame.time.Clock()

#SOUND variables
bulletSound = pygame.mixer.Sound('data/hit.wav');
music = pygame.mixer.music.load('data/music.wav');
pygame.mixer.music.play(-1);

class player(object):
    #slide = [pygame.image.load(os.path.join('data', 'S1.png')),pygame.image.load(os.path.join('data', 'S2.png')),pygame.image.load(os.path.join('data', 'S2.png')),pygame.image.load(os.path.join('data', 'S2.png')), pygame.image.load(os.path.join('data', 'S2.png')),pygame.image.load(os.path.join('data', 'S2.png')), pygame.image.load(os.path.join('data', 'S2.png')), pygame.image.load(os.path.join('data', 'S2.png')), pygame.image.load(os.path.join('data', 'S3.png')), pygame.image.load(os.path.join('data', 'S4.png')), pygame.image.load(os.path.join('data', 'S5.png'))]
    jump = pygame.image.load('data/standing.png');
    jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]
    walkRight = [pygame.image.load('data/R1.png'),pygame.image.load('data/R2.png'),pygame.image.load('data/R3.png'),pygame.image.load('data/R4.png'),pygame.image.load('data/R5.png'),pygame.image.load('data/R6.png'),pygame.image.load('data/R7.png'),pygame.image.load('data/R8.png'),pygame.image.load('data/R9.png')];
    walkLeft = [pygame.image.load('data/L1.png'),pygame.image.load('data/L2.png'),pygame.image.load('data/L3.png'),pygame.image.load('data/L4.png'),pygame.image.load('data/L5.png'),pygame.image.load('data/L6.png'),pygame.image.load('data/L7.png'),pygame.image.load('data/L8.png'),pygame.image.load('data/L9.png')]
    char = pygame.image.load('data/Standing.png')

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

class projectile(object):
    '''Bullet'''
    bullet_right = pygame.image.load('data/bulletR.png')
    bullet_left = pygame.image.load('data/bulletL.png')

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

def redrawGame():
    ''' Draws the game '''
    window.blit(background, (bgX,0))
    window.blit(background, (bgX2,0))
    hero.draw(window);
    text = font.render("Score: 10",1,(255,255,255)) #missing score
    window.blit(text, (370,10));
    for bullet in bullets:
        bullet.draw(window);
    pygame.display.update();

#GAME variables
font = pygame.font.SysFont('comicsans',30,True);
hero = player(200,410,64,64);
bullets = [];
fps = 30
shootLoop = 0;
pygame.time.set_timer(USEREVENT+1,1000*60); #half second = 500
game = True;

while game:
    redrawGame();
    
    #BULLET COOLDOWN:
    if shootLoop > 0:
        shootLoop += 1;
    if shootLoop > 3:
        shootLoop = 0;

    #BULLETS:
    for bullet in bullets:
        '''
        if goblin.visible == True:
            #hitbox within x and y = collision
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    hitSound.play();
                    goblin.hit();
                    score += 1;
                    bullets.pop(bullets.index(bullet));
        '''
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet));
    #EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False;
            pygame.quit()
            quit()
    if event.type == USEREVENT+1:
        fps += 1

    #KEYS press
    keys = pygame.key.get_pressed();

    #shoot
    if keys[pygame.K_SPACE] and shootLoop == 0:
        bulletSound.play();
        if hero.left :
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5 :
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