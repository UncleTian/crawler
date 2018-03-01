import requests
import BeautifulSoupCrawler

DOWNLOAD_URL = "https://movie.douban.com/top250"


def download_page(url):
    data = requests.get(url).content
    return data


def main():
    html = download_page(DOWNLOAD_URL)
    BeautifulSoupCrawler.parse_html(html)

if __name__ == '__main__':
    main()
