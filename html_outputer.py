# -*- coding: gbk -*-
class HtmlOutputer(object):
    '''
    ��ҳ������������Զ��������ʽ
    XXXXXX
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
        fout.write("<head> <meta http-equiv=\"Content-Type\" content=\"text/html; charset=GBK\" /></head")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>"+(u""+data['title'])+"</td>")
            fout.write("<td>"+(u""+data['img'])+"</td>")
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body")
        fout.write("</html>")
        fout.close()

        # '''
        # ͼƬ��ʽ���
        # '''
        # for data in self.datas:
