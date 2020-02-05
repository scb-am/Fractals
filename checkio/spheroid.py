import math


# def checkio(height, width):
#     if width > height:
#         V = 4 / 3 * math.pi * ((width/2)**2) * (height/2)
#         e = math.sqrt(1 - height**2 / width**2)
#         S = 0.5 * math.pi * (width**2) * (1 + (1-e**2)/e * math.atanh(e))
#     elif width < height:
#         V = 4 / 3 * math.pi * ((width / 2) ** 2) * (height / 2)
#         e = math.sqrt(1 - width ** 2 / height ** 2)
#         S = 0.5 * math.pi * (width**2) * (1 + (height / width / e * math.asin(e)))
#     else:
#         V = 4 / 3 * math.pi * ((width/2)**3)
#         S = 4 * math.pi * ((width / 2) ** 2)
#     print(f'V - {round(V, 2)}, S - {round(S, 2)}')


checkio=lambda height,width:{
    width>height:(lambda x,y:[
        round(4/3*math.pi*((x/2)**2)*(y/2),2),
        round((lambda x,e:0.5*math.pi*(x**2)*(1+(1-e**2)/e*math.atanh(e)))(x,math.sqrt(1-y**2/x**2)),2)
    ] if x>y else False)(width,height),
    width<height:(lambda x,y:[
        round(4/3*math.pi*((x/2)**2)*(y/2),2),
        round((lambda x, y, e:0.5*math.pi*(x**2)*(1+(y/x/e*math.asin(e))))(x,y,(math.sqrt(1-width**2/height**2))),2)
    ] if x<y else False)(width,height),
    width==height:(lambda x:[
        round(4/3*math.pi*((x/2)**3),2),
        round(4*math.pi*((x/2)**2),2)
    ])(width)
}[True]

# Using formulas from http://en.wikipedia.org/wiki/Spheroid

# from math import pi, asin, atanh
#
#
# def checkio(height, width):
#     """
#     Calculate the volume and the surface area for the spheroid.
#
#     Args:
#         height: spheroid's height.
#         width: spheroid's width.
#     Returns:
#         the list with the volume and the surface area. Rounded at two digits.
#     """
#     a, c = width / 2, height / 2
#     volume = (4 / 3) * pi * c * (a ** 2)
#
#     # prolate
#     if a < c:
#         e = (1 - a ** 2 / c ** 2) ** 0.5
#         area = 2 * pi * a ** 2 * (1 + asin(e) * c / (a * e))
#     # oblate
#     elif a > c:
#         e = (1 - c ** 2 / a ** 2) ** 0.5
#         area = 2 * pi * a ** 2 * (1 + atanh(e) * (1 - e ** 2) / e)
#     # sphere
#     else:
#         area = 4 * pi * a ** 2
#
#     return [round(volume, 2), round(area, 2)]


print(checkio(4, 2))
print(checkio(2, 2))
print(checkio(2, 4))
