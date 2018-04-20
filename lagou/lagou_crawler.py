from https import Https
from settings import headers, cookies
from data_manage import extract_company_name

import codecs

url = 'https://www.lagou.com/jobs/positionAjax.json'
para = {'first': 'true', 'pn': '1', 'kd': 'Java', 'city': '上海'}


def main():
    general_http = Https()
    content = general_http.post(url=url, para=para, headers=headers, cookies=cookies)
    companies = extract_company_name(content)
    with codecs.open('company.txt', 'wb', encoding='utf-8') as f:
        for company in companies:
            f.write(company + '\n')


if __name__ == '__main__':
    main()
