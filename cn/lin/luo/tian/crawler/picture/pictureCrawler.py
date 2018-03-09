import codecs
import urllib.request

picture_url = 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2047004674,4088207824&fm=27&gp=0.jpg'

def main():
    print('Start gathering pictures...')
    download_picture(picture_url)


def download_picture(url):
    response = urllib.request.urlopen(url)
    cat_img = response.read()

    with codecs.open('qiaoba.jpg', 'wb') as f:
        f.write(cat_img)


if __name__ == '__main__':
    main()
