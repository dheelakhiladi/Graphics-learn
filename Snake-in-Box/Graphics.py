from numpy    import *
from graphics import *
from turtle   import *
from math	  import *
win= GraphWin(width=1000,height=1000)#win = GraphWin(width = 200, height = 200) # create a window
#win.setCoords(0, 0, 100, 100) # set the coordinates of the window; bottom left is (0, 0) and top right is (10, 10)
pt=Point(100,100)
pt1=Point(200,200)
pt2=Point(150,150)
pt3=Point(250,250)
rec1 = Rectangle(pt,pt1) # create a rectangle from (1, 1) to (9, 9)
rec1.draw(win) # draw it to the window
rec2=Rectangle(pt2,pt3)
rec2.draw(win)
line1=Line(pt,pt2)
line1.draw(win)
line2=Line(Point(200,100),Point(250,150))
line2.draw(win)
line3=Line(Point(200,200),Point(250,250))
line3.draw(win)
line4=Line(Point(100,200),Point(150,250))
line4.draw(win)
a=0
line5=Line(Point(125,175),Point(225,175))
line5.draw(win)
#for i in arange(124,226,0.7):
#	j = 10*sin(a)
#	y=175-j
#	p= Point(i,y)
#	p.draw(win)
#	for x in xrange(1,1000000):
#		pass
#	a=a+1
#	print i,'	=	',a,'	=	',y
#y=sin(2)
#print y
j=0
a=[0,pi/2,pi,3*pi/2,2*pi]
for i in arange(124,226,5):
	pt11=Point(i,175-(10*sin(a[j%5])))
	pt12=Point(i,175-(10*sin(a[j%5])))
	pt13=Point(i,175-(10*sin(a[j%5])))
	pt14=Point(i,175-(10*sin(a[j%5])))
	pt15=Point(i,175-(10*sin(a[j%5])))
	line11=Line(pt11,pt12)
	line11.draw(win)
	line12=Line(pt12,pt13)
	line12.draw(win)
	line13=Line(pt13,pt14)
	line13.draw(win)
	line14=Line(pt14,pt15)
	line14.draw(win)
	j=j+1

win.getMouse() # pause before closing