#coding='utf-8'

import datetime
import urllib.request
import re
import os, sys

# url = "http://findicons.com/pack/2787/beautiful_flat_icons"
url = "http://www.meizitu.com"
# 设置headers，网站会根据这个判断你的浏览器及操作系统，很多网站没有此信息将拒绝你访问
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

save_dir = "d:/spider_image/"

# 获取要爬取的母网页的 HTML 内容
def getHTML(url):
    webPage = urllib.request.urlopen(url)
    html = webPage.read()
    html = html.decode('utf-8',"ignore")  #忽略 无法解码的 字符
    return html

# 对母网页内容处理，提取出里面的图片链接
def getPicList(html):
    k = re.split(r'\s+', html)
    s = []
    sp = []
    si = []


    for i in k:
        if (re.match(r'src', i) or re.match(r'href', i)):
            if (not re.match(r'href="#"', i)):
                if (re.match(r'.*?png"', i) or re.match(r'.*?ico"', i) or re.match(r'.*?jpg"', i)):
                    if (re.match(r'src', i)):
                        s.append(i)



    # 过滤结果
    for it in s:
        if (re.match(r'.*?png"', it) or re.match(r'.*?jpg"', it)):
            sp.append(it)

    return sp

# 爬取图片
def spider_pic():
    # 对母网页内容处理，提取出里面的图片链接
    html = getHTML(url)
    # 对母网页内容处理，提取出里面的图片链接
    sp = getPicList(html)

    # 检查文件夹是否存在
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # 获取这些图片链接的内容，并保存成本地图片
    cnt = 0
    cou = 1
    for it in sp:

        m = re.search(r'src="(.*?)"', it)
        iturl = m.group(1)
        print(iturl)
        if (iturl[0] == '/'):
            continue;

        # 加上 HTTP 数据请求头

        req = urllib.request.Request(url=iturl, headers=header)
        web = urllib.request.urlopen(req)
        img_data = web.read()  # 图片数据

        date_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")  # 当前时间
        # 只下载30张图片
        if (cnt <= 30):
            f = open(save_dir + date_now + '.jpg', "wb")
            f.write(img_data)
            f.close()
        cnt = cnt + 1



if __name__=='__main__':
    spider_pic()














