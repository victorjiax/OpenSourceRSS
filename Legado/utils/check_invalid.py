import json
import requests
from tqdm import tqdm
from urllib.parse import urlparse
from utils import contain_str
origin_booksource = "./bookSource.json"

with open(origin_booksource, encoding="utf-8") as f:
    origin_dict = json.load(f)

bookSourceName_dup = {}

bookSourceGroup_dic = {}

check_list = [[], []]
result = []
for item in tqdm(origin_dict):
    bookSourceGroup = item.get("bookSourceGroup", "")
    item["bookSourceGroup"]=bookSourceGroup
    bookSourceUrl = item["bookSourceUrl"]
    # 预处理
    bookSourceUrl=bookSourceUrl.replace("已整理","")
    if "#" in bookSourceUrl:
        bookSourceUrl = bookSourceUrl.split("#",1)[0]
    if "search" in bookSourceUrl:
        bookSourceUrl = bookSourceUrl.split("search",1)[0]
    item["bookSourceUrl"] = bookSourceUrl
    bookSourceName = item["bookSourceName"]

    putong = ["5","6", "namo", "一程","3", "1","Namo","地址变动1210", "网络","APP","自查","随便吧","能用", "可用","已检","备用","文学迷","nnnn", "同人", '★网页源'\
              '普通', "发现", "搜索", "新+", "红莲相依", 'po', '400,400+', '🎃 通用', '小白自制', '🪁轻小说', '🪃其他', '🎀 晋江,🍊 女频', '💐 女频', '网页源', '有效书源', \
              '天龙', '🙈 新增','📝  小众', '🦔 刺猬', '🔒 YCK', '♾️', '📝 小众', '💠 其他', '2' , '实验']
    jingping = ['男频', '女频', '轻小说',"精华","精品", "精选", '⭐️ 收藏', '📗 纵横', '📜 追书', '🗞 掌阅', '🔥 HUO', '🐱 七猫', '🍑 九桃', '🌝 红袖', '🔥 HUO', '📃 优书',\
                '📒 得间', '🦉 飞卢', '🎈 轻文', '大佬', '百度', '晋江', "☄️ 抓包", "番茄", "优质"]
    chunban = ["出版", "付费"]
    teshu = ['刘备', '🔞', "特殊", "耽", "A级", "基友","R18", "18", "SM", "成人", "肉", "欲望"]
    manhua = ["漫画", "禁漫", "动漫"]
    yousheng = ["有声", "听书", "音乐"]
    zhonghe = ["🌙 ΑΡI", "平台", "杂", "聚合", "综合", "论坛"]
    zhengban = ["名著",'正版']
    black = ['校验超时', "错误"]


    if contain_str(item["bookSourceGroup"], putong):
        item["bookSourceGroup"] = '🔰 普通'
    elif contain_str(item["bookSourceGroup"], jingping):
        item["bookSourceGroup"] = "🎉 精选"
    elif contain_str(item["bookSourceGroup"], chunban):
        item["bookSourceGroup"] = "📚 出版"
    elif contain_str(item["bookSourceGroup"], teshu) or contain_str(bookSourceName, teshu):
        item["bookSourceGroup"] = "🚬 特殊"
    elif contain_str(item["bookSourceGroup"], manhua):
        item["bookSourceGroup"] = "🌠 漫画"
    elif contain_str(item["bookSourceGroup"], yousheng) or "有声" in bookSourceName or "听" in bookSourceName:
        item["bookSourceGroup"] = "📻 有声"
    elif contain_str(item["bookSourceGroup"], zhonghe):
        item["bookSourceGroup"] = "💠 综合"
    elif contain_str(item["bookSourceGroup"], zhengban):
        item["bookSourceGroup"] = '💰 正版'


    if "笔趣" in bookSourceName :
        item["bookSourceGroup"] = "💰 普通"
    if contain_str(bookSourceGroup, black):
        continue

    bookSourceGroup = item["bookSourceGroup"]
    if bookSourceGroup not in check_list[0]:
        check_list[0].append(bookSourceGroup)
    domain = urlparse(bookSourceUrl).netloc
    # print(domain)
    if domain not in check_list[1]:
        check_list[1].append(domain)
    else:
        continue
    bookSourceName_list = list(bookSourceName)
    if len(bookSourceName_list)==1:
        bookSourceName_list = bookSourceName.split()
    if "ハ" in bookSourceName:
        continue
    elif "ＵＣ书库" in bookSourceName:
        bookSourceName = "ＵＣ书库"
    else:
        for i in range(len(bookSourceName_list)):
            try:
                ch = bookSourceName_list[i]
                if '\u4e00' <= ch <= '\u9fff' or '0' <= ch <= '9' or 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                    break
                bookSourceName_list= bookSourceName_list[i:]
            except Exception as e:
                print(e)
                print(bookSourceName)
                print(i)
                continue
        book_len = len(bookSourceName_list)
        for i in range(len(bookSourceName_list)):
            try:
                ch = bookSourceName_list[book_len-i-1]
                if '\u4e00' <= ch <= '\u9fff' or 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                    break
                bookSourceName_list= bookSourceName_list[:book_len-i-1]
            except Exception as e:
                print(e)
                print(bookSourceName)
                print(i)
                continue
    bookSourceName = "".join(bookSourceName_list)
    newbookSourceName =bookSourceName.strip()
    dup_list = ["(优)", "㊣","♛","🎀","🌐","📺","🌠","🔮","📓","🌾","🍹","⌨","✐","🅰","🎨","📱","💫","🔥","🌸","🔝",
    "🧐","♨️","🌻","🔎","🦔", "🎈","▪︎API","♜","♬","🎧","💰","🌿","💦","📕","🎼","💾","🌄","🌷","🌱","✾",
    "🎉","🔖","🎃","✨","●QB  ","📚","🌙","💎","🍎","👍","🍀","🐱","📀", "🍊","🔞","🔲","🍩","🐼","💯",
    "🍁","💐","🔰","🌵","💜","🐲","🥣","🔶","🔹heenee","✍","🍒","🔷","👔","🍑","📖","📜","🌹","🍉","🎻",
    "⭐", "🌕","☘️","🐑","🧡","💗","🌈","🪙","👙","⚡","📗","🥂","💠","👾","①","❶","⑰","③","⑲","⑥","②","④",
    "⑤","⑲","⑱","⑧","⑪","㉙","㉛","㉘","⑩","㉕","㉗","⑫","⑨","㉒","⓪","⑦","㉖","⑭","⑮","⑯","⑳","㉑","㉓","㉔","㊿",
    "㉚","🧩","🪐","🙈","🔴","~m.zhuishushenqi.com","13.","备用™烏雲","pelingresort","<xguolu88>","ibiquge.net"]
    for dup in dup_list:
        if dup in bookSourceName:
            bookSourceName.replace(dup, "")
    
    if "#" in bookSourceName:
        newbookSourceName = bookSourceName.split("#")[0]
        print("origin name {} new name {}".format(bookSourceName, newbookSourceName))
        bookSourceName = newbookSourceName.strip()
    if "[" in bookSourceName:
        newbookSourceName = bookSourceName.split("[")[0]
        print("origin name {} new name {}".format(bookSourceName, newbookSourceName))
        bookSourceName = newbookSourceName.strip()
    if "（" in bookSourceName:
        newbookSourceName = bookSourceName.split("（")[0]
        print("origin name {} new name {}".format(bookSourceName, newbookSourceName))
        bookSourceName = newbookSourceName.strip()
    if "(" in bookSourceName:
        newbookSourceName = bookSourceName.split("(")[0]
        print("origin name {} new name {}".format(bookSourceName, newbookSourceName))
        bookSourceName = newbookSourceName.strip()
    if "ap" in bookSourceName:
        if "wap" in bookSourceName :
            continue
        newbookSourceName = bookSourceName.split("ap")[0]
        print("origin name {} new name {}".format(bookSourceName, newbookSourceName))
        bookSourceName = newbookSourceName.strip()
    print("origin name:{}".format(bookSourceName))
    
    item["bookSourceName"] = bookSourceName.replace(" ", "")
    item["bookSourceName"] = list(bookSourceGroup)[0] + " " + item["bookSourceName"]
    if item["bookSourceName"] not in bookSourceName_dup:
        bookSourceName_dup[item["bookSourceName"]] = [0, 0]
    else:
        bookSourceName_dup[item["bookSourceName"]][0]+=1

    if item["bookSourceName"] in bookSourceGroup_dic:
        item["bookSourceGroup"] = bookSourceGroup_dic[item["bookSourceName"]]
    else:
        bookSourceGroup_dic[item["bookSourceName"]] = item["bookSourceGroup"]
    

    result.append(item)
print(check_list[0])


with open(origin_booksource.replace("json","new.json"), encoding="utf-8", mode="w") as f:
    result = json.dump(result, f, ensure_ascii=False, indent=2)
