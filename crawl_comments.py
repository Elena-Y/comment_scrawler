# crawl comments
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys
import time
import os
import random
import glob


def get_comment(url):
    driver.get(url)

    # 展开评论内容（若有）
    try:
        show_buttons = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.ToggleBtn'))
        )
        for show_button in show_buttons:
            show_button.click()
            time.sleep(0.5)
        print("已展开全部")
    except:
        print("按钮未找到或超时")

    # 提取评论内容
    try:
        comments = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="comment-content"]'))
        )
        if '收起全部' in comments[-1].text:
            comments = comments[:-1]
        time.sleep(0.5)
        return comments
    except:
        print("评论内容未找到或超时")
    

def login():
    driver.get('https://www.yousuu.com/login')
    # 关闭弹窗（如果有的话）
    try:
        close_button = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(., '关闭')]"))
        )
        close_button.click()
        print("弹窗已关闭")
    except:
        print("弹窗未找到或超时")
    
    # 找到用户名和密码的输入框，并输入相应的信息
    username_input = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/section/div/div/form/div[1]/div[1]/div/div/input') #排除搜索框的干扰
    password_input = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/section/div/div/form/div[1]/div[2]/div/div/input')

    try:
        username_input.send_keys('18410997021')
        time.sleep(0.5)
        password_input.send_keys('D4pwj,xbrys.')
        time.sleep(0.5)
        # 提交表单
        try:
            password_input.send_keys(Keys.RETURN)
            print("登录成功")
        except:
            print("登录失败")
    except:
        print("输入框未找到")

# 创建一个WebDriver实例（使用Chrome浏览器）
driver = webdriver.Chrome()
login()
time.sleep(0.5)

# # 单页测试
# url = 'https://www.yousuu.com/book/112'
# comments = get_comment(url)
# for comment in comments:
#     print(comment.text)

# 自动创建文件夹
if not os.path.exists('./comments'):
    os.mkdir('./comments')

# 批量爬取
files = glob.glob('./urls/*.txt')
print(len(files))

for file in files:
    cat = file.split('_')[-1].strip('.txt')
    with open(file, 'r', encoding='utf-8') as f:
        books = f.read()
        books = books.replace("\n", ",")
        books = books.split(',')
        # print(books)
        for book in books:
            book = book.replace("{", "")
            book = book.replace("}", "")
            book = book.replace("'", "")
            book = book.replace(": ", " ")
            # print(book)
            try:
                name, url = book.split()
                # print(name, url)
            except:
                if book == ' ':
                    print('space error')
                elif book == '':
                    print('empty error')
                elif book == '\n':
                    print('line error')
                continue
            filename = f'./comments/{cat}_{name}.txt'
            # print(name, url)
            # print(filename)
            if os.path.exists(filename):
                print(name, 'exists')
                continue
            # print(name, 'start')
            # print(url)
            comments = get_comment(url)
            if not comments or '请登录查看评论内容' in comments[0].text:
                print(name, 'failed')
                continue
            with open(f'./comments/{cat}_{name}.txt', 'w', encoding='utf-8') as f:
                for comment in comments:
                    f.write(comment.text + '\n')  
                print(name, 'success')
            time.sleep(random.uniform(1.5, 5.5))
        print(f'{cat}爬取完成')
    

# 关闭浏览器
driver.close()