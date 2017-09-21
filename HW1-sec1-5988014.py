from turtle import *

# HELPER FUNCTIONS
def draw(sides=6, size=50):
  for i in range(sides):
    fd(size)
    rt(360/sides)

def one():
  round = 8
  color('red')
  for i in range(round):
    draw(6)
    rt(360/round)

def two():
  color('blue')
  speed(60)
  lt(180)
  for i in range(65):
    rt(5)
    # DRAW STAR
    for j in range(5):
      fd(i*3)
      rt(144)

def three():
  color('black')
  for i in range(8):
    fd(200)
    rt(135)

