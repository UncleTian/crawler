import codecs

import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = "https://movie.douban.com/top250"

def parse_html(html):
    soup = BeautifulSoup(html)

    movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})
    movie_name_list = []

    for movie_li in movie_list_soup.find_all('li'):
        detail = movie_li.find('div', attrs={'class': 'hd'})
        movie_name = detail.find('span', attrs={'class': 'title'}).getText()
        movie_name_list.append(movie_name)

    next_page = soup.find('span', attrs={'class': 'next'}).find('a')
    if next_page:
        return movie_name_list, DOWNLOAD_URL + next_page['href']
    return movie_name_list, None


def download_page(url):
    data = requests.get(url).content
    return data


def main():
    url = DOWNLOAD_URL

    with codecs.open('movies.txt', 'wb', encoding = 'utf-8') as fp:
        while url:
            print("the URL is", url)
            html = download_page(url)
            movie_name_list, next_page = parse_html(html)
            for movie_name in movie_name_list:
                print(movie_name)
            url = next_page
            fp.write(u'{movies}\n'.format(movies = '\n'.join(movie_name_list)))

if __name__ == '__main__':
    main()
