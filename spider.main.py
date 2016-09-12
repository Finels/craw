import html_downloader
import html_outputer
import html_parser
import url_manager
'''
the dispatch controller for the main programme,it will call all the self-modules 
'''

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url):
        cout = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (cout, new_url))
                html_count = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_count)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if cout==1000:
                    break
                cout+=1
            except:
                print('craw failed')

        self.outputer.output_html()
    pass


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
