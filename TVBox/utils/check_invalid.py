import json
import requests
import random
from tqdm import tqdm
from urllib.parse import urlparse
from utils import check_site_is_online, emoji_list
origi_source = r"E:\Study\Code\OpenSourceRSS\TVBox\main.json"

with open(origi_source, encoding="utf-8") as f:
    origin_dict = json.load(f)

result = []
for item in tqdm(origin_dict["urls"]):
    url = item["url"]
    if not check_site_is_online(url):
        continue
    name = item["name"]
    if "饭太硬" in name or "肥猫" in name:
        result.append(item)
        continue 
    name_list =list(name)
    for index in range(len(name_list)):
        ch = name_list[index]
        if '\u4e00' <= ch <= '\u9fff' or 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            break
        name = random.choice(emoji_list)+" "+"".join(name_list[index:]).strip()
        item["name"]=name
    result.append(item)
    
with open(origi_source.replace("json","new.json"), encoding="utf-8", mode="w") as f:
    result = json.dump(result, f, ensure_ascii=False, indent=2)
