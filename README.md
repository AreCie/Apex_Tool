[![OSCS Status](https://www.oscs1024.com/platform/badge/AreCie/Apex_Tool.svg?size=large)](https://www.oscs1024.com/project/AreCie/Apex_Tool?ref=badge_large)
# Apex_Tool  APEX英雄QQBot信息查询
 适用于[绪山真寻Bot](https://github.com/HibiKier/zhenxun_bot) ，``nonebot2``使用的话，需要稍加更改，可以参考这个[nonebot2 中使用该插件](https://github.com/AreCie/Apex_Tool/issues/9#issuecomment-1218910846)

# 更新日志

### 2022/10/06  v1.5.0
完善帮助文档，非首次安装用户，需删除真寻Bot``/data/configs``目录下``plugins2settings.yaml``文件中该查询的配置``Apex_Tool``

帮助命令使用：艾特你的Bot，然后``帮助 [派派, 派, Apex, apex, APEX]``，中括号中任意一个即可，或者使用``派帮助/派命令/a帮助/a命令``其中任意一个即可

### 2022/09/25  v1.4.0
增加对`没有找到玩家信息/烂橘子ID错误`时的判断，增长请求数据的超时时间

### 2022/09/02  v1.3.0
增加对私聊的支持

### 2022/08/18  v1.2.0
优化代码，去除无用的依赖，去除有问题的状态码判断(官方文档提供的状态码和说明有偏差，索性直接去掉判断)，调整说明文档

### 2022/08/17  v1.1.0
修复使用代理时造成的错误

### 2022/08/16  v1.0.0
优化代码逻辑，对图片进行压缩，提升处理、响应速度，部分追踪器汉化修正。

# 关于追踪器汉化
追踪器汉化只是试验阶段，如果有不正确或者未显示汉化的，及时提出，谢谢。
 
# 关于图片资源
所用到的图片素材都是下载自接口，因为接口是国外的，所以国内部署的QQBot使用的话，下载会很慢，具体表现为查询时等待时间过长，但第二次同样内容的查询会比之前快很多。

所以为了提高体验效果，我这里提供了部分处理好的图片素材，用的你们最爱的蓝奏云，下载后直接覆盖到Assets文件夹里即可。

下载地址：[点我下载](https://wws.lanzoub.com/i5KER0bn0oih)

# 目前功能及对应命令
 **查询地图轮换**：【a地图】

 **查询制造轮换**：【a制造】
 
 **查询猎杀信息**：【a猎杀】
 
 **绑定烂橘子ID**：【a绑定 烂橘子ID】
 
 **查询玩家信息**：【a查询】(这个需先绑定烂橘子ID)、【a查询 烂橘子ID】
 
# 功能展示
 ![JP $79QF_IG{INTWPY7KWVG](https://user-images.githubusercontent.com/41849402/170845769-6cf5141b-7e79-412a-86ad-391464ac16e7.png)
![O_GMHBEG5{QW{0$GA@IS9SI](https://user-images.githubusercontent.com/41849402/170845801-e0ddc0d3-f44b-4aa6-b51b-1e21d7be7653.png)
![4(O6QJ~8C@V3T3{B3}RL )W](https://user-images.githubusercontent.com/41849402/170845803-421213e7-5f48-42c8-8afd-faddf933160b.png)
![RG7{{~%DV~SAJD`})EUJ{RB](https://user-images.githubusercontent.com/41849402/170845806-c37feb98-88c8-42c7-98df-499d7841fa80.png)
![UGH P~HG}3`CI0_ V8G})K5](https://user-images.githubusercontent.com/41849402/170845810-e8c5016f-a49b-443f-80c5-c839cbafcd8e.png)
![O@H%0E}Y8A%ML @{HTT)RQN](https://user-images.githubusercontent.com/41849402/170845813-09872adb-3458-41fc-b854-e441e943e030.png)

# 使用方法
1、先将该插件下载下来,将文件夹名字改为【Apex_Tool】

2、访问这个网站 https://portal.apexlegendsapi.com/ 获取token

3、打开该插件中的【config.py】文件

4、将步骤2获取的token填入到【Tool_Token】字段中

5、将改好的插件放到[绪山真寻Bot](https://github.com/HibiKier/zhenxun_bot)的【plugins】文件夹下

6、在虚拟环境下安装该插件的依赖文件【requirements.txt】，安装方法：

```shell
pip install -r [插件路径]/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

也可以直接用下面这条命令安装：
```shell
pip install opencv_python Pillow -i https://pypi.tuna.tsinghua.edu.cn/simple
```

主要就是安装两个依赖：```opencv-python #cv2```、```Pillow #PIL```

(```opencv-python #cv2```安装``真寻Bot``时在安装依赖那步好像有安装，不太确定。)


6、重启[绪山真寻Bot](https://github.com/HibiKier/zhenxun_bot)即可

帮助命令使用：艾特你的Bot，然后``帮助 [派派, 派, Apex, apex, APEX]``，中括号中任意一个即可，或者使用``派帮助/派命令/a帮助/a命令``其中任意一个即可

注意: 文件夹的名字一定要是【Apex_Tool】
# 题外话
因本人主修C#，Python只有自学的程度，某些地方写的可能没那么完美，有能力的可以自己优化下，就这样
