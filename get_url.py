# collect comment urls from yousuu.com
import glob
from requests_html import HTMLSession, HTML
import time
import re
import os

def get_book_urls(html):  # 修改函数参数，接受HTML字符串而不是URL
    page = HTML(html=html)  # 使用HTML类实例化HTML字符串
    bookname = page.find(".book-name") # 使用CSS选择器提取评论
    bookurl = {}
    for book in bookname:
        bookurl[book.text] = 'https://www.yousuu.com' + book.attrs['href']
    return bookurl

# 单个网页解析测试
# session = HTMLSession()
# r = session.get('https://www.yousuu.com/bookstore/?channel&classId=2')
# html = r.html.html
# bookurl = get_book_urls(html)
# print(len(bookurl))
# print(bookurl)

# 自动创建文件夹
if not os.path.exists('./urls'):
    os.mkdir('./urls')

# 网页批量化处理
files = glob.glob('./cats/*.html')
print(len(files))

for file in files:
    # 读取html文件
    html = open(file, 'r', encoding='utf-8').read()
    # 利用requests_html函数解析
    bookurl = get_book_urls(html)
    # 将解析后的结果写入文件
    try:
        if '游戏' in file:
            with open('./urls/url_youxi.txt', 'a', encoding='utf-8') as f:
                f.write(str(bookurl) + '\n')
        elif '历史' in file:
            with open('./urls/url_lishi.txt', 'a', encoding='utf-8') as f:
                f.write(str(bookurl) + '\n')
        elif '奇幻' in file:
            with open('./urls/url_qihuan.txt', 'a', encoding='utf-8') as f:
                f.write(str(bookurl) + '\n')
        elif '玄幻' in file:
            with open('./urls/url_xuanhuan.txt', 'a', encoding='utf-8') as f:
                f.write(str(bookurl) + '\n')
        elif '都市' in file:
            with open('./urls/url_dushi.txt', 'a', encoding='utf-8') as f:
                f.write(str(bookurl) + '\n')
        print(file, 'success')
    except:
        print(file, 'fail')
