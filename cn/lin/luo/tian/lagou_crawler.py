from cn.lin.luo.tian.https import Https
from cn.lin.luo.tian.settings import headers, cookies
from cn.lin.luo.tian.data_manage import data_extract
import codecs

url = 'https://www.lagou.com/jobs/positionAjax.json'
para = {'first': 'true', 'pn': '1', 'kd': 'Java', 'city': '上海'}


def main():
    general_http = Https()
    content = general_http.post(url=url, para=para, headers=headers, cookies=cookies)
    companies = data_extract(content)
    with codecs.open('company.txt', 'wb', encoding='utf-8') as f:
        for company in companies:
            f.write(company + '\n')


if __name__ == '__main__':
    main()
