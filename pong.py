import pygame
import random
import time
import math
from math import pi
while True:
    gamequit = False
    runcycles = 0
    opturn = True
    screenwidth = 700
    screenheight = 700
    pygame.init()
    win = pygame.display.set_mode((screenwidth, screenheight))
    pygame.display.set_caption("Pong")
    scorefont = pygame.font.SysFont("monospace", 75)
    winfont = pygame.font.SysFont("monospace", 130)

    px = 30
    pwin = False
    startpy = 350
    pscore = 0
    pwidth = 10
    pheight = 100
    pvel = 20
    py = (startpy+(startpy-pheight))/2

    ox = 660
    owin = False
    oscore = 0
    startoy = 350
    owidth = 10
    oheight = 100
    ovel = 20
    oy = (startoy+(startoy-oheight))/2
    oyorigin = (startoy+(startoy-oheight))/2
    oyodds = 25
    opchance = random.randint(1, oyodds)

    bwidth = 10
    bheight = 10
    bvel = 5
    bx = 350
    by = 30
    angle = random.randint(20, 80)
    neg = random.randint(0,1)
    if neg == 1:
        angle = -angle
        bvel = -bvel
    while angle == 0:
        pass
        


    def gradtorad(grad):
        return grad*pi/200


    if runcycles == 0:
        win.fill((255,255,255))
        sep = pygame.draw.rect(win, (255,0,0), (350,0,10,700))
        player = pygame.draw.rect(win, (0,0,0), (px,py,pwidth,pheight))
        ball = pygame.draw.rect(win, (0,0,255), (bx,by,bwidth,bheight))
        opponent = pygame.draw.rect(win, (0,0,0), (ox,oy,owidth,oheight))
        pscoregui = scorefont.render(str(pscore), 1, (0,0,0))
        win.blit(pscoregui, (175, 10))
        oscoregui = scorefont.render(str(oscore), 1, (0,0,0))
        win.blit(oscoregui, (475, 10))
        pygame.display.update()
        time.sleep(1)

    run = True
    while run == True:
        
        pygame.time.delay(25)
        win.fill((255,255,255))
        if pscore == 10 or pscore > 10:
            run = False
            pwin = True
        if oscore == 10 or oscore > 10:
            run = False
            owin = True
        pscoregui = scorefont.render(str(pscore), 1, (0,0,0))
        win.blit(pscoregui, (175, 10))
        oscoregui = scorefont.render(str(oscore), 1, (0,0,0))
        win.blit(oscoregui, (475, 10))
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False
                gamequit = True
        if keys[pygame.K_UP] and py >= pvel:
            py = py-pvel
        if keys[pygame.K_DOWN] and py < screenheight - pheight:
            py = py+pvel 

        by = by+(bvel*math.tan(gradtorad(angle)))
        bx = bx+bvel
        

        sep = pygame.draw.rect(win, (255,0,0), (350,0,10,700))
        player = pygame.draw.rect(win, (0,0,0), (px,py,pwidth,pheight))
        ball = pygame.draw.rect(win, (0,0,255), (bx,by,bwidth,bheight))
        opponent = pygame.draw.rect(win, (0,0,0), (ox,oy,owidth,oheight))

        if player.colliderect(ball):
            opturn = True
            angle = random.randint(20, 80)
            bvel = -bvel
            
        oycentre = (oy+(oy-oheight))/2
        
        if opponent.colliderect(ball):
            if opturn == True:
                opturn = False
                opchance = random.randint(1, oyodds)
                angle = random.randint(20, 80)
                bvel = -bvel

        if bx > ox+100:
            opturn = True
            opchance = random.randint(1, oyodds)
            bx = 350
            by = 30
            pscore = pscore+1
            print(pscore)
            angle = random.randint(20, 80)
                
        if bx < px-100:
            opturn = True
            opchance = random.randint(1, oyodds)
            bx = 350
            by = 30
            oscore = oscore+1
            print(oscore)
            angle = random.randint(20, 80)
            
            

        if by > screenheight - bheight:
            angle = -angle

        if by < 0:
            angle = -angle

        
        if opchance != 1:
            if bx > 350 and opturn == True:
                if (oy+oheight/2)-ovel > by:
                    oy = oy-ovel
                elif (oy-oheight/2)+ovel < by:
                    oy = oy+ovel
                else:
                    pass
            else:
                if oy-ovel > oyorigin:
                    oy = oy-ovel
                elif oy+ovel < oyorigin:
                    oy = oy+ovel
        else:
            if bx > 350 and opturn == True:
                choice = random.randint(0,1)
                if choice == 0:
                    oy = oy+ovel
                else:
                    oy = oy-ovel
            
            if oy-ovel > oyorigin:
                oy = oy-ovel
            elif oy+ovel < oyorigin:
                oy = oy+ovel
        
        pygame.display.update()
        runcycles = runcycles+1

    while owin == True:
        keys = pygame.key.get_pressed()
        win.fill((255,255,255))
        wingui = winfont.render("You Lose!", 1, (0,0,0))
        win.blit(wingui, (10, 250))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                owin = False
                gamequit = True
        if keys[pygame.K_RETURN]:
            oscore = 0
            run = True
            break

    while pwin == True:
        keys = pygame.key.get_pressed()
        win.fill((255,255,255))
        wingui = winfont.render("You Win!", 1, (0,0,0))
        win.blit(wingui, (40, 250))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pwin = False
                gamequit = True
        if keys[pygame.K_RETURN]:
            pscore = 0
            run = True
            break
        

    if gamequit == True:
        pygame.quit()
        break
