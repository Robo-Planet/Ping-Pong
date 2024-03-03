import pygame
import random

WIDTH = 800
HEIGHT = 600

player_score = 0
opponent_score = 0


def ball_animation():
    global ball_speed_x, ball_speed_y, opponent_score, player_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    elif ball.left <= 0:
        player_score += 1
        ball_restart()
    elif ball.right >= WIDTH:
        opponent_score += 1
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def ball_restart():
    global ball_speed_y, ball_speed_x
    ball.y = HEIGHT/2
    ball.x = WIDTH/2
    ball_speed_y *= random.choice((-1,1))
    ball_speed_x *= random.choice((-1,1))

def player_movement():
    if keyboard.up and player.y >= 0:
        player.y -= 5
    if keyboard.down and player.y + player.height <= HEIGHT:
        player.y += 5

def opponent_movement():
    opponent_speed = 5
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.top > ball.y:
        opponent.y -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= HEIGHT:
        opponent.bottom = HEIGHT



#Game Rectangles

ball = Rect(WIDTH/2, HEIGHT/2,10,10)
player = Rect(WIDTH - 20, HEIGHT/2 - 70, 10,140)
opponent = Rect(10, HEIGHT/2 - 70, 10, 140)
ball_speed_x = 7
ball_speed_y = 7
light_grey = (200,200,200)

def draw():
    screen.fill((83,161,215))
    screen.draw.filled_circle((ball.x, ball.y),10, light_grey)
    screen.draw.filled_rect(player, light_grey)
    screen.draw.filled_rect(opponent, light_grey)
    screen.draw.line((WIDTH/2,HEIGHT),(WIDTH/2,0),light_grey)
    screen.draw.text("Score" + ' ' + str(player_score), (550,10), fontsize = 32)
    screen.draw.text("Score" + ' ' + str(opponent_score), (150,10), fontsize = 32)
def update():
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    ball_animation()
    player_movement()
    opponent_movement()
