# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 21:45:41 2021

@author: HP
"""
import random as rd

from PIL import Image
PATH = "Images/tableau.png"
WHITE, RED, BLUE,BLACK = (255,255,255), (255,0,0), (0,0,255), (0,0,0)
HEIGHT = 1

# IMAGE PREPROCESSING-------------------------------------------------------------------------------
#The precossing isn't over yet
def colorsLayout(image):
    newImage = image.copy()
    for j in range(newImage.height):
        for i in range(newImage.width):
            temp = newImage.getpixel((i,j))

            tol = 30
            if not ((WHITE[0] -tol <temp[0]<WHITE[0] + tol) and (WHITE[1] -tol <temp[1]<WHITE[1] + tol)
            and (WHITE[2] -tol <temp[2]<WHITE[2] + tol)): newImage.putpixel((i,j), BLACK)
    return newImage


def colorize(image): #just for fun
        pas = 5
        previousI, previousJ =0,0
        newImage = image.copy()
        for j in range(0,image.height,pas):
            for i in range(0,image.width,pas):
                i = min(image.width,i)
                j = min(image.height,j)
                red,green,blue = rd.randrange(0,255),rd.randrange(0,255),rd.randrange(0,255)
                for jj in range(previousJ, j+1):
                    for ii in range(previousI, i+1):
                        newImage.putpixel((ii,jj),(red,green,blue))
                previousI = i
            previousJ = j
        return newImage
# CALCULATING AREA UTILITIES-------------------------------------------------------------------------




def getStartingPoint(image):
    br = 0
    startingPoint = (0,0)
    for j in range(0, image.height):
        for i in range(0, image.width):
            temp = image.getpixel((i,j))
            if temp != WHITE:
                startingPoint = (i,j)
                br = 1
                break
        if br: break
    return startingPoint

def getUpBorders(image):
    '''Take an image path (shape of image with two colors) and return coordinates in pixels of the upper left and upper right of the shape as a list of tuple'''
    direction = [0,0]
    key = 0
    br = 0
    currentColor = WHITE  
    for j in range(0,image.height):
        for i in range(0,image.width):
            temp = image.getpixel((i,j))
            if temp != currentColor:
                direction[key] = (i-1*(key==1),j)
                currentColor = temp
                key += 1
                if key == 2:
                    br = 1
            if br: break
        if br: 
            break
    return direction

def cutVertically(image,upLeft=None,upRight=None, right = True, percent = 0.5):
    if upLeft==None or upRight==None:
        temp = getUpBorders(image)
        upLeft,upRight = temp[0], temp[1]
    middleX = int((-upLeft[0]+ upRight[0])*(percent) + upLeft[0]) +1
    for j in range(0,image.height):
        for i in range(0+middleX*(not right),middleX*(right) + image.width*( not right)):
            temp = image.getpixel((i,j))
            if temp != WHITE: image.putpixel((i,j),WHITE)
    return image 


def getHeight(image,isCut = False, startingPoint = None):
    pixels = 0
    if not isCut:
        image = cutVertically(image)
    if startingPoint == None: startingPoint = getStartingPoint(image)
    for i in range(startingPoint[1],image.height - startingPoint[1]):
        temp = image.getpixel((startingPoint[0], i))
        pixels +=1
        if temp == WHITE: 
            pixels -=1
            break
    return pixels 

def getWidth(image):
    temp = getUpBorders(image)
    return temp[1][0] - temp[0][0]

def getUnitFromHeight(image, heightInMeter,isCut = False, sp = None):
    heightPixels = getHeight(image,isCut = isCut, startingPoint = sp)
    return heightInMeter/heightPixels


def getPixels(image):
    pixels,edgePixels = 0,0
    startingPoint = getStartingPoint(image)
    directions = [(0,1),(1,0),(1,1),(-1,0),(0,-1),(-1,-1),(-1,1), (1,-1)]
    for j in range(startingPoint[1],image.height):
        for i in range(startingPoint[0], image.width):
            temp = image.getpixel((i,j))
            if temp!= WHITE:
                pixels +=1
                for dir in directions:
                    try:
                        coord = (i+dir[0],j+dir[1])
                        nearPixel = image.getpixel(coord)
                        if nearPixel == WHITE:
                            #Add it to the edge
                            #image.putpixel((i,j),RED) #To DEBUG only
                            edgePixels +=1
                            break
                    except Exception as ex : 
                        print(ex)
                        continue
    return pixels, edgePixels

def calculateArea(image):
    image = cutVertically(image)
    unit = getUnitFromHeight(image, 1, isCut = True)
    print(unit*unit)
    totalPixels = getPixels(image)[0]
    print(totalPixels)
    return totalPixels*unit*unit*2
    
with Image.open(PATH).convert('RGB') as image:
    #print("Area: {} m2".format(calculateArea(image)))
    #colorsLayout(image).show()
    image = colorize(image)
    image.show()
    image.save("Images/colorized.png")

                
                
                
                
                
                
                
                
                
                
                
                