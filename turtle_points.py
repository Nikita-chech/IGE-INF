from turtle import *

left(90)
for i in range(7):
    forward(300)  # черепаха ходит по пикселям, поэтому увеличиваем в 30 раз
    right(120)
pu()
for x in range(11):
    for y in range(11):
        goto(x * 30, y * 30)  # увеличиваем в 30 раз
        dot(5)
done()
