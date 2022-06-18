import requests
import json
import aiofiles
from PIL import Image, ImageDraw, ImageFont
from nonebot.log import logger
from pathlib import Path
import os
from .config import *


def addText(img, size, text, x, y, color=(255, 255, 255)):
    draw = ImageDraw.Draw(img)
    typeface = ImageFont.truetype(Font_Path, size)
    draw.text((x, y), text, font=typeface, fill=color)
    return draw


def progressBar(img, bgcolor, color, x, y, w, h, progress):
    drawObject = ImageDraw.Draw(img)

    '''BG'''
    drawObject.ellipse((x + w, y, x + h + w, y + h), fill=bgcolor)
    drawObject.ellipse((x, y, x + h, y + h), fill=bgcolor)
    drawObject.rectangle((x + (h / 2), y, x + w + (h / 2), y + h), fill=bgcolor)

    '''PROGRESS'''
    if (progress <= 0):
        progress = 0.01
    if (progress > 1):
        progress = 1
    w = w * progress
    drawObject.ellipse((x + w, y, x + h + w, y + h), fill=color)
    drawObject.ellipse((x, y, x + h, y + h), fill=color)
    drawObject.rectangle((x + (h / 2), y, x + w + (h / 2), y + h), fill=color)

    '''SAVE'''
    # im.save(imgPath)


def isHasImg(path, url):
    if not os.path.lexists(path):
        img = requests.get(url)
        if img.status_code == 200:
            with open(path, 'wb') as f:
                f.write(img.content)
                f.close()
                print(f"保存成功{path}")
        else:
            return False
    else:
        print(f"已有{path}")
    return True


def loadEAIDJson():
    target_file = open(Bind_EAID_JSON, 'r+')
    try:
        QQ_EA = json.load(target_file)
        print('load_sucess')
    except Exception as e:
        print(e)
        QQ_EA = {}
    target_file.close()
    return QQ_EA


def writeEAID(js):
    target_file = open(Bind_EAID_JSON, 'w+')
    json.dump(js, target_file)
    target_file.close()
    return


def isHasKey(key, dic):
    for d in dic:
        if d.lower() in key.lower():
            return True, dic[d]
    return False, ""
