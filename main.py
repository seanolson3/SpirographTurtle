from turtle import Turtle
import turtle as t
import random

# Create an instance, called timmy_the_turtle, of the class Turtle from the turtle module
tim = Turtle()
t.colormode(255)

tim.pensize(1)
tim.speed("fastest")

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  random_color = (r, g, b)
  return random_color

def draw_circle():
  for _ in range(18):
    tim.forward(20)
    tim.right(20)

def rotate():
  tim.right(10)

for _ in range(36):
  tim.color(random_color())
  draw_circle()
  rotate()
