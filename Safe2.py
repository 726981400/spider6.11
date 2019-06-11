import Safe
import requests
import re
import urllib.request
import xlwt

def getHtml(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    return html

y = 0
def getContext(html):
    x = 0
    sth = re.findall('<p>(.*?)</p>',html)#关于&#160；为tab制表符，难以去除
    return sth

def getImgs(html):
    imgs = re.findall('<img src=".*?(/images.*?.jpg)"',html)
    x = 0
    global y
    for img in imgs:
        imgs[x] = "http://www.gov.cn/gzdt"+ img
        # try:
        #     if str(imgs[x]).find('.jpg')>=0:
        #         urllib.request.urlretrieve(imgs[x],'\pic_down\%d.jpg' %(y))
        #     else:
        #         urllib.request.urlretrieve(imgs[x],'\pic_down\%d.jpg' %(y))
        # except:
        #     print("某张图片下载失败")
        #     pass
        x+=1
        y+=1
    return imgs

data_list = []
rowdata = []
def main():
    z = 0
    for url in Safe.main()[0]:#为什么循环完网址后停不下来？会重新循环？
        html = getHtml(url)
        context = getContext(html)
        imgs = getImgs(html)
        rowdata = [z,Safe.main()[1][z],imgs,context]
        data_list.append(rowdata)
        z+=1
        if z>60:
            break
    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
    row = 0
    for i in range(len(data_list)):
        col = 0;
        row = row + 1
        data = data_list[i]
        for j in range(len(data)):
            col = col + 1
            booksheet.write(row,col,data[j])
        workbook.save('安全局信息.xls')





if __name__ == '__main__':
    main()