import pickle
import time
import os
import logging
import urllib.request
from pictureCrawler import download_picture

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

url_zhihu = 'https://www.zhihu.com/signup?next=%2F'
url_12306 = 'https://kyfw.12306.cn/otn/index/init'
url_12306_picture_check = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
cookie_dir = os.getcwd() + os.sep + 'cookies' + os.sep
suffix_zhihu = '.zhihu'
suffix_12306 = '.12306'


# Imitate login with fireFox and store the cookie to determined place
# store cookies from ZhiHu
def login_zhihu(url, cookie_path):
    if not url:
        logging.error('url can not be empty')
        return

    cookies = load_cookies(cookie_path, suffix_zhihu)
    driver = prepare_login(url, cookies)

    # Switch to login page
    login_btn = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[2]/span')
    login_btn.click()

    driver.find_element_by_name('username').send_keys('****')
    driver.find_element_by_name('password').send_keys('****')
    driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/button').click()  # 点击登录
    time.sleep(5)
    print(driver.page_source)

    if not cookies:
        collect_cookies(driver, cookie_path, suffix_zhihu)


def login_12306(url, cookie_path):
    if not url:
        logging.error('url can not be empty')
        return
    cookies = load_cookies(cookie_path, suffix_12306)

    driver = prepare_login(url, cookies)
    driver.find_element_by_id('login_user').click()
    time.sleep(5)

    img_ele = driver.find_element_by_class_name('touclick-image')
    img_src = img_ele.get_property('src')
    download_picture(img_src, '12306.jpg')

    input_str = input("Enter your choice for pictures: ")
    nums = input_str.split(',')
    for num in nums:
        print(num)
    data = {}
    urllib.request.Request(url_12306_picture_check, data=data)

    # driver.find_element_by_id('username').send_keys('915504579@qq.com')
    # driver.find_element_by_id('password').send_keys('t19891020')
    # login_btn = driver.find_element_by_id('loginSub')
    # login_btn.click()

    print(driver.page_source)

def transfer_picture_choice(indexs):
    247,46,43,45,114,46,185,44,42,115,108,116,182,117,253,115
    42,50,118,45,185,42,246,44,38,115,182,118,248,117,112,

    41,43,114,43,183,43,254,42,40,117,111,116,182,115,253,113


def collect_cookies(driver, cookie_path, cookie_suffix):
    # get cookie information
    cookie_list = driver.get_cookies()

    cookie_dict = {}
    for cookie in cookie_list:
        # Write cookies to file
        f = open(cookie_path + cookie['name'] + cookie_suffix, 'wb')
        pickle.dump(cookie, f)
        f.close()

        if 'name' in cookie and 'value' in cookie:
            cookie_dict[cookie['name']] = cookie['value']


def prepare_login(url_login, cookies):
    options = Options()
    options.add_argument('-headless')
    driver = Firefox(executable_path='geckodriver', firefox_options=options)
    driver.get(url_login)
    # Add cookie action should after get action
    if cookies:
        for cookie in cookies:
            driver.add_cookie(cookie)
    time.sleep(5)
    return driver


def load_cookies(path, file_suffix):
    cookies = []
    files = os.listdir(path)
    for f in files:
        with open(path + f, 'rb') as pf:
            if pf.name.endswith(file_suffix):
                cookies.append(pickle.load(pf))
    return cookies


def main():
    # login_zhihu(url=url_zhihu, cookie_path=cookie_dir)
    login_12306(url=url_12306, cookie_path=cookie_dir)


if __name__ == '__main__':
    main()
