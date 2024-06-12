import json
import requests
from tqdm import tqdm
from urllib.parse import urlparse
from utils import contain_str
origin_booksource = "./exportRssSource.json"

with open(origin_booksource, encoding="utf-8") as f:
    origin_dict = json.load(f)

check_list = [[], []]   # Grounp 域名
result = []
for item in tqdm(origin_dict):
    sourceGroup = item.get("sourceGroup","")
    sourceUrl = item["sourceUrl"]
    sourceName = item["sourceName"]
    tool_group = ["ai工具集", "工具", "⚙️工具", "图片", "ai", "AI", '✏️ 设计', '📱 资源', '〽️ 创意', '🌏 图文', '📥 下载']
    meiti_group =['🎶 音乐', '📻 音频']
    game_group =["游戏", "4399"]
    video_group =["📺 影视", '🎞️ 视频','🎬 大陆', '🎬 直播', '🎬 影视', "影视", "媒体"]
    soft_group = ["软件", "csdn"]
    zixun_group = ['🌐 新闻', '👻 异闻', '🛰️ 科技', "新闻"]
    chengren_group = ['18禁', '®免翻,18禁', '®免翻,18禁', "18", "美图", "🔞","特殊", "A姐", "MISSAV"]
    yuedu_group = ['legado', '📖 书源', '📚 书单', '1', "📮不似苏", "古诗", "⓪整合", "订阅" ]
    yuedu_name = ['legado', "书源", "知乎", "经"]
        
    if contain_str(sourceGroup, tool_group):
        item["sourceGroup"] = "⚙️ 工具"
    elif contain_str(sourceGroup, meiti_group):
        item["sourceGroup"] = '📻 媒体'
    elif contain_str(sourceGroup, game_group):
        item["sourceGroup"] = "🎲 娱乐"
    elif contain_str(sourceGroup, video_group):
        item["sourceGroup"] = "🎞️ 影视"
    elif contain_str(sourceGroup, soft_group):
        item["sourceGroup"] = "🗂️ 软件"
    elif contain_str(sourceGroup, zixun_group):
        item["sourceGroup"] = '📰 资讯'
    elif contain_str(sourceGroup, chengren_group):
        item["sourceGroup"] = '🎬 18禁'
    elif contain_str(sourceGroup, yuedu_group) or contain_str(sourceName, yuedu_name):
        item["sourceGroup"] = '📖 阅读'
    else:
        print("======sourceGroup:{}======sourceName:{}".format(sourceGroup, sourceName))
        item["sourceGroup"] = '💠 其他'

    domain = urlparse(sourceUrl).netloc
    if domain not in check_list[1]:
        check_list[1].append(domain)
    else:
        continue

    if sourceGroup not in check_list[0]:
        check_list[0].append(sourceGroup)
    sourceName_list = list(sourceName)

    for i in range(len(sourceName_list)):
        try:
            ch = sourceName_list[i]
            if '\u4e00' <= ch <= '\u9fff' or '0' <= ch <= '9' or 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                break
            sourceName_list= sourceName_list[i:]
        except Exception as e:
            print(e)
            print(sourceName)
            print(i)
    sourceName = "".join(sourceName_list)
    sourceName =sourceName.strip()
    item["sourceName"] = sourceName.replace(" ", "")

    result.append(item)
print(check_list[0])

with open(origin_booksource.replace("json","new.json"), encoding="utf-8", mode="w") as f:
    result = json.dump(result, f, ensure_ascii=False, indent=2)