from nonebot import on_command
from nonebot.typing import T_State
from nonebot.params import State, CommandArg, ArgStr
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, Message, Event
from services.log import logger
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from utils.http_utils import AsyncHttpx
import os
from .config import *
from .utils import *
import json
import requests
import cv2

__zx_plugin_name__ = "APEX查询工具"
__plugin_usage__ = """
usage：
    查询APEX地图轮换、制造机轮换、猎杀信息、玩家信息
    指令：
        a地图/a制造/a猎杀/a查询
""".strip()
__plugin_des__ = "查询APEX地图轮换、制造机轮换、猎杀信息、玩家信息"
__plugin_cmd__ = ["a地图", "a制造", "a猎杀"]
__plugin_version__ = 0.1
__plugin_author__ = "AreCie"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["a地图", "a制造", "a猎杀"],
}

apexdt = on_command("a地图", priority=5, block=True)
apexzz = on_command("a制造", priority=5, block=True)
apexls = on_command("a猎杀", priority=5, block=True)
apexcx = on_command("a查询", priority=5, block=True)
apexbind = on_command("a绑定", priority=5, block=True)


async def GetData(bot: Bot, url: str):
    resp = None
    isSucc = False
    try:
        resp = requests.post(url, timeout=(20, 5))
        code = resp.status_code
        if code == 200:
            isSucc = True
            logger.info(f'获取【{url}】数据成功')
        else:
            if code == 400 or code == 405:
                await bot.send("API出错啦，请稍后再试")
            if code == 403:
                await bot.send("API密钥错误，请重新配置")
            if code == 404:
                await bot.send("该玩家不存在")
            if code == 429:
                await bot.send("API查询频繁(目前每秒可请求2次)，再试一次吧")
            if code == 500:
                await bot.send("API内部错误(不是插件的锅!!!)")
    except Exception as e:
        await bot.send(f"API连接超时")
    return resp.text, isSucc


@apexdt.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    url = f"https://api.mozambiquehe.re/maprotation?auth={Tool_Token}&version=1"
    dataRet = await GetData(apexdt, url)
    if dataRet[1]:
        retdata = json.loads(dataRet[0])  # 地图数据
        tmpimgs = []
        selMap = ["battle_royale", "arenas", "ranked", "arenasRanked"]
        for data in selMap:
            dat = retdata[data]  # 当前游戏模式数据
            current = dat["current"]  # 当前地图
            nextmap = dat["next"]  # 下一地图

            isHasImg(f"{Map_Path}/{current['code']}.jpg", current["asset"])  # 当前地图图片

            im = Image.open(f"{Map_Path}/{current['code']}.jpg")
            x, y = im.size
            im = im.resize((960, 300), Image.ANTIALIAS)

            await addText(im, 50, GameMode_Dict[data], 20, 20)  # 地图类型
            await addText(im, 60, Map_Dict[current['code']] if current['code'] in Map_Dict else current['map'], 20,
                          90)  # 地图名称
            await addText(im, 30, f"剩余时间：{current['remainingTimer']}", 20, 170)
            await addText(im, 30,
                          f"下一轮换：{Map_Dict[nextmap['code']] if nextmap['code'] in Map_Dict else nextmap['map']}",
                          20, 220)

            tmpimg = f'{Temp_Path}/{data}_{current["code"]}.jpg'
            tmpimgs.append(tmpimg)
            im.save(tmpimg)

        # 设置画布(格式，尺寸，背景色)
        image = Image.new('RGB', (960, 1200), (255, 255, 255))
        for i, img in enumerate(tmpimgs):
            image.paste(Image.open(img), (0, i * 300))

        tmpMapPath = f"{Temp_Path}/map_ok.jpg"  # 地图路径
        logger.info(f"保存地图【{tmpMapPath}】")
        image.save(tmpMapPath)
        image_file = f"file:///{tmpMapPath}"

        msg = f"[CQ:image,file={image_file}]"
        try:
            logger.info(f"发送地图【{tmpMapPath}】")
            await bot.send_group_msg(group_id=event.group_id, message=msg)
        except Exception as e:
            await bot.send_group_msg(group_id=event.group_id, message=f"出错啦!\n错误信息：{e}")
            logger.info(e)


@apexzz.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    url = f"https://api.mozambiquehe.re/crafting?auth={Tool_Token}"
    dataRet = await GetData(apexdt, url)
    if dataRet[1]:
        retdata = json.loads(dataRet[0])  # 制造机数据
        zday = retdata[0]["bundleContent"]  # 每天轮换
        zwek = retdata[1]["bundleContent"]  # 每周轮换
        items = [zday[0]["itemType"], zday[1]["itemType"], zwek[0]["itemType"], zwek[1]["itemType"]]
        image = Image.new('RGB', (800, 800), (255, 255, 255))
        for i, item in enumerate(items):
            localImg = f"{Make_Path}/{item['name']}.jpg"
            isHasImg(localImg, item["asset"])
            im = Image.open(localImg)
            im = im.resize((400, 400), Image.ANTIALIAS)
            image.paste(im, (400 if bool(i & 1) else 0, 400 if i > 1 else 0))

        await addText(image, 50, "当日", 350, 345)
        await addText(image, 50, "本周", 350, 405)
        image.save(f"{Temp_Path}/mark_ok.jpg")
        image_file = f"file:///{Temp_Path}/mark_ok.jpg"
        msg = f"[CQ:image,file={image_file}]"
        try:
            await bot.send_group_msg(group_id=event.group_id, message=msg)
        except Exception as e:
            await bot.send_group_msg(group_id=event.group_id, message=f"出错啦!\n错误信息：{e}")
            logger.info(e)


@apexls.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    url = f"https://api.mozambiquehe.re/predator?auth={Tool_Token}"
    dataRet = await GetData(apexdt, url)
    if dataRet[1]:
        resp = json.loads(dataRet[0])
        try:
            ls = Image.open(f"{Template_Path}/ls.jpg")  # 加载模板
            for i, res in enumerate(resp):
                rank = resp[res]
                for j, ter in enumerate(rank):
                    terr = rank[ter]
                    lastRank = terr["foundRank"]
                    rankScore = terr["val"]
                    rankTotal = terr["totalMastersAndPreds"]
                    x, y = 60 if i == 0 else 430, 650 + (j * 300)
                    await addText(ls, 40, f"最低排名：{lastRank}", x, y)
                    await addText(ls, 40, f"排位分数：{rankScore}", x, y + 50)
                    await addText(ls, 40, f"大师总数：{rankTotal}", x, y + 100)
            ls = ls.convert('RGB')
            ls.save(f"{Temp_Path}/ls_ok.jpg")
            image_file = f"file:///{Temp_Path}/ls_ok.jpg"
            msg = f"[CQ:image,file={image_file}]"
            await bot.send_group_msg(group_id=event.group_id, message=msg)
        except Exception as e:
            await bot.send_group_msg(group_id=event.group_id, message=f"出错啦!\n错误信息：{e}")
            logger.info(e)


@apexbind.handle()
async def _(bot: Bot, event: Event, text: Message = CommandArg()):
    args = []
    if len(text) > 0:
        args = text[0].data['text'].split(' ')
    if len(args) < 1:
        await apexbind.send('绑定ID使用方式：[a绑定 烂橘子ID]')
        return

    EA_ID = args[0]
    url = f"https://api.mozambiquehe.re/bridge?auth={Tool_Token}&player={EA_ID}&platform=PC"
    dataRet = await GetData(apexdt, url)
    if dataRet[1]:
        try:
            QQ_EA = loadEAIDJson()
            QQ = event.get_user_id()
            QQ_EA[QQ] = EA_ID
            writeEAID(QQ_EA)
            await apexbind.send(f'成功将【{QQ}】与【{EA_ID}】绑定！')
        except Exception as e:
            await bot.send_group_msg(group_id=event.group_id, message=f"出错啦!\n错误信息：{e}")
            logger.info(e)


@apexcx.handle()
async def _(bot: Bot, event: Event, text: Message = CommandArg()):
    args = []
    uid = ""

    if len(text) > 0:
        args = text[0].data['text'].split(' ')

    if len(args) >= 1:
        uid = args[0]
    else:
        QQ = event.get_user_id()
        QQ_EA = loadEAIDJson()
        if QQ_EA.get(QQ) is None:
            await apexcx.send(f'{QQ}未绑定EA账号!如需绑定，请回复\na绑定 你的Origin_ID')
            return
        uid = QQ_EA[QQ]
    print(uid)
    url = f"https://api.mozambiquehe.re/bridge?auth={Tool_Token}&player={uid}&platform=PC"
    dataRet = await GetData(apexdt, url)
    if dataRet[1]:
        response = json.loads(dataRet[0])

        rankPimg = ""
        arenaPimg = ""
        img = Image.open(f"{Template_Path}/info.jpg")  # 信息页模板

        try:
            user = response["global"]  # 账号数据
            toNextLevelPercent = user["toNextLevelPercent"] / 100  # 经验进度比
            progressBar(img, (255, 255, 255), (130, 170, 0), 1100, 185, 300, 20, toNextLevelPercent)  # 添加进度条
            await addText(img, 60, user["name"] if user["name"] else uid, 1080, 63)  # 添加名字
            levWid = 780 if user["level"] >= 200 else 785 if user["level"] >= 100 else 790 if user[
                                                                                                  "level"] >= 10 else 795
            await addText(img, 32, str(user["level"] if user["level"] < 500 else 500), levWid, 216, (0, 0, 0))  # 添加等级
            for rk in range(2):
                rname = ["rank", "排位"] if rk == 1 else ["arena", "竞技场"]
                rank = user[rname[0]]
                rankName = rank["rankName"]
                rankDiv = rank["rankDiv"]
                rankImg = rank["rankImg"]

                rimgPath = f"{Rank_Path}/{rankName}{rankDiv}.png"
                isHasImg(rimgPath, rankImg)
                rimgdraw = Image.open(rimgPath).convert("RGBA")
                rimgdraw = rimgdraw.resize((250, 250), Image.ANTIALIAS)
                rimgdraw.save(rimgPath)

                if rk == 1:
                    rankPimg = rimgPath
                else:
                    arenaPimg = rimgPath
                ix, iy = (765, 600) if rk == 1 else (1200, 600)
                rankScore = rank["rankScore"]
                ladderPosPlatform = rank["ladderPosPlatform"]

                await addText(img, 40, f"{rname[1]}：{rankScore}", ix, iy)
                await addText(img, 40, f"猎杀排名：{str(ladderPosPlatform) if ladderPosPlatform > 0 else '无'}", ix, iy + 50)

            realtime = response["realtime"]
            await addText(img, 40, "当前状态：", 680, 900)
            await addText(img, 40, "在线" if realtime["isOnline"] else "离线", 900, 900)
            await addText(img, 40, "正在游戏" if realtime["isInGame"] else "未在游戏", 1070, 900)
            await addText(img, 40, "小队已满" if realtime["partyFull"] else "小队未满", 1300, 900)

            legends = response["legends"]["selected"]
            LegendName = legends["LegendName"]
            icon = legends["ImgAssets"]["icon"]
            iconPath = f"{Legend_Path}/{LegendName}.png"
            if not isHasImg(iconPath, icon):
                nopic = Image.open(f"{Template_Path}/nopic.png")
                await addText(nopic, 50, Legend_Dict[LegendName] if LegendName in Legend_Dict else LegendName, 230, 150,
                              (0, 0, 0))
                iconPath = f"{Temp_Path}/{LegendName}_nopic.png"
                nopic.save(iconPath)

            await addText(img, 60, Legend_Dict[LegendName] if LegendName in Legend_Dict else LegendName, 170, 33)
            lengData = legends["data"]
            for i, dat in enumerate(lengData):
                y = 120 + (i * 75)
                await addText(img, 30,
                              f"{isHasKey(dat['name'], Tracker)[1] if isHasKey(dat['name'], Tracker)[0] else dat['name']}：",
                              100, y)
                await addText(img, 30, str(dat["value"]), 500, y)

            icoPimgh = Image.open(iconPath).convert("RGBA")
            rankPimgh = Image.open(rankPimg).convert("RGBA")
            arenaPimgh = Image.open(arenaPimg).convert("RGBA")

            img.paste(rankPimgh, (760, 320), mask=rankPimgh)
            img.paste(arenaPimgh, (1200, 320), mask=arenaPimgh)
            img.paste(icoPimgh, (0, 270), mask=icoPimgh)
            img = img.convert('RGB')
            img.save(f"{Temp_Path}/{uid}_info.jpg")
            image_file = f"file:///{Temp_Path}/{uid}_info.jpg"
            msg = f"[CQ:image,file={image_file}]"
            await bot.send_group_msg(group_id=event.group_id, message=msg)
        except Exception as e:
            await bot.send_group_msg(group_id=event.group_id, message=f"出错啦!\n错误信息：{e}")
            logger.info(e)
