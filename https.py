import logging

def post(url, para, headers=None, cookies=None, proxy=None, timeOut=5, timeOutRetry=5):
    if not url or not para:
        logging.error('Post url or para can not be empty')
        return None

    logging.info('Post %s' % url)

