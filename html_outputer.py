class HtmlOutputer(object):
    '''
    网页输出器，可以自定义输出格式
    '''

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')
        fout.write("<html>")
        fout.write("<head> <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" /></head")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('GBK'))
            fout.write("<td>%s</td>" % data['img'].encode('GBK'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body")
        fout.write("</html>")

        # '''
        # 图片格式输出
        # '''
        # for data in self.datas:
