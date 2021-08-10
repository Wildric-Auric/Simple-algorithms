#This script was created for the automatization of dowloads of berserk from Mangakalot

from selenium import webdriver
from time import sleep
import os
from win32com.client import Dispatch
from pynput.keyboard import Key, Controller
from shutil import copyfile

keyboard = Controller()

def shortCut(hold, press, wait = 0.2, wait1 = 0.2):
    
    keyboard.press(hold)
    sleep(wait)
    keyboard.press(press)
    sleep(wait1)
    keyboard.release(hold)
    keyboard.release(press)
    
def pressRelease(key, wait = 0.1):
    keyboard.press(key)
    sleep(wait)
    keyboard.release(key)
    
    

PATH = r"C:\Program Files (x86)\chromedriver.exe"
SAVEPATH = r"C:\Users\HP\Downloads"
PLAYLIST = r"C:\Users\HP\Downloads\Playlist"
browser = webdriver.Chrome(PATH)

start, end = 329, 345


def savePage(browser,adress):
    browser.get(adress)
    sleep(2)
    shortCut(Key.ctrl, 's')
    sleep(0.6)
    pressRelease(Key.enter)
    
def saveMany(browser,start,end):
    filesNum = len(os.listdir(SAVEPATH))
    for i in range(start, end+1):
        savePage("https://readmanganato.com/manga-ma952557/chapter-" +str(i))
        while (len(os.listdir(SAVEPATH)) != filesNum +2):
            pass
        else: filesNum +=2
        sleep(0.2)


def createPlaylist(path):
    order = 1
    #shell = Dispatch("WScript.Shell") As you will see after I first attempted to create shortcuts in the playlist folder but a shortcut in it's definition lead you to the file in it's the original directory which I don't want 
    allFolders = os.listdir(SAVEPATH)
    for folder in allFolders:
        if  os.path.isdir(os.path.join(SAVEPATH,folder)):
            newGlobalPath = os.path.join(SAVEPATH, folder)
            allImages = os.listdir(newGlobalPath)
            for image in allImages:
                if ((".jpg" in image) or (".png" in image)) and image.split(".")[0].isdigit():
                        # shortCut = shell.CreateShortcut(os.path.join(os.path.join(SAVEPATH, "Playlist"),str(order) + ".lnk"))
                        # shortCut.Targetpath = os.path.join(newGlobalPath, image)
                        # shortCut.IconLocation = os.path.join(newGlobalPath, image)
                        # shortCut.save()
                        src = os.path.join(newGlobalPath, image)
                        copyfile(src, os.path.join(PLAYLIST,str(order) + ".jpg"))
                        order += 1
    print("PLAYLIST CREATED SUCCESSFULLY, ENJOY!")
            

createPlaylist(PLAYLIST)