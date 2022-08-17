import requests
import json
import aiofiles
from PIL import Image, ImageDraw, ImageFont
from nonebot.log import logger
from pathlib import Path
import os
import cv2
from .config import *
from utils.http_utils import AsyncHttpx


async def addText(img, size, text, x, y, color=(255, 255, 255)):
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


async def isHasImg(path, url):
    if not os.path.lexists(path):
        img = await AsyncHttpx.get(url)
        if img.status_code == 200:
            with open(path, 'wb') as f:
                f.write(img.content)
                f.close()
                print(f"保存成功{path}")
            if path.rsplit(".", 1)[1] == "jpg":
                img = cv2.imread(path, 1)
                cv2.imwrite(path, img, [cv2.IMWRITE_JPEG_QUALITY, 30])
        else:
            return False
    else:
        print(f"已有{path}")
    return True


def loadEAIDJson():
    target_file = open(Bind_EAID_JSON, 'r+')
    try:
        QQ_EA = json.load(target_file)
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


def writeEAID(js):
    target_file = open(Bind_EAID_JSON, 'w+')
    json.dump(js, target_file)
    target_file.close()
    return


def isHasKey(key, dic):
    for d in dic:
        if key and d.lower() in key.lower():
            return True, dic[d]
    return False, ""


def ysImg(inPath):
    im = Image.open(inPath)
    (x, y) = im.size
    x_s = 1000
    y_s = int(y * x_s / x)
    out = im.resize((x_s, y_s))
    out.save(inPath)
