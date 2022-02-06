import pygame
import random
import time

dimensiones = [700, 900]
fondo = pygame.image.load("FONDO.png")
Intro = pygame.image.load("Intro.png")
FLOWERNW = pygame.image.load("FLOWERNW1.png")
FLOWERNE = pygame.image.load("FLOWERNE1.png")
FLOWERSW =pygame.image.load("FLOWERSW1.png")
FLOWERSE =pygame.image.load("FLOWERSE1.png")
DUST00 =pygame.image.load("DUST00.png")
DUST10 =pygame.image.load("DUST10.png")
DUST30 =pygame.image.load("DUST30.png")
DUST40 =pygame.image.load("DUST40.png")
LDifficulty = ""
HDifficulty = 1000
Score = 0
NW = 1
NE = 1
SW = 1
SE = 1
PositionWormA = 1
PositionWormB = 1
PositionSpiderA = 1
PositionSpiderB = 1
PositionWormDelayA = 0
PositionWormDelayB = 0
PositionSpiderDelayA = 0
PositionSpiderDelayB = 0
GWX = 2
GWY = 3
A = ""
POSIBLESPOSICIONES = [(0,0),(1,0),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,3),(4,0)]
MISS = 0
PositionDustDelaySW = 0
NumberDustSW = []
PositionDustDelaySE = 0
NumberDustSE = []
Dust00 = 0
Dust10 = 0
Dust30 = 0
Dust40 = 0


def reset():
    global GWX
    global GWY
    global A
    global MRGW
    global MISS
    global PositionWormA
    global PositionWormB
    global PositionSpiderA
    global PositionSpiderB
    global Score
    global NW
    global NE
    global SW
    global SE
    global PositionWormDelayA
    global PositionWormDelayB
    global PositionSpiderDelayA
    global PositionSpiderDelayB
    global PositionDustDelaySW
    global NumberDustSW
    global PositionDustDelaySE
    global NumberDustSE
    global Dust00
    global Dust10
    global Dust30
    global Dust40
    global LDifficulty
    global HDifficulty
    global SCORE
    Score = 0
    NW = 1
    NE = 1
    SW = 1
    SE = 1
    PositionWormA = 1
    PositionWormB = 1
    PositionSpiderA = 1
    PositionSpiderB = 1
    PositionWormDelayA = 0
    PositionWormDelayB = 0
    PositionSpiderDelayA = 0
    PositionSpiderDelayB = 0
    GWX = 2
    GWY = 3
    A = ""
    MISS = 0
    PositionDustDelaySW = 0
    NumberDustSW = []
    PositionDustDelaySE = 0
    NumberDustSE = []
    Dust00 = 0
    Dust10 = 0
    Dust30 = 0
    Dust40 = 0
    LDifficulty = ""
    HDifficulty = 1000

 
def miss():
    global MISS
    global Score
    global LDifficulty
    LDifficultyOLD = LDifficulty 
    ScoreOLD = Score
    MISSOLD = MISS
    reset()
    MISS = MISSOLD
    MISS += 1
    Score = ScoreOLD
    LDifficulty = LDifficultyOLD
    MRGW = "MRGW"+str(GWX)+str(GWY)+A+".png"
    MRGW = pygame.image.load(MRGW)
    WORMA = "WORMA"+str(PositionWormA)+".png"
    WORMA = pygame.image.load(WORMA)
    WORMB = "WORMB"+str(PositionWormB)+".png"
    WORMB = pygame.image.load(WORMB)
    SPIDERA = "SPIDERA"+str(PositionSpiderA)+".png"
    SPIDERA = pygame.image.load(SPIDERA)
    SPIDERB = "SPIDERB"+str(PositionSpiderB)+".png"
    SPIDERB = pygame.image.load(SPIDERB)
    screen.blit(fondo, [0, 0])
    screen.blit(MRGW, [0, 0])
    screen.blit(FLOWERNW, [0, 0])
    screen.blit(FLOWERNE, [0, 0])    
    screen.blit(FLOWERSW, [0, 0])    
    screen.blit(FLOWERSE, [0, 0])
    screen.blit(SCORE, [50,395])
    for i in range (MISS):
        MISSES = "MISS"+str(i+1)+".png"
        MISSES = pygame.image.load(MISSES)    
        screen.blit(MISSES, [0, 0])
    screen.blit(WORMA, [0, 0])
    screen.blit(WORMB, [0, 0])
    screen.blit(SPIDERA, [0, 0])
    screen.blit(SPIDERB, [0, 0])
    pygame.display.flip()
    time.sleep(LDifficulty/4)

def Greenhouse():
    global GWX
    global GWY
    global A
    global MRGW
    global MISS
    global PositionWormA
    global PositionWormB
    global PositionSpiderA
    global PositionSpiderB
    global Score
    global NW
    global NE
    global SW
    global SE
    global PositionWormDelayA
    global PositionWormDelayB
    global PositionSpiderDelayA
    global PositionSpiderDelayB
    global PositionDustDelaySW
    global NumberDustSW
    global PositionDustDelaySE
    global NumberDustSE
    global Dust00
    global Dust10
    global Dust30
    global Dust40
    global HDifficulty
    global FLOWERNW
    global FLOWERNE
    global FLOWERSW
    global FLOWERSE
    global SCORE
    global hecho

    while not hecho:
        for evento in pygame.event.get():  
            if evento.type == pygame.QUIT: 
                hecho = True
            GWXOLD = GWX
            GWYOLD = GWY
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    GWX += 1
                if evento.key == pygame.K_LEFT:
                    GWX -= 1
                if evento.key == pygame.K_UP:
                    GWY -= 1
                if evento.key == pygame.K_DOWN:
                    GWY += 1
                if evento.key == pygame.K_a:
                    A = "a"
                #Baja volumen
                if evento.key == pygame.K_9 and pygame.mixer.music.get_volume() > 0.0:
                    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1)

                #Sube volumen
                if evento.key == pygame.K_0 and pygame.mixer.music.get_volume() < 1.0:
                    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)

                #Quitar volumen
                if evento.key == pygame.K_m:
                    pygame.mixer.music.set_volume(0.0)
                           
            if GWX == 2:
                A = ""
                
            if (GWX,GWY) == (1,3) and A == "a":
                NumberDustSW.append(5)

            if (GWX,GWY) == (3,3) and A == "a":
                NumberDustSE.append(5)

            if (GWX,GWY) == (0,0) and A == "a":
                Dust00 = 20
                
            if (GWX,GWY) == (1,0) and A == "a":
                Dust10 = 20
             
            if (GWX,GWY) == (3,0) and A == "a":
                Dust30 = 20
                
            if (GWX,GWY) == (4,0) and A == "a":
                Dust40 = 20            
         
                                    
            if not (GWX,GWY) in POSIBLESPOSICIONES:
                GWX = GWXOLD
                GWY = GWYOLD
                
        MRGW = "MRGW"+str(GWX)+str(GWY)+A+".png"
        MRGW = pygame.image.load(MRGW)

        #Logic
        #Logic
        #Logic
        if HDifficulty < 21:
            HDifficulty = 21
        if NW == 1:               
            if PositionWormDelayA > random.randrange(LDifficulty,HDifficulty):
                PositionWormDelayA = 0
                PositionWormA += 1
            if Dust00 > 0 and (PositionWormA == 5 or PositionWormA == 4):
                Score += 1
                HDifficulty -= 10
                PositionWormA = 1
                Squash.play(1)
                PositionWormDelayA = random.randrange(-20,0)
            if Dust10 > 0 and (PositionWormA == 3 or PositionWormA == 2):
                Score += 1
                HDifficulty -= 10
                PositionWormA = 1
                Squash.play(1)
                PositionWormDelayA = random.randrange(-20,0) 
            if PositionWormA > 5: 
                NW = 0
                FLOWERNW = "FLOWERNW"+str(NW)+".png"
                FLOWERNW = pygame.image.load(FLOWERNW)
                miss()
                NW = 1
                FLOWERNW = "FLOWERNW"+str(NW)+".png"
                FLOWERNW = pygame.image.load(FLOWERNW)            
            WORMA = "WORMA"+str(PositionWormA)+".png"
            WORMA = pygame.image.load(WORMA)
            PositionWormDelayA += 1

        if HDifficulty < 21:
            HDifficulty = 21
        if NE == 1:
            if PositionWormDelayB > random.randrange(LDifficulty,HDifficulty):
                PositionWormDelayB = 0
                PositionWormB += 1
            if Dust40 > 0 and (PositionWormB == 5 or PositionWormB == 4):
                Score += 1
                HDifficulty -= 10
                PositionWormB = 1
                Squash.play(1)
                PositionWormDelayB = random.randrange(-20,0)
            if Dust30 > 0 and (PositionWormB == 3 or PositionWormB == 2):
                Score += 1
                HDifficulty -= 10
                PositionWormB = 1
                Squash.play(1)
                PositionWormDelayB = random.randrange(-20,0)
            if PositionWormB > 5:
                NE = 0
                FLOWERNE = "FLOWERNE"+str(NE)+".png"
                FLOWERNE = pygame.image.load(FLOWERNE)
                miss()
                NE = 1
                FLOWERNE = "FLOWERNE"+str(NE)+".png"
                FLOWERNE = pygame.image.load(FLOWERNE)
            WORMB = "WORMB"+str(PositionWormB)+".png"
            WORMB = pygame.image.load(WORMB)
            PositionWormDelayB += 1

        if PositionDustDelaySW > 20:
            PositionDustDelaySW = 0
            for i in range (len(NumberDustSW)):
                NumberDustSW[i] -= 1
            for i in range (NumberDustSW.count(0)):
                NumberDustSW.remove(0)
        if len(NumberDustSW) > 0:
            PositionDustDelaySW += 1
              
        if PositionDustDelaySE > 20:
            PositionDustDelaySE = 0
            for i in range (len(NumberDustSE)):
                NumberDustSE[i] -= 1
            for i in range (NumberDustSE.count(0)):
                NumberDustSE.remove(0)
        if len(NumberDustSE) > 0:
            PositionDustDelaySE += 1

        if Dust00 > 0:
            Dust00 -= 1
                    
        if Dust10 > 0:
            Dust10 -= 1
            
        if Dust30 > 0:
            Dust30 -= 1
            
        if Dust40 > 0:
            Dust40 -= 1

        if HDifficulty < 21:
            HDifficulty = 21
        if SW == 1:
            if PositionSpiderDelayA > random.randrange(LDifficulty,HDifficulty):
                PositionSpiderDelayA = 0
                PositionSpiderA += 1
            if PositionSpiderA in NumberDustSW:
                if PositionSpiderA == 1:
                    PositionSpiderDelayA = 0
                elif PositionSpiderA == 5:
                    Squash.play(1)
                    Score += 3
                    HDifficulty -= 30
                    for i in range (NumberDustSW.count(PositionSpiderA)):
                        NumberDustSW.remove(PositionSpiderA)
                    PositionSpiderA = 1
                else:
                    Score += 1
                    HDifficulty -= 10
                    for i in range (NumberDustSW.count(PositionSpiderA)):
                        NumberDustSW.remove(PositionSpiderA)
                    PositionSpiderA -= 1
                PositionSpiderDelayA = 0  
            if PositionSpiderA > 5:     
                SW = 0
                FLOWERSW = "FLOWERSW"+str(SW)+".png"
                FLOWERSW = pygame.image.load(FLOWERSW)
                miss()
                SW = 1
                FLOWERSW = "FLOWERSW"+str(SW)+".png"
                FLOWERSW = pygame.image.load(FLOWERSW)
            SPIDERA = "SPIDERA"+str(PositionSpiderA)+".png"
            SPIDERA = pygame.image.load(SPIDERA)
            PositionSpiderDelayA += 1
            
        if HDifficulty < 21:
            HDifficulty = 21
        if SE == 1:
            if PositionSpiderDelayB > random.randrange(LDifficulty,HDifficulty):
                PositionSpiderDelayB = 0
                PositionSpiderB += 1
            if PositionSpiderB in NumberDustSE:
                if PositionSpiderB == 1:
                    PositionSpiderDelayB = 0
                elif PositionSpiderB == 5:
                    Squash.play(1)
                    Score += 3
                    HDifficulty -= 30
                    for i in range (NumberDustSE.count(PositionSpiderB)):
                        NumberDustSE.remove(PositionSpiderB)
                    PositionSpiderB = 1
                else:
                    Score += 1
                    HDifficulty -= 10
                    for i in range (NumberDustSE.count(PositionSpiderB)):
                        NumberDustSE.remove(PositionSpiderB)
                    PositionSpiderB -= 1
                PositionSpiderDelayB = 0
            if PositionSpiderB > 5:
                SE = 0
                FLOWERSE = "FLOWERSE"+str(SE)+".png"
                FLOWERSE = pygame.image.load(FLOWERSE)
                miss()
                SE= 1
                FLOWERSE = "FLOWERSE"+str(SE)+".png"
                FLOWERSE = pygame.image.load(FLOWERSE)              
            SPIDERB = "SPIDERB"+str(PositionSpiderB)+".png"
            SPIDERB = pygame.image.load(SPIDERB)
            PositionSpiderDelayB += 1

        SCORE = myfont.render(str(Score), False, (0, 0, 0))
        
        if MISS == 3:
            print("Game Over")
            break

        #DIBUJAR
        #DIBUJAR
        #DIBUJAR

        screen.blit(fondo, [0, 0])
        screen.blit(MRGW, [0, 0])
        screen.blit(FLOWERNW, [0, 0])
        screen.blit(FLOWERNE, [0, 0])    
        screen.blit(FLOWERSW, [0, 0])    
        screen.blit(FLOWERSE, [0, 0])
        screen.blit(SCORE, [50,395])
    
        if NW == 1:
            screen.blit(WORMA, [0, 0])
        if NE == 1:
            screen.blit(WORMB, [0, 0])
        if SW == 1:
            screen.blit(SPIDERA, [0, 0])
        if SE == 1:
            screen.blit(SPIDERB, [0, 0])
     
        for i in range (len(NumberDustSW)):
            DUSTSW = "DUSTSW"+str(NumberDustSW[i])+".png"
            DUSTSW = pygame.image.load(DUSTSW)
            screen.blit(DUSTSW, [0, 0])

        for i in range (len(NumberDustSE)):
            DUSTSE = "DUSTSE"+str(NumberDustSE[i])+".png"
            DUSTSE = pygame.image.load(DUSTSE)
            screen.blit(DUSTSE, [0, 0])
        
        for i in range (MISS):
            MISSES = "MISS"+str(i+1)+".png"
            MISSES = pygame.image.load(MISSES)    
            screen.blit(MISSES, [0, 0])

        if Dust00 > 0:
            screen.blit(DUST00, [0, 0])
            
        if Dust10 > 0:
            screen.blit(DUST10, [0, 0])
            
        if Dust30 > 0:
            screen.blit(DUST30, [0, 0])
            
        if Dust40 > 0:
            screen.blit(DUST40, [0, 0])

        pygame.display.flip()
        reloj.tick(20)

def intro():
    global hecho
    global LDifficulty
    x = 0
    while not hecho and x == 0:
        for evento in pygame.event.get():  
            if evento.type == pygame.QUIT: 
                hecho = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if LDifficulty.isdigit() and int(LDifficulty) < 21:
                        LDifficulty = int(LDifficulty)
                        x = 1
                    else:
                        LDifficulty = ""
                elif evento.type == pygame.KEYDOWN:
                    LDifficulty += evento.unicode
        screen.blit(Intro, [0, 0])
        LDIFFICULTY = myfont.render(str(LDifficulty), False, (0, 150, 0))
        screen.blit(LDIFFICULTY, [200,675])
        pygame.display.flip()
        reloj.tick(10)


pygame.init()
myfont = pygame.font.SysFont('Arial', 50)
SCORE = myfont.render(str(Score), False, (0, 0, 0))
screen = pygame.display.set_mode(dimensiones)
reloj = pygame.time.Clock()
Squash = pygame.mixer.Sound('Squash.wav')
pygame.mixer.music.load('Super Smash Bros Brawl  Flat Zone 2 SNES Remix.mp3')

hecho = False
while not hecho:
    reset()
    intro()
    pygame.mixer.music.play()
    Greenhouse()
    pygame.mixer.music.rewind()
    pygame.mixer.music.stop()
             
pygame.quit ()
