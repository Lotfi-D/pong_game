from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 35, "normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()

    self.color("white")
    self.hideturtle()
    self.penup()
    
    self.player_1_score = 0
    self.player_2_score = 0
    
    self.update_scoreboard()

  def calculate_point(self, player):
    if player == "player_1":
      self.player_1_score += 1
    else:
      self.player_2_score += 1
    self.update_scoreboard()
    
  def update_scoreboard(self):
    self.clear()

    self.goto(-100, 200)
    self.write(f"{self.player_2_score}", align=ALIGNMENT, font=FONT)
  
    self.goto(100, 200)
    self.write(f"{self.player_1_score}", align=ALIGNMENT, font=FONT)
  
  def game_over(self):
    winner = "Player 1" if self.player_1_score > self.player_2_score else "Player 2"
    self.goto(0, 0)
    self.write(f"{winner} is the winner", align=ALIGNMENT, font=FONT)


    

