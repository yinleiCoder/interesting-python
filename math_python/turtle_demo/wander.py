from turtle import *
from random import randint

def wander():
    while True:
        fd(3)
        if xcor() >= 200 or xcor() <= -200 or ycor() <= -200 or ycor() >= 200:
            lt(randint(90, 180))


if __name__ == '__main__':
    shape('turtle')
    speed(0)
    wander()