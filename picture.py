"""
picture.py
Author: Alice Frederick
Credit: https://www.w3schools.com/colors/colors_picker.asp (HTML color picker)

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
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/

#color pallette
yellow = Color(0xffff66, 1.0)
red = Color(0xff1a1a, 1.0)
black = Color(0x000000, 1.0)
brown = Color(0x994d00, 1.0)
pink = Color(0xffccdc, 1.0)
lightpink = Color(0xffe6ee, 1.0)

#lines used
line = LineStyle(0.2, pink)
line2 = LineStyle(0.2, brown)

#shapes used
rectangle = RectangleAsset(160, 10, line, pink)
rectangle2 = RectangleAsset(10, 160, line, pink)
rectangle3 = RectangleAsset(140, 140, line, lightpink)
face = CircleAsset(30, line2, yellow)
cheeks = CircleAsset(5, line2, red)
ears = PolygonAsset([(60,0), (7,20), (0,60),(20,7), (60,0)], line2, yellow)
ears2 = PolygonAsset([(60,55), (7,20), (0,0),(20,7), (60,55)], line2, yellow)

#stamp background and border
Sprite(rectangle, (80, 100))
Sprite(rectangle2, (80,100))
Sprite(rectangle, (80,250))
Sprite(rectangle2, (230,100))
Sprite(rectangle3, (90,110))

#pikachu
Sprite(ears)
Sprite(ears2, (100,125))
Sprite(face, (130,150))
Sprite(cheeks, (135,180))
Sprite(cheeks, (175,180))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
