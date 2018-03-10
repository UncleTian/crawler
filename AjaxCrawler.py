import json
from urllib.request import urlopen
from urllib.request import Request

JSON_URL = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0'
url = 'https://www.lagou.com/jobs/positionAjax.json'
# para = {'first': 'true', 'pn': '1', 'kd': kd, 'city': city}


def load_json_content(content):
    json_object = json.loads(content)
    return json.dump(json_object)


def download_page(page_url):
    header = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0', "GET": url,
              "Host": "www.lagou.com"}
    req = Request(page_url, None, header)
    content = urlopen(req).read().decode("utf-8")
    return content


def main():
    result = download_page(JSON_URL)
    # str_res = load_json_content(result)
    print(result)


if __name__ == '__main__':
    main()
