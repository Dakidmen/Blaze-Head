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
    char = pygame.image.load('data/char/standing.png')

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
    def collision(self,what):
        if bullet.y - bullet.radius < what.hitbox[1] + what.hitbox[3] and bullet.y + bullet.radius > what.hitbox[1]:
                if bullet.x + bullet.radius > what.hitbox[0] and bullet.x - bullet.radius < what.hitbox[0] + what.hitbox[2]:
                    return True
        else:
            return False
            
class enemy(object):
    '''Goblin'''
    walkRight = [pygame.image.load('data/enemy/R1E.png'),pygame.image.load('data/enemy/R2E.png'),pygame.image.load('data/enemy/R3E.png'),pygame.image.load('data/enemy/R4E.png'),pygame.image.load('data/enemy/R5E.png'),pygame.image.load('data/enemy/R6E.png'),pygame.image.load('data/enemy/R7E.png'),pygame.image.load('data/enemy/R8E.png'),pygame.image.load('data/enemy/R9E.png'),pygame.image.load('data/enemy/R10E.png'),pygame.image.load('data/enemy/R11E.png')];
    walkLeft = [pygame.image.load('data/enemy/L1E.png'),pygame.image.load('data/enemy/L2E.png'),pygame.image.load('data/enemy/L3E.png'),pygame.image.load('data/enemy/L4E.png'),pygame.image.load('data/enemy/L5E.png'),pygame.image.load('data/enemy/L6E.png'),pygame.image.load('data/enemy/L7E.png'),pygame.image.load('data/enemy/L8E.png'),pygame.image.load('data/enemy/L9E.png'),pygame.image.load('data/enemy/L10E.png'),pygame.image.load('data/enemy/L11E.png')];
    
    def __init__(self, x, y, width, height, end,direction):
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
        self.direction = direction;

    def draw(self,win):
        self.move(self.direction)
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

    def move(self,direction):
        if self.direction == 'right':
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
        if self.direction == 'left':
            if self.vel < 0:
                if self.x + self.vel > self.path[1]:
                    self.x += self.vel;
                else:
                    self.vel = self.vel * -1;
                    self.walkCount = 0;
            else:
                if self.x + self.vel < self.path[0]:
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
        #pygame.draw.rect(window,(255,0,0), self.hitbox,2);
        #pygame.draw.rect(window,(255,0,0), self.hitbox,2);

    def collision(self,what):
        if what.hitbox[1] < self.hitbox[1] + self.hitbox[3] and what.hitbox[1] + what.hitbox[3] > self.hitbox[1]:
            if what.hitbox[0] + what.hitbox[2] > self.hitbox[0] and what.hitbox[0] < self.hitbox[0] + self.hitbox[2]:
                return True
        else:
            return False

def jumpFunction(keys):
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

class messages(object):
    #MESSAGES variables
    message01 = pygame.image.load('data/messages/01.png')
    def __init__(self,message,x,y,w,h):
        self.message = message
        self.x = x
        self.y = y
        self.w = w;
        self.h = h;
        self.text = ''

    def draw(self,window):
        if self.message == '01':
            window.blit(self.message01,(self.x,self.y));

class TetrisWheels(object):
    def __init__(self,form,x,y,w,h):
        self.form = form;
        self.x = x;
        self.y = y;
        self.w = w;
        self.h = h;
        self.visible = True;
        self.health = 5;

        if self.form == '1square':
            self.image = pygame.image.load('data/terrain/tetris/1square.png');
        elif self.form == '2squareVertical':
            self.image = pygame.image.load('data/terrain/tetris/2squareVertical.png');
        elif self.form == '2squareHorizontal':
            self.image = pygame.image.load('data/terrain/tetris/2squareHorizontal.png');
        elif self.form == '3L':
            self.image = pygame.image.load('data/terrain/tetris/3L.png');
        elif self.form == 'penis':
            self.image = pygame.image.load('data/terrain/tetris/penis.png');
        elif self.form == 'spaceship':
            self.image = pygame.image.load('data/terrain/tetris/spaceship.png');
        elif self.form == 'bigLVertical':
            self.image = pygame.image.load('data/images/tetris/bigLVertical.png');
        elif self.form == 'bigLHorizontal':
            self.image = pygame.image.load('data/images/tetris/bigLHorizontal.png');
        elif self.form == 'pistol':
            self.image = pygame.image.load('data/images/tetris/pistol.png');

    def draw(self,window):
        if self.visible == True:
            window.blit(self.image, (self.x,self.y));
            if self.form == '1square':
                self.hitbox = (self.x+60, 225, 70, 70);
            else:
                self.hitbox = (self.x+60, 225, 70, 70);
            #pygame.draw.rect(window,(255,0,0), self.hitbox,2);

    def collision(self,what):
        if what.hitbox[1] < self.hitbox[1] + self.hitbox[3] and what.hitbox[1] + what.hitbox[3] > self.hitbox[1]:
            if what.hitbox[0] + what.hitbox[2] > self.hitbox[0] and what.hitbox[0] < self.hitbox[0] + self.hitbox[2]:
                return True
        else:
            return False
    def hit(self,dmg):
        if self.health > 0:
            self.health -= dmg;
        else:
            self.visible = False;

def events(distance, what):
    if distance == 200:
        if what == 'blocks':
            return True;
    if distance == 20:
        if what == 'tetris':
            return True;
    if distance == 1000:
        if what == 'fps':
            return True;
    if distance == 500:
        if what == 'enemies':
            return True;
    if distance == 0:
        if what == 'space_use':
            return True;
    else:
        return False

def redrawGame():
    ''' Draws the game '''
    window.blit(background, (bgX,0))
    window.blit(background, (bgX2,0))
    hero.draw(window);
    text = font.render("Score: %s"%score,1,(255,255,255))
    window.blit(text, (370,10));
    if distance < 1000:
        counter = font.render(" %sm"%(distance),1,(255,255,255))
    else:
        counter = font.render(" %skm"%(distance/1000),1,(255,255,255))
    window.blit(counter, (0,10));
    for e in enemies:
        e.draw(window);
    for b in blocks:
        b.draw(window);
    for bullet in bullets:
        bullet.draw(window);
    for t in tetris:
        t.draw(window);
    #MESSAGES:
    for n in notes:
        n.draw(window)
    
    pygame.display.update();
    
    

#GAME variables
distance_unit = 'm'
distance = 0;
font = pygame.font.SysFont('comicsans',30,True);
bullets = [];
fps = 30
shootLoop = 0;
score = 0 
blocks = []
hero = player(200,410,64,64);
enemies = []
use_space = []
notes = []
tetris = [];

notes.append(messages('01',100,50,64,64))

game = True;
space_event = True;
while game:

    if distance >= 1000:
        distance_unit = 'km'
    redrawGame();

    #NOTES / MESSAGES:
    for m in notes:
        if hero.x > screen_w/2 and keys[pygame.K_RIGHT]:
            m.x -= 3.4
            if m.x < m.w *-1:
                notes.pop(notes.index(m));
    
    #BULLET COOLDOWN:
    if shootLoop > 0:
        shootLoop += 1;
    if shootLoop > 3:
        shootLoop = 0;

    #BULLETS:
    for bullet in bullets:
        for b in blocks:
            if bullet.collision(b) == True:
                hitSound.play();
                bullets.pop(bullets.index(bullet));
        #collision tetris bullet
        for t in tetris:
            #hitbox within x and y = collision
            if t.visible == True:
                if bullet.collision(t) == True:
                        hitSound.play();
                        t.hit(1)
                        score += 1;
                        bullets.pop(bullets.index(bullet));
        #collision enemies bullet
        for e in enemies:
            if e.visible == True:
                if bullet.collision(e) == True:
                        hitSound.play();
                        e.hit();
                        score += 1;
                        bullets.pop(bullets.index(bullet));

        if bullet.x < screen_w and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet));
            
    for b in blocks:
        if hero.x > screen_w/2 and keys[pygame.K_RIGHT]:
            b.x -= 1.4
            if b.x < b.w *-1:
                blocks.pop(blocks.index(b));
        #COLLISION blocks player
        if b.collision(hero):
            hero.collision(b.x,b.y,b.w,b.h)
            jumpFunction(keys)
    #Tetris:
    for t in tetris:
        if 0 <= t.x <= 20:
            t.x = 0;
            
        else:
            t.x -= 1.4
            if t.x < t.w *-1:
                tetris.pop(tetris.index(t));
        if t.collision(hero):
            hero.collision(t.x,t.y,t.w,t.h)
            t.hit(0.5);
            jumpFunction(keys)
    #COLLISION goblin player
    for e in enemies:
        if e.visible == True:
            #hitbox within x and y = collision
            if hero.hitbox[1] < e.hitbox[1] + e.hitbox[3] and hero.hitbox[1] + hero.hitbox[3] > e.hitbox[1]:
                if hero.hitbox[0] + hero.hitbox[2] > e.hitbox[0] and hero.hitbox[0] < e.hitbox[0] + e.hitbox[2]:
                    hero.hit();
                    score -= 5;

    #EVENTS quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False;
            pygame.quit()
            quit()
    #EVENTS fps increase
    if events(distance,'fps') == True:
        fps = 60

    #EVENTS block spawn
    if events(distance,'blocks') == True:
        blocks.append(terrain(screen_w-64,300,64,64))

    #EVENTS enemy spawn
    if events(distance,'enemies') == True:
        enemies.append(enemy(screen_w-64,410,64,64,190,'left'))
    #EVENTS tetris:
    if events(distance, 'tetris') == True:
        tetris.append(TetrisWheels('1square',screen_w-64,150,64,64))


    #EVENTS space
    if events(distance,use_space) == True:
        space_event = True;

    #KEYS press:
    keys = pygame.key.get_pressed();
    #space
    if space_event == True:
        if keys[pygame.K_SPACE] and shootLoop == 0:
            if hero.left :
                facing = -1
            else:
                facing = 1

            if len(bullets) < 3 :
                bulletSound.play();
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
            distance += 1;
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
    
    #up
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

    #END GAME:
    if distance == 2001:
        game = False;
