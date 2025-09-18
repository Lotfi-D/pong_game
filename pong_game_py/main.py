from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800 , 600)
screen.bgcolor("black")
screen.title('Pong')
screen.tracer(0)

paddle_player_1 = Paddle((350, 0))
paddle_player_2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(lambda: paddle_player_1.move("Up"), "Up")
screen.onkey(lambda: paddle_player_1.move("Down"), "Down")
screen.onkey(lambda: paddle_player_2.move("Up"), "z")
screen.onkey(lambda: paddle_player_2.move("Down"), "s")

game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(ball.speed_ball)
  ball.move()

  # Bounce off top/bottom walls
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  # Bounce off paddles
  if ((ball.distance(paddle_player_1) < 50 and ball.xcor() > 320) or
    (ball.distance(paddle_player_2) < 50 and ball.xcor() < -320)):
    ball.bounce_x()
  
  # detect paddle misses and increase game speed
  x_position = ball.xcor()
  if abs(x_position) > 380:                          
      scorer = "player_2" if x_position > 0 else "player_1"
      ball.reset_position()
      scoreboard.calculate_point(scorer)

  if scoreboard.player_1_score == 10 or scoreboard.player_2_score == 10:
     game_is_on = False
     scoreboard.game_over()


screen.exitonclick()