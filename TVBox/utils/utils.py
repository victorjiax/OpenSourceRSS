from http.client import HTTPConnection
from urllib.parse import urlparse

def check_site_is_online(url, timeout=2):
    """如果目标URL在线，返回True
    """
    error = Exception("未知错误")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception as e:
            error = e
        finally:
            connection.close()
        print("======url:{}======error:{}".format(url, error))
    return False

emoji_list = ["♛","🎀","🌐","📺","🌠","🔮","📓","🌾","🍹","🎨","📱","💫","🔥","🌸","🔝","🧐",
            "♨️","🌻","🔎","🦔", "🎈","♜","♬","🎧","💰","🌿","💦","📕","🎼","💾","🌄","🌷",
            "🌱","✾","🎉","🔖","🎃","✨","📚","🌙","💎","🍎","👍","🍀","🐱","📀", "🍊","🔲",
            "🍩","🐼","💯","🍁","💐","🔰","🌵","💜","🐲","🥣","🔶","🍒","🔷","👔","🍑","🌹",
            "🍉","🎻","⭐", "🌕","☘️","🐑","🧡","💗","🌈","🪙","👙","⚡","📗","🥂",
            "💠","👾", "🧩","🪐","🙈","🔴"]