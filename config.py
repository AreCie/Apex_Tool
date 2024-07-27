import os

# API Token
Tool_Token = ""

# 此插件根目录
Tool_Path = os.path.dirname(__file__)
# 此插件资源目录
Tool_Assets_Path = f"{Tool_Path}/Assets"
# QQ绑定的EAID的Json文件路径
Bind_EAID_JSON = f"{Tool_Path}/Assets/QQ_EA_ID.json"
# EAID的RankJson文件路径
Rank_JSON = f"{Tool_Path}/Assets/Rank_Data.json"
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
    "kings_canyon_rotation": "诸王峡谷",
    "arenas_phase_runner": "相位穿梭器",
    "broken_moon_rotation": "破碎月球",
    "freedm_tdm_habitat": "栖息地(团队竞技)",
    "freedm_swat_habitat": "栖息地(死亡之眼-无护盾)",
    "control_canyonlands_caustic": "诸王峡谷(控制)",
    "control_tropics_barometer": "晴雨表(控制)",
    "freedm_tdm_skulltown": "骷髅镇(团队竞技)",
    "freedm_gungame_wall": "高墙(枪王)",
    "control_desertlands_siphon": "熔岩虹吸(枪王)",
    "freedm_tdm_overflow": "熔岩流(团队竞技)",
    "freedm_swat_overflow": "熔岩流(死亡之眼-无护盾)",
    "freedm_gungame_skulltown": "骷髅镇(子弹时间)",
    "freedm_gungame_estates": "不动产(子弹时间)",
    "freedm_tdm_phase_runner": "相位穿梭器(团队死斗)",
    "freedm_swat_phase_runner": "相位穿梭器(死亡之眼-无护盾)",
}

# 游戏模式对照
GameMode_Dict = {
    "battle_royale": "匹配",
    "arenas": "竞技场",
    "ranked": "排位",
    "arenasRanked": "竞技场排位",
    "control": "控制",
    "freenom": "枪王模式",
    "ltm": "娱乐模式",
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
    "Vantage": "万蒂奇",
    "Catalyst": "卡特莉丝",
    "Ballistic": "弹道",
    "Conduit": "导线管",
    "Alter": "变换",
}

# 追踪器对照
Tracker = {
    # 赛季
    "BR Season 15 kills": "第15赛季Apex击杀数",
    "BR Season 15 wins": "第15赛季Apex胜场数",
    "BR Season 14 kills": "第14赛季Apex击杀数",
    "BR Season 14 wins": "第14赛季Apex胜场数",
    "BR Season 13 kills": "第13赛季Apex击杀数",
    "BR Season 13 wins": "第13赛季Apex胜场数",
    "BR Season 12 kills": "第12赛季Apex击杀数",
    "BR Season 12 wins": "第12赛季Apex胜场数",
    "BR Season 11 kills": "第11赛季Apex击杀数",
    "BR Season 11 wins": "第11赛季Apex胜场数",
    "BR Season 10 kills": "第10赛季Apex击杀数",
    "BR Season 10 wins": "第10赛季Apex胜场数",
    "BR Season 9 kills": "第9赛季Apex击杀数",
    "BR Season 9 wins": "第9赛季Apex胜场数",
    "BR Season 8 kills": "第8赛季Apex击杀数",
    "BR Season 8 wins": "第8赛季Apex胜场数",
    "BR Season 7 kills": "第7赛季Apex击杀数",
    "BR Season 7 wins": "第7赛季Apex胜场数",
    "BR Season 6 kills": "第6赛季Apex击杀数",
    "BR Season 6 wins": "第6赛季Apex胜场数",
    "BR Season 5 kills": "第5赛季Apex击杀数",
    "BR Season 5 wins": "第5赛季Apex胜场数",
    "BR Season 4 kills": "第4赛季Apex击杀数",
    "BR Season 4 wins": "第4赛季Apex胜场数",
    "BR Season 3 kills": "第3赛季Apex击杀数",
    "BR Season 3 wins": "第3赛季Apex胜场数",
    "BR Season 2 kills": "第2赛季Apex击杀数",
    "BR Season 2 wins": "第2赛季Apex胜场数",
    "BR Season 1 kills": "第1赛季Apex击杀数",
    "BR Season 1 wins": "第1赛季Apex胜场数",

    # 通用
    "Scout of Action": "侦察行动",
    "Smoke Show": "烟幕表演",
    "Jackson's Bow Out": "杰克逊的谢幕",
    "Arenas Wins": "竞技场获胜数",
    "Arenas Kills": "竞技场击杀数",
    "Arenas Damage": "竞技场模式伤害",
    "BR Special event wins": "Apex获胜数",
    "BR Special event damage": "Apex伤害数",
    "BR Special event kills": "Apex击杀数",
    "BR Kills": "Apex击杀数",
    "BR Damage": "Apex伤害",
    "BR Wins": "Apex胜场数",
    "BR Executions": "Apex终结数",
    "BR Kills as Kill Leader": "作为击杀王的Apex击杀数",
    "BR Headshots": "Apex爆头数",
    "BR Finishers": "Apex终结技次数",
    "BR Revives": "Apex急救次数",
    "BR Games Played": "Apex已进行的游戏",
    "BR Wins with Full Squad Alive": "小队无人阵亡获得的Apex胜场数",
    "BR Top 3": "排名前3的Apex次数",
    "BR AR kills": "Apex突击步枪击杀数",
    "BR LMG kills": "Apex轻机枪击杀数",
    "BR Marksman kills": "Apex神射手击杀数",
    "BR Pistol kills": "Apex手枪击杀数",
    "BR Shotgun kills": "Apex霰弹枪击杀数",
    "BR SMG kills": "Apex冲锋枪击杀数",
    "BR Sniper kills": "Apex狙击枪击杀数",
    "BR Care Package Weapon kills": "Apex补给仓武器击杀数",

    # 寻血猎犬
    "Eye: Enemies Scanned": "发现-扫描到敌人",
    "Eye: Traps Scanned": "发现-扫描到陷阱",
    "Beast of the Hunt: Kills": "狂野猎人-击杀数",

    # 直布罗陀
    "Dome: Damage Blocked": "穹顶-阻挡的伤害",
    "Bombardment: Kills": "轰炸-击杀数",
    "GunShield: Damage Blocked": "枪盾-阻挡的伤害",

    # 命脉
    "D.O.C. Drone: Squadmates Revived": "D.O.C无人机-已复活小队成员",
    "D.O.C. Drone: Healing": "D.O.C无人机-治疗量",
    "Droppod: Items for Squadmates": "降落仓-小队成员获得的物品",

    # 探路者
    "Grapple: Travel Distance": "抓钩-移动距离",
    "Zipline: Times used by Squad": "滑索-小队使用次数",
    "Survey: Beacons Scanned": "侦察-扫描信标数",

    # 恶灵
    "Voices: Warnings Heard": "声音-听到的警告次数",
    "Into the void: Time": "踏入虚空-时间",
    "Rifts: Squadmates Phased": "裂隙-相位移动的小队成员",

    # 班加罗尔
    "Double Time: Distance": "双倍时间-距离",
    "Smoke Grenade: Enemies Hit": "烟雾弹-击中的敌人",
    "Rolling Thunder: Damage": "雷声滚滚-伤害",

    # 侵蚀
    "Gas Trap: Times Activated": "毒气陷阱-触发次数",
    "NOX: Gas Damage Dealt": "NOX-毒气造成的伤害",
    "NOX: Gassed Enemies Killed": "NOX-毒气的击杀数",

    # 幻象
    "Encore: Executions Escaped": "再来一次-逃脱处决次数",
    "Decoys Created": "制造诱饵",
    "Bamboozles": "骗术成功次数",

    # 动力小子
    "Stim Distance Traveled": "兴奋剂移动距离",
    "Jump Pad Allies Launched": "跳板发射队友",
    "Passive Health Regenerated": "被动恢复生命值",

    # 沃特森
    "Breaches Detected": "检测到违规",
    "Friendly Shields Charged": "友方护盾已充能",
    "Enemy Ordnance Intercepted": "已拦截敌方轰炸火力",

    # 密客
    "Neurolink: Enemies Scanned": "神经连接-扫描到敌人",
    "Drone EMP: Shield Damage": "无人机 电子脉冲-护盾伤害",
    "Drone EMP: Devices Hit": "无人机 电子脉冲-设备命中",

    # 亡灵
    "Silence: Enemies Silenced": "静默-被静默的敌人",
    "Silence: Silenced Knockdowns": "静默-静默击倒",
    "Death Totem: Activations": "死亡图腾-激活",

    # 罗芭
    "Loot Pinged Through Walls": "透过墙壁标记的战利品数",
    "Meters Teleported": "传送距离",
    "Loot Taken by Allies": "队友拿到的战利品数",

    # 兰伯特
    "Wall: Bullets Amped": "墙体-强化子弹",
    "Wall: Damage Blocked": "墙体-阻挡伤害",
    "Turret: Bullets Fired": "炮台-发射子弹",

    # 地平线
    "Spacewalk: Impacts Avoided": "太空漫步-避免猛烈冲击",
    "Gravity Lift: Teammates Lifted": "重力电梯-承载过的队友",
    "Black Hole: Damage Done": "大逃杀 黑洞-伤害",

    # 暴雷
    "Grenades: Distance Thrown": "手雷-远距离投掷",
    "Knuckle Cluster: Total Hits": "集束炸弹-总命中次数",
    "Motherload: Enemies Captured": "广域轰炸-捕获敌人数",

    # 瓦尔基里
    "VTOL Jets: Distance Travelled": "垂直起降喷射器-移动距离累计",
    "Missile Swarm: Enemies Hit": "飞弹流星-击中的敌人数量",
    "Skyward Dive: Allies Repositioned": "天际俯冲-移动队友次数",

    # 希尔
    "Heart Seeker: Heartbeats Heard": "觅心者-已听到心跳数",
    "Focus of Attention: Enemies Hit": "聚焦之眼-击中的敌人",
    "Exhibit: Enemies Tracked": "一览无余-追踪到的敌人",

    # 艾许
    "Marked for Death: Enemies Marked": "死亡印记-标记敌人",
    "Arc Snare: Enemies Tethered": "电弧陷阱-绊索敌人",
    "Phase Breach: Players Phased": "相位突破-已传送玩家",

    # 疯玛吉
    "Warlord's Ire: Highlight Time": "战争领主之怒-高亮时间",
    "Riot Drill: Drill Distance": "暴乱训练-训练距离",
    "Wrecking Ball: Boosted Travel Distance": "破坏球-提升移动距离",

    # 纽卡斯尔
    "Retrieve the Wounded: Revive Distance": "救助伤员-急救距离",
    "Mobile Shield: Damage Blocked": "机动护盾-阻挡的伤害",
    "Castle Wall: Allies Rescued": "护城铁壁-救援的盟友",
}
