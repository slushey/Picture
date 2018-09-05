"""
picture.py
Author: Alice Frederick
Credit: 

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

#line
line = LineStyle(0.2, black)

#box
rectangle = RectangleAsset(50, 10, line, pink)

# add your code here /\  /\  /\


myapp = App()
myapp.run()
