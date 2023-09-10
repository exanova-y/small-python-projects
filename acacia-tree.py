#set up
from tkinter import * 
from colorsys import hsv_to_rgb 
from random import randint
myWindow = Tk()


#function that changes hsv to hex, so I can use it for gradients
def hex(h, s, v):
	rgb = tuple(round(n*255) for n in hsv_to_rgb(h/360, s/100, v/100))
	return "#"+"%02x%02x%02x"% rgb

#start creating background
h = 330
s = 70
v = 40
screen = Canvas(myWindow, width=800, height=600, background= hex(h, s, v))
screen.pack()


#create sky gradients
x1 = 200
y1 = 0
x2 = 800
y2 = 600

for x in range(60):
	sky = hex(h, s, v)
	if h < 360:
		h = h+1
	else:
		h = 0
	s = s + 0.5
	v = v+1
	x1 = x1 + 6
	y1 = y1 + 4
	x2 = x2 - 3
	y2 = y2 - 5
	screen.create_oval(x1, y1, x2, y2, fill = sky,  outline = "")

#sun
d = 70
h = 35
for x in range(5):
	x1 = x1 + 2
	y1 = y1 + 2
	sun = hex(h, s, v)
	s = s - 20
	d = d - 4
	screen.create_oval(x1, y1, x1+d, y1+d, fill = sun, outline = "")


#birds
for x in range(5):
	x1 = randint(550, 720)
	y1 = randint(150, 400)
	x2 = x1 + randint(30, 40)
	y2 =  y1+ randint(15, 25)
	screen.create_arc(x1, y1, x2, y2,  style = ARC, width = 2)
	screen.create_arc(x2-2, y2+6, x1+2*(x2-x1)-10, y1, start = 60, style = ARC, width = 2)


#hills
screen.create_polygon(0, 500, 0, 435, 150, 437, 200, 435, 225, 445, 250, 450, 275, 455, 350, 460, 430, 465, 450, 500, fill = hex(351, 45, 65), smooth = "true")
screen.create_polygon(410, 500, 410, 470, 500, 437, 700, 440, 799, 445, 800, 500, fill = hex(335, 50, 50))


#far grass
h = 12
s = 76
v = 41
y = 470
for x in range(20):
	v = v-1
	y = y+2
	grass = hex(h, s, v)
	screen.create_line(0, y, 800, y, fill= grass, width = 2)


#tree

#left branches
screen.create_polygon(310, 500, 340, 475, 350, 400, 340, 375, 335, 360, 200,  275, 80, 240, 100, 240, 200, 255, 250, 280, 300, 315, 350, 340, 375, 375, 390, 455, 390, 475, 383, 500, fill = "black")
screen.create_line(170, 255, 145, 230, 175, 180, fill = "black", width = 7)
screen.create_line(150, 230, 110, 190, fill = "black", width = 5)
#left 2
screen.create_line(250, 290, 300, 240, 280, 220, 280, 200, 240, 155, fill = "black", width = 11)
#left 3
screen.create_line(350, 345, 340, 337, 330, 290, 340, 225, 340, 200, 380, 160, fill = "black", width = 9)
screen.create_line(340, 200, 310, 175, fill = "black", width = 6)


#right branches
screen.create_polygon(370, 370, 380, 360, 400, 320, 450, 280, 500, 260, 550, 230, 575, 210, 650, 185, 650, 190, 580, 220, 570, 230, 500, 273, 450, 300, 410, 330, 390, 375, 380, 400, 383, 410, fill = "black")
#right 1
screen.create_line(430, 310, 425, 240, 410, 225, 410, 210, 420, 215, 390, 165 ,fill = "black", width = 9)
screen.create_line(425, 250, 440, 240, 485, 230, 500, 220, 495, 200, 470, 185, 475, 155 ,fill = "black", width = 7)
#right 2
screen.create_line(540, 240, 550, 190, 530, 180, 537, 165, 580, 135,fill = "black", width = 7)
screen.create_line(537, 165, 500, 150 ,fill = "black", width = 5)
#right3
screen.create_line(615, 200, 625, 175, fill = "black", width = 5)
#broken branch
screen.create_rectangle(395, 305, 405, 330, fill = "black")


#close grass
h = 16
s = 81
v = 20
for y in range(500, 600):
        screen.create_line(0, y, 800, y, fill = hex(h, s, v))
        v = v - 0.15


#leaves, grouped
def leaves(x1, x2, y1, y2):
        area = round(((y2-y1)*(x2-x1))/25)
        for n in range(area):
                x = randint(x1, x2)
                y = randint(y1, y2)
                v1 = randint(-10, 20)
                v2 = randint(-10, 20)
                screen.create_polygon(x, y, x+v1, y+v1, x+v2, y+v1, fill = "black")

leaves(40, 175, 140, 250)
leaves(15, 225, 130, 230)
leaves(100, 250, 70, 200)
leaves(175, 365, 50, 165)
leaves(300, 400, 70, 170)
leaves(400, 480, 110, 160)
leaves(480, 580, 75, 190)
leaves(575, 670, 87, 225)
leaves(530, 730, 110, 210)


#kid, left
screen.create_oval(540, 437, 555, 455, fill = "black")
screen.create_polygon(550, 460, 547, 460, 550, 460, 555, 467, 550, 467, 540, 490, 545, 501, 540, 525, 553, 530, 535, 530, 535, 520, 540, 510, 533, 503, 530, 505, 510, 495, 500, 505, 500, 497, 505, 490, 515, 495, 530, 495, 525, 480, 535, 475, 537, 470, 530, 470, 525, 460,540, 455, 542, 450, fill = "black", smooth ="true")
screen.create_polygon(515,475, 517,469, 530,460, 535,463, fill ="black")
screen.create_polygon(547,467, 560,485, 563,487, 553,467, fill = "black")

#kid, right
screen.create_oval(490, 433, 505, 451, fill = "black")
screen.create_polygon(495, 450, 500,455, 497,470, 495,473, 490,470, 490,465, 489,463, 485,475, 480,490, 460,507, 470,515, 460,517, 455,510, 470,490, 470,485, 460,483, 455,487, 453,485, 455,475, 460,480, 470,480, 465,475, 478,455, 460,453, 460,447, 475,445, 480,447, 490,445, fill = "black")  
screen.create_polygon(480,475, 485,490, 470,493, fill = "black")
screen.create_polygon(460,455, 447,458, 450,454, 460,450, fill = "black")

#date
screen.create_text(760, 590, fill ="white", font = "Times 10", text = "June 2020")
screen.mainloop()

#Picture inspired by Afrikaans song "Doringboom". Created by Yoyo Yuan