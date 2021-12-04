import PIL
from numpy import exp
WIDTH =  500
HEIGHT = 500
CENTER = (WIDTH//2, HEIGHT//2)
RADIUS = 100
MAXT = 255
OVEREXPOSURE = 255
SQUAREMODE = 1
EXPMODE = 1
#EXPMUL = 2
maxDistance = 100

img = PIL.Image.new("RGBA",(WIDTH,HEIGHT), (0,0,0,0))
color = [255,255,255]
data=[]
for x in range(WIDTH):
    for y in range(HEIGHT):
        f = ((x - CENTER[0])**2 + (y - CENTER[1])**2)**0.5
        distance = max((  min(f,RADIUS), 0.001))
        disPercent = max(1.0 - distance/RADIUS, 0);
        if not EXPMODE:
            formula = MAXT*(( disPercent)**(SQUAREMODE))
        else:
            formula = MAXT*(exp(1-1/(max(disPercent*disPercent,0.01))))
            
        transparency = min(OVEREXPOSURE,max(formula, 0))
        data.append(tuple(color[::]+[int(transparency)]))
        
img.putdata(data)
img.save('test6.png', "PNG")
