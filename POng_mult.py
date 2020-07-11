import pygame,sys,random,time

def ball_animation():
    global ball_speed_x,ball_speed_y,cond_1,cond_1
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <=0 or ball.bottom >= screen_height:
        ball_speed_y*=-1
    if ball.left <=0 or ball.right >= screen_width:
        ball_speed_x*=-1
     
    
    if ball.colliderect(player):
        ball_speed_x *= -1
        cond_1 = pygame.time.get_ticks()
    if ball.colliderect(opponent):
        ball_speed_x *= -1
    if ball.colliderect(pad):
        ball_speed_x *= -1    
    if ball.left <=0 or ball.right>= screen_width:
        reset()
        cond_1 = None
    
def player_animation():
    
    if player.top <=0:
        player.top = 0
    
    if player.bottom>= screen_height:
        player.bottom = screen_height
    

def opponent_animation():
    global opponent_speed

    if opponent.top <=0:
        opponent.top = 0
    
    if opponent.bottom>= screen_height:
        opponent.bottom = screen_height

    if ball2.left > ball.left:
        if opponent.top <= ball.top:
            opponent.y += opponent_speed
        
        if opponent.bottom >= ball.bottom:
            opponent.y -= opponent_speed
    if ball.left > ball2.left:
        if opponent.top <= ball2.top:
            opponent.y += opponent_speed
        
        if opponent.bottom >= ball2.bottom:
            opponent.y -= opponent_speed


def pad1():
    global pad_speed
    if pad.top <= 0:
        pad_speed *= -1
        pad.y += pad_speed
    if pad.bottom >= screen_height:
        pad_speed *= -1
        pad.y += pad_speed
    pad.y += pad_speed

def reset():
    global ball_speed_x,ball_speed_y,ball2_speed_x,ball2_speed_y
    time.sleep(1.0)
    ball.center = (screen_width/2,screen_height/2)
    ball2.center = (screen_width/2,screen_height/2)
    ball_speed_x *= random.choice((1,-1))
    ball_speed_y *= random.choice((1,-1))
    ball2_speed_x *= random.choice((1,-1))
    ball2_speed_y *= random.choice((1,-1))


def ball_2():
    global ball2,ball2_speed_x,ball2_speed_y,ball_speed_x,cond_1
    current_time = pygame.time.get_ticks()
    if cond_1:
        if current_time > 9000:
            pygame.draw.ellipse(screen,white,ball2)
            ball2.x += ball2_speed_x
            ball2.y += ball2_speed_y
        
        if ball2.top <= 0 or ball2.bottom >= screen_height:
            ball2_speed_y *= -1
        if ball2.left <= 0 or ball2.right >= screen_width:
            reset()
            cond_1 = None
        if ball2.colliderect(player):
            ball2_speed_x *= -1
        if ball2.colliderect(opponent):
            ball2_speed_x *= -1 
        if ball2.colliderect(pad):
            ball2_speed_x *= -1       
        if ball2.colliderect(ball):
            ball2_speed_x *= -1
            ball_speed_x *= -1

    

pygame.init()
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
ball = pygame.Rect(screen_width/2 - 15,screen_height/2 -15,30,30)
ball2 = pygame.Rect(screen_width/2 - 15,screen_height/2 -15,30,30)
player = pygame.Rect(screen_width-10,screen_height/2- 70,10,140)
opponent = pygame.Rect(0,screen_height/2- 70,10,140)
pad = pygame.Rect(screen_width/2-5,40,10,140)
pygame.display.set_caption('POng')
bg_color = pygame.Color("grey12")
white = (200,200,200)
ball_speed_x = 8
ball_speed_y = 5
player_speed = 0
opponent_speed = 20
pad_speed = 5
ball2_speed_x = 9
ball2_speed_y = 8
cond_1 = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 20
            if event.key == pygame.K_DOWN:
                player_speed-= 20
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 20
            if event.key == pygame.K_UP:
                player_speed-= 20



    screen.fill(bg_color)
    pygame.draw.rect(screen,white,player)
    pygame.draw.rect(screen,white,opponent)
    pygame.draw.ellipse(screen,white,ball)
    pygame.draw.aaline(screen,white,(screen_width/2,0),(screen_width/2,screen_height))
    pygame.draw.rect(screen,white,pad)
    player.y +=player_speed
    
    ball_animation()
    ball_2()
    player_animation()
    opponent_animation()
    pad1()
    pygame.display.flip()
    clock.tick(60)