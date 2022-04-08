from math import sqrt
from random import randint

WIDTH = 800
HEIGHT = 600

has_catch_color = (255,0,0)
player_default_size = 15

class Player:
    
    def __init__(self, rect, controls, color, speed):
        self.rect = rect
        self.color = color
        self.controls = controls
        self.speed = speed
        self.has_catch = False
        
    def draw(self):
        if self.has_catch:
            screen.draw.filled_rect(self.rect, has_catch_color)
        else:
            screen.draw.filled_rect(self.rect, self.color)
    
    def give_catch(self, other_player):
        self.has_catch = False
        other_player.has_catch = True
        other_player.rect.x = randint(player_default_size,WIDTH - player_default_size)
        other_player.rect.y = randint(player_default_size,HEIGHT - player_default_size)
    
    def handle_movement(self):
        directionX = 0
        directionY = 0
        if keyboard[self.controls["left"]]:
            directionX = -1
        if keyboard[self.controls["right"]]:
            directionX = 1
        if keyboard[self.controls["up"]]:
            directionY = -1
        if keyboard[self.controls["down"]]:
            directionY = 1

        if directionX and directionY:
            directionY /= sqrt(2)
            directionX /= sqrt(2)

        self.rect.x += self.speed*directionX
        self.rect.y += self.speed*directionY

    def check_player_collision(self, other_player):
        return other_player.rect.colliderect(self.rect)
        
    def handle_side_collision(self, players):
        if self.rect.x < 0 :
            self.rect.x = 0
        
        if self.rect.y < 0 :
            self.rect.y = 0
            
        if self.rect.x > WIDTH - player_default_size:
            self.rect.x = WIDTH - player_default_size
        
        if self.rect.y > HEIGHT - player_default_size:
            self.rect.y = HEIGHT - player_default_size
        
    

"""
class Spiral_projectile:
    def __init__(self, name, age):
        self.name = name
        self.age = age
"""


player1_conrtols = {
    "up": 'w',
    "down": 's',
    "left": 'a',
    "right": 'd'
}

player2_conrtols = {
    "up": 'up',
    "down": 'down',
    "left": 'left',
    "right": 'right'
}

player3_conrtols = {
    "up": 'KP8',
    "down": 'KP5',
    "left": 'KP4',
    "right": 'KP6'
}


players = [
    Player(Rect((15, 15), (player_default_size, player_default_size)), player1_conrtols, (0,0,255), 5),
    Player(Rect((WIDTH - 15, HEIGHT - 15), (player_default_size, player_default_size)), player2_conrtols, (0,255,0), 5),
    #Player(Rect((WIDTH/2, HEIGHT/2), (player_default_size, player_default_size)), player3_conrtols, (0,127,127), 5)
]

players[0].has_catch = True

def update():
    for player in players:
        player.handle_movement() 
        player.handle_side_collision(players)
        
    i = 0
    while i < len(players):
        if players[i].has_catch:
            x = 0
            while x < len(players):
                if x != i:
                    if players[i].check_player_collision(players[x]):
                        players[i].give_catch(players[x])
                x += 1
        i += 1
    

def draw():
    screen.clear()
    for player in players:
        player.draw()
    
