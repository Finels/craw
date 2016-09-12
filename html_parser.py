import re
from urllib.parse import *

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, page_url, html_count):
        if page_url is None or html_count is None:
            return
        soup = BeautifulSoup(html_count, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup);
        new_data = self._get_new_data(page_url, soup);
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # 筛选所以a标签，用正则表达式匹配
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))  # \d表示数字
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)  # 将后一个参数按照前一个参数的url格式 自动拼接成一个完整的url
            new_urls.add(new_full_url)
        return new_urls

    '''
    解析抓取到的html内容，按照自定规则进行筛选
    '''

    def _get_new_data(self, page_url, soup):
        res_data = {}

        res_data['url'] = page_url
        # 例如筛选网页标题
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data
