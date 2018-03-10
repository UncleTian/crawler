import pickle

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


def get_cookie_from_network():
    options = Options()
    options.add_argument('-headless')
    url_login = 'https://passport.baidu.com/v2/api/?login'
    driver = Firefox(executable_path='geckodriver', firefox_options=options)
    driver.get(url_login)
    driver.find_element_by_xpath('//input[@type="text"]').send_keys('13524352854')  # 改成你的微博账号
    driver.find_element_by_xpath('//input[@type="password"]').send_keys('*****')  # 改成你的微博密码

    driver.find_element_by_xpath('//input[@type="submit"]').click()  # 点击登录

    # get cookie informations
    cookie_list = driver.get_cookies()
    print(cookie_list)

    cookie_dict = {}
    for cookie in cookie_list:
        # Write cookies to file
        f = open(cookie['name'] + '.weibo', 'w')
        pickle.dump(cookie, f)
        f.close()

        if cookie.has_key('name') and cookie.has_key('value'):
            cookie_dict[cookie['name']] = cookie['value']

    return cookie_dict


def main():
    cookies = get_cookie_from_network()
    print(cookies)


if __name__ == '__main__':
    main()
