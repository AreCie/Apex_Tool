import os

# API Token
Tool_Token = "把我替换掉"

# 此插件根目录
Tool_Path = os.path.dirname(__file__)
# 此插件资源目录
Tool_Assets_Path = f"{Tool_Path}/Assets"
# QQ绑定的EAID的Json文件路径
Bind_EAID_JSON = f"{Tool_Path}/Assets/QQ_EA_ID.json"
# 字体文件路径
Font_Path = f"{Tool_Assets_Path}/Font.ttf"
# 地图图片资源目录
Map_Path = f"{Tool_Assets_Path}/Map"
# 制造器图片资源目录
Make_Path = f"{Tool_Assets_Path}/Make"
# 段位图片资源目录
Rank_Path = f"{Tool_Assets_Path}/Rank"
# 传奇图片资源目录
Legend_Path = f"{Tool_Assets_Path}/Legend"
# 模板图片资源目录
Template_Path = f"{Tool_Assets_Path}/Template"
# 临时资源目录
Temp_Path = f"{Tool_Assets_Path}/Temp"

# 地图名称对照
Map_Dict = {
    "worlds_edge_rotation": "世界尽头",
    "storm_point_rotation": "风暴点",
    "arenas_encore": "再来一次",
    "arenas_party_crasher": "派对破坏者",
    "caustic_tt_rotation": "毒气室",
    "hammond_labs_rotation": "哈蒙德实验室",
    "olympus_rotation": "奥林匹斯",
    "arenas_composite": "原料厂",
    "arenas_overflow": "熔岩流",
    "arenas_habitat": "栖息地4",
}

# 游戏模式对照
GameMode_Dict = {
    "battle_royale": "匹配",
    "arenas": "竞技场",
    "ranked": "排位",
    "arenasRanked": "竞技场排位",
    "control": "控制",
}

# 传奇名字对照
Legend_Dict = {
    "Revenant": "亡灵",
    "Crypto": "密客",
    "Horizon": "地平线",
    "Gibraltar": "直布罗陀",
    "Wattson": "华森",
    "Fuse": "暴雷",
    "Bangalore": "班加罗尔",
    "Wraith": "恶灵",
    "Octane": "动力小子",
    "Bloodhound": "寻血猎犬",
    "Caustic": "侵蚀",
    "Lifeline": "命脉",
    "Pathfinder": "探路者",
    "Loba": "罗芭",
    "Mirage": "幻象",
    "Rampart": "兰伯特",
    "Valkyrie": "瓦尔基里",
    "Seer": "希尔",
    "Ash": "艾许",
    "Mad Maggie": "疯玛吉",
    "Newcastle": "纽卡斯尔",
}
