import pickle
import time
import os
import logging

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

url_zhihu = 'https://www.zhihu.com/signup?next=%2F'
cookie_dir = os.getcwd() + os.sep + 'cookies' + os.sep


# Imitate login with fireFox and store the cookie to determined place
# store cookies from ZhiHu
def login_zhihu(url, cookie_path):
    if not url:
        logging.error('url can not be empty')
        return

    cookies = load_cookies(cookie_path, '.zhihu')
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
        collect_cookies(driver, cookie_path)


def collect_cookies(driver, cookie_path):
    # get cookie information
    cookie_list = driver.get_cookies()

    cookie_dict = {}
    for cookie in cookie_list:
        # Write cookies to file
        f = open(cookie_path + cookie['name'] + '.zhihu', 'wb')
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
    login_zhihu(url=url_zhihu, cookie_path=cookie_dir)


if __name__ == '__main__':
    main()
