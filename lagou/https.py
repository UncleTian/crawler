import logging
import requests


class Https:
    def post(self, url, para, headers=None, cookies=None, proxy=None, time_out=5, time_out_retry=5):
        if not url or not para:
            logging.error('url or para is empty')
            return None

        logging.info('Post %s' % url)

        try:
            if not headers:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'}
            response = requests.post(url=url, data=para, headers=headers, cookies=cookies, proxies=proxy,
                                     timeout=time_out)

            if response.status_code == 200 or response.status_code == 300:
                html_code = response.text
            else:
                html_code = None
                logging.error('Post %s %s' % (response.status_code, url))
        except Exception as e:
            logging.error('Post exception %s' % str(e))
            if time_out_retry > 0:
                time_out_retry -= 1
                html_code = self.post(url=url, para=para, timeOutRetry=time_out_retry)
            else:
                logging.error('Post time out')
                return None
        return html_code
