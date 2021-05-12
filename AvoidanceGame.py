######################################
# Opening Comments
# Author: Nathaniel Edwards
# 3/26/21
# Avoidance Game
#######################################
import time

import pygame
import random
import sqlite3
from sqlite3 import Error
import GameLogon as GL

highScore = 0
enemyKilled = 0
potionCollected = 0
redPotionCollected = 0
bluePotionCollected = 0
yellowPotionCollected = 0
greenPotionCollected = 0
purplePotionCollected = 0

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    K_SPACE,
    QUIT,
    K_w,
    K_a,
    K_s,
    K_d
    )

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
EnemySpawnSpeed = 2000
RED = 135
BLUE = 205
GREEN = 250
Score = 0
GameOver = True

class Player(pygame.sprite.Sprite):
    walkCount = 0
    moving = False
    IsMovable = True
    IdleCount = 0
    AttackCount = 0
    Speed = 10
    facingRight = False
    facingLeft = False
    facingUp = False
    facingDown = False
    isIdle = True
    isFlashing = False
    isInvulnerable = False
    IsBlue = False
    IsYellow = False
    IsPurple = False
    IsGreen = False
    IsColored = False
    IsAttacking = False
    IsCollidable = True
    BlueCount = 0
    YellowCount = 0
    GreenCount = 0
    PurpleCount = 0
    Limit = 300
    FlashCount = 0
    FlashLimit = 150
    PlayerSpeedAdded = 0
    EnemySpeedRemoved = 0
    EnemySpawnAdded = 0
    AttackNum = 0
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("Images/Swordsman/Swordsman-Idle-North_00.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(center=((SCREEN_WIDTH/2), 650))

    def update(self, pressed_keys):

        playerAnimationRight = ["Images/Swordsman/Swordsman-Run-East_00.png", "Images/Swordsman/Swordsman-Run-East_01.png",
                                "Images/Swordsman/Swordsman-Run-East_02.png", "Images/Swordsman/Swordsman-Run-East_03.png",
                                "Images/Swordsman/Swordsman-Run-East_04.png", "Images/Swordsman/Swordsman-Run-East_05.png",
                                "Images/Swordsman/Swordsman-Run-East_06.png", "Images/Swordsman/Swordsman-Run-East_07.png",
                                "Images/Swordsman/Swordsman-Run-East_08.png", "Images/Swordsman/Swordsman-Run-East_09.png",
                                "Images/Swordsman/Swordsman-Run-East_10.png"]
        playerAnimationLeft = ["Images/Swordsman/Swordsman-Run-West_00.png", "Images/Swordsman/Swordsman-Run-West_01.png",
                                "Images/Swordsman/Swordsman-Run-West_02.png", "Images/Swordsman/Swordsman-Run-West_03.png",
                                "Images/Swordsman/Swordsman-Run-West_04.png", "Images/Swordsman/Swordsman-Run-West_05.png",
                                "Images/Swordsman/Swordsman-Run-West_06.png", "Images/Swordsman/Swordsman-Run-West_07.png",
                                "Images/Swordsman/Swordsman-Run-West_08.png", "Images/Swordsman/Swordsman-Run-West_09.png",
                                "Images/Swordsman/Swordsman-Run-West_10.png"]
        playerAnimationUp = ["Images/Swordsman/Swordsman-Run-North_00.png", "Images/Swordsman/Swordsman-Run-North_01.png",
                                "Images/Swordsman/Swordsman-Run-North_02.png", "Images/Swordsman/Swordsman-Run-North_03.png",
                                "Images/Swordsman/Swordsman-Run-North_04.png", "Images/Swordsman/Swordsman-Run-North_05.png",
                                "Images/Swordsman/Swordsman-Run-North_06.png", "Images/Swordsman/Swordsman-Run-North_07.png",
                                "Images/Swordsman/Swordsman-Run-North_08.png", "Images/Swordsman/Swordsman-Run-North_09.png",
                                "Images/Swordsman/Swordsman-Run-North_10.png"]
        playerAnimationDown = ["Images/Swordsman/Swordsman-Run-South_00.png", "Images/Swordsman/Swordsman-Run-South_01.png",
                                "Images/Swordsman/Swordsman-Run-South_02.png", "Images/Swordsman/Swordsman-Run-South_03.png",
                                "Images/Swordsman/Swordsman-Run-South_04.png", "Images/Swordsman/Swordsman-Run-South_05.png",
                                "Images/Swordsman/Swordsman-Run-South_06.png", "Images/Swordsman/Swordsman-Run-South_07.png",
                                "Images/Swordsman/Swordsman-Run-South_08.png", "Images/Swordsman/Swordsman-Run-South_09.png",
                                "Images/Swordsman/Swordsman-Run-South_10.png"]
        PlayerIdleAnimation = ["Images/Swordsman/Swordsman-Idle-North_00.png", "Images/Swordsman/Swordsman-Idle-North_01.png",
                               "Images/Swordsman/Swordsman-Idle-North_02.png", "Images/Swordsman/Swordsman-Idle-North_03.png",
                               "Images/Swordsman/Swordsman-Idle-North_04.png", "Images/Swordsman/Swordsman-Idle-North_05.png",
                               "Images/Swordsman/Swordsman-Idle-North_06.png", "Images/Swordsman/Swordsman-Idle-North_07.png",
                               "Images/Swordsman/Swordsman-Idle-North_08.png", "Images/Swordsman/Swordsman-Idle-North_09.png",
                               "Images/Swordsman/Swordsman-Idle-North_10.png"]
        PlayerAttackAnimation = ["Images/Swordsman/Swordsman-Attack-North_00.png", "Images/Swordsman/Swordsman-Attack-North_01.png",
                                 "Images/Swordsman/Swordsman-Attack-North_02.png", "Images/Swordsman/Swordsman-Attack-North_03.png",
                                 "Images/Swordsman/Swordsman-Attack-North_04.png", "Images/Swordsman/Swordsman-Attack-North_05.png",
                                 "Images/Swordsman/Swordsman-Attack-North_06.png", "Images/Swordsman/Swordsman-Attack-North_07.png",
                                 "Images/Swordsman/Swordsman-Attack-North_08.png", "Images/Swordsman/Swordsman-Attack-North_09.png",
                                 "Images/Swordsman/Swordsman-Attack-North_10.png"]

        if self.moving:
            if self.facingRight:
                if self.walkCount > len(playerAnimationRight) - 1:
                    self.walkCount = 0
                self.surf = pygame.image.load(playerAnimationRight[self.walkCount]).convert_alpha()
                if self.isFlashing:
                    if self.FlashCount % 5 == 0:
                        player.surf = pygame.image.load("Images/Swordsman/Swordsman_Flash.png").convert_alpha()
                self.walkCount += 1
            elif self.facingLeft:
                if self.walkCount > len(playerAnimationLeft) - 1:
                    self.walkCount = 0
                self.surf = pygame.image.load(playerAnimationLeft[self.walkCount]).convert_alpha()
                if self.isFlashing:
                    if self.FlashCount % 5 == 0:
                        player.surf = pygame.image.load("Images/Swordsman/Swordsman_Flash.png").convert_alpha()
                self.walkCount += 1
            elif self.facingUp:
                if self.walkCount > len(playerAnimationUp) - 1:
                    self.walkCount = 0
                self.surf = pygame.image.load(playerAnimationUp[self.walkCount]).convert_alpha()
                if self.isFlashing:
                    if self.FlashCount % 5 == 0:
                        player.surf = pygame.image.load("Images/Swordsman/Swordsman_Flash.png").convert_alpha()
                self.walkCount += 1
            elif self.facingDown:
                if self.walkCount > len(playerAnimationDown) - 1:
                    self.walkCount = 0
                self.surf = pygame.image.load(playerAnimationDown[self.walkCount]).convert_alpha()
                if self.isFlashing:
                    if self.FlashCount % 5 == 0:
                        player.surf = pygame.image.load("Images/Swordsman/Swordsman_Flash.png").convert_alpha()
                self.walkCount += 1
        elif self.isIdle:
            self.moving = False
            if self.IdleCount > len(PlayerIdleAnimation) - 1:
                self.IdleCount = 0
            self.surf = pygame.image.load(PlayerIdleAnimation[self.IdleCount]).convert_alpha()
            if self.isFlashing:
                if self.FlashCount % 5 == 0:
                    player.surf = pygame.image.load("Images/Swordsman/Swordsman_Flash.png").convert_alpha()
            self.IdleCount += 1
        elif self.IsAttacking:
            if self.AttackCount > len(PlayerAttackAnimation)-1:
                self.AttackCount = 0
                if self.AttackNum != 0:
                    self.isIdle = True
                    self.IsAttacking = False
                    self.isInvulnerable = False
                    self.IsMovable = True
                else:
                    self.AttackNum += 1
            else:
                if self.AttackCount % 3 == 0:
                    self.surf = pygame.image.load(PlayerAttackAnimation[self.AttackCount]).convert_alpha()
                self.AttackCount += 1



        if self.IsMovable:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(self.Speed * -1,0)
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(self.Speed,0)
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, self.Speed * -1)
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, self.Speed)
            if pressed_keys[K_a]:
                self.rect.move_ip(self.Speed * -1,0)
            if pressed_keys[K_d]:
                self.rect.move_ip(self.Speed,0)
            if pressed_keys[K_w]:
                self.rect.move_ip(0, self.Speed * -1)
            if pressed_keys[K_s]:
                self.rect.move_ip(0, self.Speed)


        #Keep the player from going off screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def Reset(self):
        self.surf = pygame.image.load("Images/Swordsman/Swordsman-Idle-North_00.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(center=((SCREEN_WIDTH / 2), 650))
        self.isFlashing = True
        self.isInvulnerable = True
        self.IsMovable = True
        self.IsCollidable = True


class Enemy(pygame.sprite.Sprite):
    WalkCount = 0
    AttackCount = 0
    DeathCount = 0
    Dying = False
    CurrentSpeed = 4
    IsAttacking = False
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("Images/Enemy/Enemy-Melee-Ghost-S_00.png").convert_alpha()
        self.rect = self.surf.get_rect(center=(random.randint(5, SCREEN_WIDTH-10), random.randint(1, 10)))
        self.speed = self.CurrentSpeed
        self.etype = 'Ghost'

    def update(self):
        EnemyMove = ["Images/Enemy/Enemy-Melee-Ghost-S_00.png", "Images/Enemy/Enemy-Melee-Ghost-S_01.png",
                     "Images/Enemy/Enemy-Melee-Ghost-S_02.png", "Images/Enemy/Enemy-Melee-Ghost-S_03.png",
                     "Images/Enemy/Enemy-Melee-Ghost-S_04.png", "Images/Enemy/Enemy-Melee-Ghost-S_05.png",
                     "Images/Enemy/Enemy-Melee-Ghost-S_06.png", "Images/Enemy/Enemy-Melee-Ghost-S_07.png",
                     "Images/Enemy/Enemy-Melee-Ghost-S_08.png", "Images/Enemy/Enemy-Melee-Ghost-S_09.png",
                     "Images/Enemy/Enemy-Melee-Ghost-S_10.png", "Images/Enemy/Enemy-Melee-Ghost-S_11.png"]
        EnemyAttack = ["Images/Enemy/Enemy-Melee-Attack-S_00.png", "Images/Enemy/Enemy-Melee-Attack-S_01.png",
                       "Images/Enemy/Enemy-Melee-Attack-S_02.png", "Images/Enemy/Enemy-Melee-Attack-S_03.png",
                       "Images/Enemy/Enemy-Melee-Attack-S_04.png", "Images/Enemy/Enemy-Melee-Attack-S_05.png",
                       "Images/Enemy/Enemy-Melee-Attack-S_06.png", "Images/Enemy/Enemy-Melee-Attack-S_07.png",
                       "Images/Enemy/Enemy-Melee-Attack-S_08.png", "Images/Enemy/Enemy-Melee-Attack-S_09.png",
                       "Images/Enemy/Enemy-Melee-Attack-S_10.png", "Images/Enemy/Enemy-Melee-Attack-S_11.png",
                       "Images/Enemy/Enemy-Melee-Attack-S_12.png", "Images/Enemy/Enemy-Melee-Attack-S_13.png",
                       "Images/Enemy/Enemy-Melee-Attack-S_14.png", "Images/Enemy/Enemy-Melee-Attack-S_15.png",
                       "Images/Enemy/Enemy-Melee-Attack-S_16.png", "Images/Enemy/Enemy-Melee-Attack-S_17.png",
                       "Images/Enemy/Enemy-Melee-Attack-S_18.png", "Images/Enemy/Enemy-Melee-Attack-S_19.png",
                       "Images/Enemy/Enemy-Melee-Attack-S_20.png", "Images/Enemy/Enemy-Melee-Attack-S_21.png",
                       "Images/Enemy/Enemy-Melee-Attack-S_21.png", "Images/Enemy/Enemy-Melee-Attack-S_23.png"]
        EnemyDeath = ["Images/Enemy/Enemy-Melee-Death_00.png", "Images/Enemy/Enemy-Melee-Death_01.png",
                      "Images/Enemy/Enemy-Melee-Death_02.png", "Images/Enemy/Enemy-Melee-Death_03.png",
                      "Images/Enemy/Enemy-Melee-Death_04.png", "Images/Enemy/Enemy-Melee-Death_05.png",
                      "Images/Enemy/Enemy-Melee-Death_06.png", "Images/Enemy/Enemy-Melee-Death_07.png",
                      "Images/Enemy/Enemy-Melee-Death_08.png", "Images/Enemy/Enemy-Melee-Death_09.png",
                      "Images/Enemy/Enemy-Melee-Death_10.png", "Images/Enemy/Enemy-Melee-Death_11.png",
                      "Images/Enemy/Enemy-Melee-Death_12.png", "Images/Enemy/Enemy-Melee-Death_13.png",
                      "Images/Enemy/Enemy-Melee-Death_14.png", "Images/Enemy/Enemy-Melee-Death_15.png",
                      "Images/Enemy/Enemy-Melee-Death_16.png", "Images/Enemy/Enemy-Melee-Death_17.png",
                      "Images/Enemy/Enemy-Melee-Death_18.png", "Images/Enemy/Enemy-Melee-Death_19.png",
                      "Images/Enemy/Enemy-Melee-Death_20.png", "Images/Enemy/Enemy-Melee-Death_21.png",
                      "Images/Enemy/Enemy-Melee-Death_22.png", "Images/Enemy/Enemy-Melee-Death_23.png",]
        if self.IsAttacking != True:
            if self.WalkCount > len(EnemyMove)-1:
                self.WalkCount = 0
            self.surf = pygame.image.load(EnemyMove[self.WalkCount]).convert_alpha()
            self.WalkCount += 1
        else:
            if self.AttackCount > len(EnemyAttack)-1:
                self.AttackCount = 0
                self.IsAttacking = False
                player.Reset()
            self.surf = pygame.image.load(EnemyAttack[self.AttackCount]).convert_alpha()
            self.AttackCount += 1


        if self.rect.bottom >= SCREEN_HEIGHT-15:
            if self.DeathCount > len(EnemyDeath) - 1:
                self.kill()
                if self.IsAttacking == True:
                    player.IsMovable = True
                self.DeathCount = 0
            else:
                self.surf = pygame.image.load(EnemyDeath[self.DeathCount]).convert_alpha()
                self.DeathCount += 1
        else:
            if self.IsAttacking != True:
                self.rect.move_ip(0, self.speed)



class Potions(pygame.sprite.Sprite):
    CurrSpeed = 4
    BubbleCount = 0
    PotionList = ["Blue", "Yellow", "Red", "Green", "Purple"]


    def __init__(self):
        super(Potions, self).__init__()
        Potion = random.choice(self.PotionList)
        if Potion == "Blue":
            self.surf = pygame.image.load("Images/Potions/Blue/00_Blue_Potion_Full.png").convert_alpha()
            self.etype = "Blue"
        elif Potion == "Red":
            self.surf = pygame.image.load("Images/Potions/Red/00_Red_Potion_Full.png").convert_alpha()
            self.etype = "Red"
        elif Potion == "Yellow":
            self.surf = pygame.image.load("Images/Potions/Yellow/00_Yellow_Potion_Full.png").convert_alpha()
            self.etype = "Yellow"
        elif Potion == "Green":
            self.surf = pygame.image.load("Images/Potions/Green/00_Green_Potion_Full.png").convert_alpha()
            self.etype = "Green"
        elif Potion == "Purple":
            self.surf = pygame.image.load("Images/Potions/Purple/00_Purple_Potion_Full.png").convert_alpha()
            self.etype = "Purple"
        self.rect = self.surf.get_rect(center=(random.randint(5, SCREEN_WIDTH - 10), random.randint(1, 10)))
        self.speed = self.CurrSpeed

    def update(self):
        #All potion sprites gotten from Flip on Itch.io.
        BluePotionBubble = ["Images/Potions/Blue/00_Blue_Potion_Full.png", "Images/Potions/Blue/01_Blue_Potion_Full.png",
                            "Images/Potions/Blue/02_Blue_Potion_Full.png", "Images/Potions/Blue/03_Blue_Potion_Full.png",
                            "Images/Potions/Blue/04_Blue_Potion_Full.png", "Images/Potions/Blue/05_Blue_Potion_Full.png",
                            "Images/Potions/Blue/06_Blue_Potion_Full.png", "Images/Potions/Blue/07_Blue_Potion_Full.png"]
        RedPotionBubble = ["Images/Potions/Red/00_Red_Potion_Full.png", "Images/Potions/Red/01_Red_Potion_Full.png",
                           "Images/Potions/Red/02_Red_Potion_Full.png", "Images/Potions/Red/03_Red_Potion_Full.png",
                           "Images/Potions/Red/04_Red_Potion_Full.png", "Images/Potions/Red/05_Red_Potion_Full.png",
                           "Images/Potions/Red/06_Red_Potion_Full.png", "Images/Potions/Red/07_Red_Potion_Full.png"]
        YellowPotionBubble = ["Images/Potions/Yellow/00_Yellow_Potion_Full.png", "Images/Potions/Yellow/01_Yellow_Potion_Full.png",
                              "Images/Potions/Yellow/02_Yellow_Potion_Full.png", "Images/Potions/Yellow/03_Yellow_Potion_Full.png",
                              "Images/Potions/Yellow/04_Yellow_Potion_Full.png", "Images/Potions/Yellow/05_Yellow_Potion_Full.png",
                              "Images/Potions/Yellow/06_Yellow_Potion_Full.png", "Images/Potions/Yellow/07_Yellow_Potion_Full.png"]
        GreenPotionBubble = ["Images/Potions/Green/00_Green_Potion_Full.png", "Images/Potions/Green/01_Green_Potion_Full.png",
                             "Images/Potions/Green/02_Green_Potion_Full.png", "Images/Potions/Green/03_Green_Potion_Full.png",
                             "Images/Potions/Green/04_Green_Potion_Full.png", "Images/Potions/Green/05_Green_Potion_Full.png",
                             "Images/Potions/Green/06_Green_Potion_Full.png", "Images/Potions/Green/07_Green_Potion_Full.png"]
        PurplePotionBubble = ["Images/Potions/Purple/00_Purple_Potion_Full.png", "Images/Potions/Purple/01_Purple_Potion_Full.png",
                              "Images/Potions/Purple/02_Purple_Potion_Full.png", "Images/Potions/Purple/03_Purple_Potion_Full.png",
                              "Images/Potions/Purple/04_Purple_Potion_Full.png", "Images/Potions/Purple/05_Purple_Potion_Full.png",
                              "Images/Potions/Purple/06_Purple_Potion_Full.png", "Images/Potions/Purple/07_Purple_Potion_Full.png"]

        if self.BubbleCount > len(BluePotionBubble) - 1:
            self.BubbleCount = 0
        if self.etype == "Blue":
            self.surf = pygame.image.load(BluePotionBubble[self.BubbleCount]).convert_alpha()
            self.BubbleCount += 1
        elif self.etype == "Red":
            self.surf = pygame.image.load(RedPotionBubble[self.BubbleCount]).convert_alpha()
            self.BubbleCount += 1
        elif self.etype == "Yellow":
            self.surf = pygame.image.load(YellowPotionBubble[self.BubbleCount]).convert_alpha()
            self.BubbleCount += 1
        elif self.etype == "Green":
            self.surf = pygame.image.load(GreenPotionBubble[self.BubbleCount]).convert_alpha()
            self.BubbleCount += 1
        elif self.etype == "Purple":
            self.surf = pygame.image.load(PurplePotionBubble[self.BubbleCount]).convert_alpha()
            self.BubbleCount += 1

        if self.rect.bottom >= SCREEN_HEIGHT - 15:
            self.kill()
        else:
            self.rect.move_ip(0, self.speed)

def LevelUp(Level, RED, BLUE, GREEN):
    pygame.time.set_timer(ADDENEMY, EnemySpawnSpeed-30)
    Enemy.CurrentSpeed += 1
    Player.Speed += 2
    Level += 1
    RED = random.randint(10, 245)
    BLUE = random.randint(10, 245)
    GREEN = random.randint(10, 245)
    return Level, RED, BLUE, GREEN

def getDbConnection():
    conn = None
    try:
        conn = sqlite3.connect("GameStats.db")
    except Error as e:
        print(e)
    return conn


def saveGameStats(userName, highScore, enemyKilled, potionCollected, redPotionCollected, bluePotionCollected, yellowPotionCollected,
                          greenPotionCollected, purplePotionCollected):
    conn = getDbConnection()
    curr = conn.cursor()
    updateSql = "UPDATE Stats set HighScore = ?,EnemyKilled = ?,PotionsCollected = ?,RedPotionsCollected = ?,BluePotionsCollected = ?," \
                "YellowPotionsCollected = ?,GreenPotionsCollected = ?,PurplePotionsCollected = ? WHERE UserID = ?"
    record = (highScore, enemyKilled, potionCollected, redPotionCollected, bluePotionCollected, yellowPotionCollected,
                          greenPotionCollected, purplePotionCollected, userName)
    print(f"this is the sql update: {updateSql}")
    curr.execute(updateSql, record)
    print(record)
    conn.commit()
    conn.close()

user_name = GL.GameLogon()

con = getDbConnection()
curr = con.cursor()

#rows = curr.execute("SELECT * FROM Stats").fetchall()
rows = curr.execute("SELECT * FROM Stats WHERE UserID = ?", (user_name,)).fetchall()
if user_name == '':
    running = False
    GameOver = False
else:
    running = True
    if len(rows) == 0:
        record = (user_name, 0, 0, 0, 0, 0, 0, 0, 0)
        sql = "INSERT INTO Stats (UserId,HighScore,EnemyKilled,PotionsCollected,RedPotionsCollected,BluePotionsCollected,YellowPotionsCollected," \
            "GreenPotionsCollected,PurplePotionsCollected) values(?,?,?,?,?,?,?,?,?)"
        curr.execute(sql, record)
        con.commit()
    else:
        for row in rows:
            highScore = row[1]
            enemyKilled = row[2]
            potionCollected = row[3]
            redPotionCollected = row[4]
            bluePotionCollected = row[5]
            yellowPotionCollected = row[6]
            greenPotionCollected = row[7]
            purplePotionCollected = row[8]




#Main Code
pygame.init()

Lives = 10
Level = 1
black = (0, 0, 0)
myFont = pygame.font.SysFont("Comicsans", 40)
Lives_Label = myFont.render("Lives: ", 1, black)
Lives_Value = myFont.render(str(Lives), 1, black)
Level_Label = myFont.render("Level: ", 1, black)
Level_Value = myFont.render(str(Level), 1, black)
Score_Label = myFont.render("Score: ", 1, black)
Score_Value = myFont.render(str(Score), 1, black)
highScore_Label = myFont.render("High Score: ", 1, black)
highScore_Value = myFont.render(str(highScore), 1, black)
myEndFont = pygame.font.SysFont("Comicsans", 80)
End_Label = myEndFont.render("GAME OVER!!!", 1, black)
End_Score = myEndFont.render("Final Score: ", 1, black)
End_Score_Number = myEndFont.render(str(Score), 1, black)
EnemyLevel = 1

clock = pygame.time.Clock()

ADDENEMY = pygame.USEREVENT+1
LEVELUP = pygame.USEREVENT+2
ADDPOTION = pygame.USEREVENT+3
SCOREUP = pygame.USEREVENT+4
pygame.time.set_timer(ADDENEMY, EnemySpawnSpeed)
pygame.time.set_timer(LEVELUP, 30000)
pygame.time.set_timer(ADDPOTION, 10000)
pygame.time.set_timer(SCOREUP, 10000)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Avoidance game")

player = Player()
enemy = Enemy()
potion = Potions()

all_Sprites = pygame.sprite.Group()
all_Enemies = pygame.sprite.Group()
all_potions = pygame.sprite.Group()
all_Sprites.add(player)
all_Enemies.add(enemy)
all_Sprites.add(enemy)
all_potions.add(potion)
all_Sprites.add(potion)



while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                player.moving = True
                player.facingRight = False
                player.facingLeft = True
                player.facingUp = False
                player.facingDown = False
            elif event.key == K_RIGHT or event.key == K_d:
                player.moving = True
                player.facingRight = True
                player.facingLeft = False
                player.facingUp = False
                player.facingDown = False
            elif event.key == K_UP or event.key == K_w:
                player.moving = True
                player.facingRight = False
                player.facingLeft = False
                player.facingUp = True
                player.facingDown = False
            elif event.key == K_DOWN or event.key == K_s:
                player.moving = True
                player.facingRight = False
                player.facingLeft = False
                player.facingUp = False
                player.facingDown = True
            if event.key == K_ESCAPE:
                running = False
                GameOver = False
            if event.key == K_SPACE:
                player.moving = False
                player.isIdle = False
                player.IsAttacking = True
                player.IsMovable = False
                player.isInvulnerable = True
        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_a:
                player.moving = False
                player.isIdle = True
            elif event.key == K_RIGHT or event.key == K_d:
                player.moving = False
                player.isIdle = True
            elif event.key == K_UP or event.key == K_w:
                player.moving = False
                player.isIdle = True
            elif event.key == K_DOWN or event.key == K_s:
                player.moving = False
                player.isIdle = True
        elif event.type == QUIT:
            running = False
            GameOver = False
        elif event.type == ADDENEMY:
            newEnemy = Enemy()
            all_Enemies.add(newEnemy)
            all_Sprites.add(newEnemy)
        elif event.type == LEVELUP:
            Level, RED, BLUE, GREEN = LevelUp(Level, RED, BLUE, GREEN)
        elif event.type == ADDPOTION:
            randnum = random.randint(1, 3)
            if randnum == 1:
                newPotion = Potions()
                all_potions.add(newPotion)
                all_Sprites.add(newPotion)
        elif event.type == SCOREUP:
            Score += 10

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    all_Enemies.update()
    all_potions.update()

    screen.fill((RED, BLUE, GREEN))

    for entity in all_Sprites:
        screen.blit(entity.surf, entity.rect)

    if player.IsBlue:
        if player.BlueCount >= Player.Limit:
            player.IsBlue = False
            player.IsColored = False
            player.BlueCount = 0
        else:
            player.BlueCount += 1
    elif player.IsGreen:
        if player.GreenCount >= player.Limit:
            player.IsGreen = False
            player.IsColored = False
            player.GreenCount = 0
        else:
            player.GreenCount += 1
    elif player.IsYellow:
        if player.YellowCount >= player.Limit:
            player.IsYellow = False
            player.IsColored = False
            player.YellowCount = 0
        else:
            player.YellowCount += 1
    elif player.IsPurple:
        if player.PurpleCount >= player.Limit:
            player.IsPurple = False
            player.IsColored = False
            player.PurpleCount = 0
        else:
            player.PurpleCount += 1

    PlayervsSpectre = pygame.sprite.spritecollideany(player, all_Enemies)
    if player.IsCollidable == True:
        if PlayervsSpectre != None:
            if player.isInvulnerable == False:
                player.IsMovable = False
                player.isInvulnerable = True
                PlayervsSpectre.IsAttacking = True
                player.isFlashing = True
                Lives -= 1
                player.IsCollidable = False
            else:
                PlayervsSpectre.kill()
                player.IsMovable = True
                enemyKilled += 1

    PlayerPotion = pygame.sprite.spritecollideany(player, all_potions)
    if PlayerPotion != None:
        if PlayerPotion.etype == "Blue":
            player.IsColored = True
            player.IsBlue = True
            player.IsYellow = False
            player.IsGreen = False
            player.IsPurple = False
            potionCollected += 1
            bluePotionCollected +=1
        if PlayerPotion.etype == "Red":
            Lives += 1
            potionCollected +=1
            redPotionCollected +=1
        if PlayerPotion.etype == "Yellow":
            player.IsColored = True
            player.IsBlue = False
            player.IsYellow = True
            player.IsGreen = False
            player.IsPurple = False
            potionCollected +=1
            yellowPotionCollected += 1
        if PlayerPotion.etype == "Purple":
            player.IsColored = True
            player.IsBlue = False
            player.IsYellow = False
            player.IsGreen = False
            player.IsPurple = True
            potionCollected += 1
            purplePotionCollected += 1
        if PlayerPotion.etype == "Green":
            player.IsColored = True
            player.IsBlue = False
            player.IsYellow = False
            player.IsGreen = True
            player.IsPurple = False
            potionCollected += 1
            greenPotionCollected += 1
        PlayerPotion.kill()

        if player.IsBlue:
            player.BlueCount = 0
            player.YellowCount = 0
            player.GreenCount = 0
            player.PurpleCount = 0
            player.PlayerSpeedAdded += player.Speed/2
            player.Speed = player.Speed + (player.Speed/2)
            player.isInvulnerable = False
            Enemy.CurrentSpeed += player.EnemySpeedRemoved
            EnemySpawnSpeed -= player.EnemySpawnAdded
            player.EnemySpeedRemoved = 0
            player.EnemySpawnAdded = 0
        elif player.IsYellow:
            player.BlueCount = 0
            player.YellowCount = 0
            player.GreenCount = 0
            player.PurpleCount = 0
            player.Speed -= player.PlayerSpeedAdded
            player.isInvulnerable = True
            Enemy.CurrentSpeed += player.EnemySpeedRemoved
            EnemySpawnSpeed -= player.EnemySpawnAdded
            player.PlayerSpeedAdded = 0
            player.EnemySpeedRemoved = 0
            player.EnemySpawnAdded = 0
        elif player.IsPurple:
            player.BlueCount = 0
            player.YellowCount = 0
            player.GreenCount = 0
            player.PurpleCount = 0
            player.EnemySpeedRemoved += (Enemy.CurrentSpeed / 2)
            player.Speed -= player.PlayerSpeedAdded
            player.isInvulnerable = False
            Enemy.CurrentSpeed = Enemy.CurrentSpeed - (Enemy.CurrentSpeed / 2)
            EnemySpawnSpeed -= player.EnemySpawnAdded
            player.PlayerSpeedAdded = 0
            player.EnemySpawnAdded = 0
        elif player.IsGreen:
            player.BlueCount = 0
            player.YellowCount = 0
            player.GreenCount = 0
            player.PurpleCount = 0
            player.EnemySpawnAdded = EnemySpawnSpeed//2
            player.Speed -= player.PlayerSpeedAdded
            player.isInvulnerable = False
            Enemy.CurrentSpeed += player.EnemySpeedRemoved
            EnemySpawnSpeed += player.EnemySpawnAdded
            player.PlayerSpeedAdded = 0
            player.EnemySpeedRemoved = 0


    if player.IsColored != True:
        if player.isFlashing != True:
            player.BlueCount = 0
            player.YellowCount = 0
            player.GreenCount = 0
            player.PurpleCount = 0
            player.Speed -= player.PlayerSpeedAdded
            player.isInvulnerable = False
            Enemy.CurrentSpeed += player.EnemySpeedRemoved
            EnemySpawnSpeed -= player.EnemySpawnAdded
            player.PlayerSpeedAdded = 0
            player.EnemySpeedRemoved = 0
            player.EnemySpawnAdded = 0
        else:
            player.BlueCount = 0
            player.YellowCount = 0
            player.GreenCount = 0
            player.PurpleCount = 0
            player.Speed -= player.PlayerSpeedAdded
            Enemy.CurrentSpeed += player.EnemySpeedRemoved
            EnemySpawnSpeed -= player.EnemySpawnAdded
            player.PlayerSpeedAdded = 0
            player.EnemySpeedRemoved = 0
            player.EnemySpawnAdded = 0


    if player.isFlashing:
        if player.FlashCount >= player.FlashLimit:
            player.isFlashing = False
            player.isInvulnerable = False
            player.FlashCount = 0
        else:
            player.FlashCount += 1


    if Lives > 0:
        if Score > highScore:
            highScore = Score
            highScore_Value = myFont.render(str(highScore), 1, black)
        Level_Value = myFont.render(str(Level), 1, black)
        Lives_Value = myFont.render(str(Lives), 1, black)
        Score_Value = myFont.render(str(Score), 1, black)
        screen.blit(Level_Label, (SCREEN_WIDTH-110, 2))
        screen.blit(Level_Value, (SCREEN_WIDTH-20, 2))
        screen.blit(Lives_Label, (SCREEN_WIDTH-490, 2))
        screen.blit(Lives_Value, (SCREEN_WIDTH-400, 2))
        screen.blit(Score_Label, (SCREEN_WIDTH-350, 2))
        screen.blit(Score_Value, (SCREEN_WIDTH-260, 2))
        screen.blit(highScore_Label, (SCREEN_WIDTH-350, 35))
        screen.blit(highScore_Value, (SCREEN_WIDTH-180, 35))
    else:
        running = False
        for entity in all_Sprites:
            entity.kill()



    pygame.display.flip()
    clock.tick(30)


if GameOver:
    saveGameStats(user_name, highScore, enemyKilled, potionCollected, redPotionCollected, bluePotionCollected, yellowPotionCollected,
                  greenPotionCollected, purplePotionCollected)
    for entity in all_Enemies:
        entity.kill()
    pygame.display.flip()
    End_Score_Number = myEndFont.render(str(Score), 1, black)
    screen.blit(End_Label, (SCREEN_WIDTH-470, SCREEN_HEIGHT/2-50))
    screen.blit(End_Score, (SCREEN_WIDTH-470, (SCREEN_HEIGHT/2)))
    screen.blit(End_Score_Number, (SCREEN_WIDTH-100, (SCREEN_HEIGHT/2)))
    pygame.display.flip()
    time.sleep(5)

