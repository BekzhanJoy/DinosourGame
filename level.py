import pygame
import globals
import utils

class Level:
    def __init__(self, platforms=None, entities=None, winFunc=None, loseFunc=None, powerupSpawnPoints=None):
        self.platforms = platforms
        self.entities = entities
        self.winFunc = winFunc
        self.loseFunc = loseFunc
        self.powerupSpawnPoints = powerupSpawnPoints
    def isWon(self):
        if self.winFunc is None:
            return False
        return self.winFunc(self)
    def isLost(self):
        if self.loseFunc is None:
            return False
        return self.loseFunc(self)

def lostLevel(level):
    for entity in level.entities:
        if entity.type == 'player':
            if entity.battle is not None:
                if entity.battle.lives > 0:
                    return False
    return True

def wonLevel(level):
    for entity in level.entities:
        if entity.type == 'collectable':
            return False
    return True

def loadLevel(levelNumber):
    if levelNumber == 1:
        globals.world = Level(
            platforms = [
                # middle
                pygame.Rect(100,300,400,50),
                # left
                pygame.Rect(100,250,50,50),
                # right
                pygame.Rect(450,250,50,50)
            ],
            entities = [
                utils.makeCoin(100,200),
                utils.makeCoin(200,250),
                utils.makeEnemy(150,274)
            ],
            winFunc = wonLevel,
            loseFunc = lostLevel,
        )
    if levelNumber == 3:

        globals.world = Level(
            platforms=[
                # left
                pygame.Rect(0, 150, 200, 50),
                # right
                pygame.Rect(400, 150, 200, 50),
                # top
                pygame.Rect(200, -100, 200, 50),
                # bottom
                pygame.Rect(200, 200, 200, 50)
            ],
            entities=[
                utils.makeCoin(100, 100),
                utils.makeCoin(550, 140),
                utils.makeEnemy(450, 130)
            ],
            winFunc=wonLevel,
            loseFunc=lostLevel,
        )
    if levelNumber == 2:

        globals.world = Level(
            platforms=[
                # left platform
                pygame.Rect(0, 400, 300, 50),
                # right platform
                pygame.Rect(550, 400, 300, 50),
                # middle platform
                pygame.Rect(250, 250, 350, 50),
                # top platform
                pygame.Rect(350, 100, 150, 50)
            ],
            entities=[
                utils.makeCoin(400, 200),
                utils.makeCoin(600, 350),
                utils.makeEnemy(400, 80)
            ],
            winFunc=wonLevel,
            loseFunc=lostLevel,
        )
    if levelNumber == 4:
        globals.world = Level(
            platforms=[
                pygame.Rect(50, 110, 200, 30),  # Platform 1
                pygame.Rect(400, 110, 200, 30),  # Platform 2
                pygame.Rect(250, 200, 300, 30),  # Platform 3
                pygame.Rect(200, 350, 200, 30),  # Platform 4
                pygame.Rect(300, 350, 200, 30)  # Platform 5
            ],
            entities=[
                utils.makeCoin(150, 30),
                utils.makeCoin(450, 30),
                utils.makeCoin(250, 170),
                utils.makeCoin(150, 320),
                utils.makeCoin(540, 320),
            ],
            winFunc=wonLevel,
            loseFunc=lostLevel,
        )
    if levelNumber == 5:
        globals.world = Level(
            platforms=[
                pygame.Rect(100, 200, 200, 30),  # Platform 1
                pygame.Rect(300, 200, 200, 30),  # Platform 2
                pygame.Rect(550, 200, 300, 30),  # Platform 3
                pygame.Rect(700, 200, 200, 30),  # Platform 4
                pygame.Rect(900, 200, 200, 30),
                pygame.Rect(400, 520, 200, 30)
            ],
            entities=[
                utils.makeCoin(150, 170),
                utils.makeCoin(450, 170),
                utils.makeCoin(560, 170),
                utils.makeCoin(300, 170),
                utils.makeCoin(800, 170),
                utils.makeEnemy(503, 190),
                utils.makeEnemy(503, 220),
                utils.makeEnemy(503, 250),
                utils.makeEnemy(503, 280),
                utils.makeEnemy(503, 310),
                utils.makeEnemy(503, 340),
                utils.makeEnemy(503, 370),
                utils.makeEnemy(503, 400),
                utils.makeEnemy(503, 430),
                utils.makeEnemy(503, 460),
                utils.makeEnemy(503,490)
            ],
            winFunc=wonLevel,
            loseFunc=lostLevel,
        )

    for player in globals.players:
        globals.world.entities.append(player)

    for entity in globals.world.entities:
        entity.reset(entity)