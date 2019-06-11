import requests
import re

def getHtml(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    response = requests.get(url , headers = headers)
    # 解决乱码
    response.encoding = 'utf-8'
    html = response.text
    f = open("安全局.txt","w")
    f.write(html)
    f.close()
    return html

url_list = []#网址列表
def getUrls(html):
    x = 0
    #网址
    urls = re.findall('href="(.*?)"', html)
    for url in urls:
        if x>27 and x<88 :
            url_list.append(url)
        x+=1
    x = 0
    for url in url_list:
        if url[1] == 'y' :
            url_list[x] = "http://www.gov.cn"+url
        x+=1
    # f = open("安全局灾害网址列表.txt", "w")
    # for url in url_list:
    #     f.write(url+"\r\n")#\r\n换行
    # f.close()
    return url_list

title_list = []#标题列表
def getTitle(html):
    #标题
    titles = re.findall('_blank"  >(.*?)</a>',html)
    for title in titles:
        title_list.append(title)
    # f = open("安全局灾害标题列表.txt", "w")
    # for title in title_list:
    #     f.write(title + "\r\n")  # \r\n换行
    # f.close()
    return title_list

def main():
    url = "http://www.gov.cn/yjgl/tfsj.htm"

    try:
        html = getHtml(url)
    except:
        print("检查网络或出现其他错误，导致网页没能down下来，已退出")

    Urls = getUrls(html)
    Titles = getTitle(html)

    Info = []
    Info.append(Urls)
    Info.append(Titles)

    return Info

if __name__ == '__main__':
    main()