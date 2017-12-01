import tkinter
from tkinter import *

WIDTH = 640
# width and height of our picture in pixels
HEIGHT = 640
#The zooms
xmin2 = -1.373485000588
xmax2 = -1.373420137793
ymin2 = 0.0780386221506
ymax2 = 0.0781034849453
xmin1 = -1.0743587654
xmax1 = -1.0739062997
ymin1 = -0.2414068509
ymax1 = -0.2409543851
xmin = 0.3050133341
xmax = 0.3055797071
ymin = 0.0278018392
ymax = 0.0283682122
maxIt = 255
#Max iterations

#Mandlebrot Calculation
def mandlebrot(z,c,count):
	z = z**2 + c
	count =count+1
	if abs(z)>2 or count >maxIt-1:
		return count
	return mandlebrot(z,c,count)
#Picture 1
window = Tk()
canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg = "#000000")
img = PhotoImage(width = WIDTH, height = HEIGHT)
canvas.create_image((0, 0), image = img, state = "normal", anchor = tkinter.NW)
for row in range(HEIGHT):
	for col in range(WIDTH):
		zx1 = (((xmax-xmin)*col)/WIDTH) + xmin
		zy1 = (((ymax-ymin)*row)/HEIGHT) + ymin
		c = complex(zx1,zy1)
		z = complex(0.0,0.0)
		#Execute the mandelbrot calculation
		r = mandlebrot(z,c,0)
		#Color Choices
		rd = hex(r)[2:].zfill(2)
		gr = hex(45)[2:].zfill(2)
		bl = hex(95)[2:].zfill(2)
		img.put("#" + rd + gr + bl, (col, row))
canvas.pack()

#Picture 2
window1 = tkinter.Toplevel()
canvas1 = Canvas(window1, width = WIDTH, height = HEIGHT, bg = "#000000")
img1 = PhotoImage(width = WIDTH, height = HEIGHT)
canvas1.create_image((0, 0), image = img1, state = "normal", anchor = tkinter.NW)
for row in range(HEIGHT):
	for col in range(WIDTH):
		zx1 = (((xmax1-xmin1)*col)/WIDTH) + xmin1
		zy1 = (((ymax1-ymin1)*row)/HEIGHT) + ymin1
		c = complex(zx1,zy1)
		z = complex(0.0,0.0)
		#Execute the mandelbrot calculation
		r = mandlebrot(z,c,0)
		#Color Choices
		rd = hex(r)[2:].zfill(2)
		gr = hex(55)[2:].zfill(2)
		bl = hex(245)[2:].zfill(2)
		img1.put("#" + rd + gr + bl, (col, row))
canvas1.pack()

#Picture 3
window2 = tkinter.Toplevel()
canvas2 = Canvas(window2, width = WIDTH, height = HEIGHT, bg = "#000000")
img2 = PhotoImage(width = WIDTH, height = HEIGHT)
canvas2.create_image((0, 0), image = img2, state = "normal", anchor = tkinter.NW)
for row in range(HEIGHT):
	for col in range(WIDTH):
		zx1 = (((xmax2-xmin2)*col)/WIDTH) + xmin2
		zy1 = (((ymax2-ymin2)*row)/HEIGHT) + ymin2
		c = complex(zx1,zy1)
		z = complex(0.0,0.0)
		#Execute the mandelbrot calculation
		r = mandlebrot(z,c,0)
		#Color Choices
		rd = hex(r)[2:].zfill(2)
		gr = hex(135)[2:].zfill(2)
		bl = hex(65)[2:].zfill(2)
		img2.put("#" + rd + gr + bl, (col, row))
canvas2.pack()
mainloop()
