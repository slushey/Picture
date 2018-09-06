"""
picture.py
Author: Alice Frederick
Credit: https://www.w3schools.com/colors/colors_picker.asp (HTML color picker) and http://brythonserver.github.io/ggame/#ggame.LineAsset

Assignment: Picture

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, LineAsset

# add your code here \/  \/  \/

#color pallette
yellow = Color(0xffff66, 1.0)
red = Color(0xff1a1a, 1.0)
black = Color(0x000000, 1.0)
brown = Color(0x994d00, 1.0)
pink = Color(0xffccdc, 1.0)
lightpink = Color(0xffe6ee, 1.0)
white = Color(0xffffff,1.0)

#lines used
line = LineStyle(0.2, pink)
line2 = LineStyle(0.2, brown)
line3 = LineStyle(0.2, black)
line4 = LineStyle(0.5,black)
line5 = LineStyle(0.2,white)
line6 = LineStyle(0.2,yellow)

#shapes used
rectangle = RectangleAsset(160, 10, line, pink)
rectangle2 = RectangleAsset(10, 160, line, pink)
rectangle3 = RectangleAsset(140, 140, line, lightpink)
face = CircleAsset(30, line2, yellow)
cheeks = CircleAsset(5, line2, red)
ears = PolygonAsset([(60,0), (40,7), (0,55),(53,20), (60,0)], line2, yellow)
ears2 = PolygonAsset([(0,0), (7,20), (60,55),(20,7), (0,0)], line2, yellow)
tip = PolygonAsset([(60,0), (40,7), (53, 20), (60,0)], line3, black)
tip2 = PolygonAsset([(0,0), (7,20), (20,7), (0,0)], line3, black)
mouth = LineAsset(3,0, line4)
mouth2 = PolygonAsset([(0,3), (3,0)], line4,black)
mouth3 = PolygonAsset([(0,0), (3,3)], line4,black)
nose = PolygonAsset([(0,0), (3,0), (1.5,1.5),(0,0)], line4,black)
eye = CircleAsset(4,line4,black)
shiny = CircleAsset(2.5,line2,white)
body = EllipseAsset(30,40, line2,yellow)
BOX = RectangleAsset(200,50,line5,white)
arm = EllipseAsset(5,15,line2,yellow)
box2 = RectangleAsset(10,10,line6,yellow)

#pikachu's body and the pink box
Sprite(rectangle3, (90,110))
Sprite(body, (130,190))
Sprite(rectangle, (80, 100))
Sprite(rectangle2, (80,100))
Sprite(rectangle, (80,250))
Sprite(rectangle2, (230,100))
Sprite(BOX, (80,260))

#pikachu
Sprite(ears, (160,125))
Sprite(ears2, (100,125))
Sprite(face, (130,150))
Sprite(cheeks, (135,180))
Sprite(cheeks, (175,180))
Sprite(tip, (200,125))
Sprite(tip2, (100,125))
Sprite(mouth, (152,195))
Sprite(mouth2,(155,191.5))
Sprite(mouth3,(157,191.5))
Sprite(mouth, (160,195))
Sprite(nose, (156, 186))
Sprite(eye, (142,170))
Sprite(eye,(171,170))
Sprite(shiny,(143.5,170))
Sprite(shiny,(171.5,170))
s = Sprite(arm, (140,215))
s.rotation = 0.3
g = Sprite(arm, (170,210))
g.rotation = -0.3
Sprite(box2,(140,210))
Sprite(box2,(170,210))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
