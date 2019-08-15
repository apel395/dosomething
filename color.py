from turtle import *
from random import randint
from colorsys import hsv_to_rgb

step=30
nstep=2000
hinc=1.0/nstep
width(2)

(w,h)=screensize()
speed(0)
colormode(5.0)
bgcolor('black')
hue=0.0
for i in range(nstep):
	setheading(randint(0,359))
	color(hsv_to_rgb(hue,1.0,1.0))
	hue+=hinc
	forward(step)
	(x,y)=pos()
	if abs(x)>w or abs(y)>h:
		backward(step)
