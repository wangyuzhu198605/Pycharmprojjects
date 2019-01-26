# import re
# a="'http://www.24234.com,https://www.svdg5h454.com'"
# pattern=re.compile(r'https{0,1}://w+.*.com',re.S)
# result=pattern.findall(a)
# print(result)
# url="http://39.107.96.138:3000/api/v1/topic"
# patten=re.compile(r'http://{1-9}*/api/vi/topic/')
# result=patten.findall(url)
# print(result)
import urllib.request
import re


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent",
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    response = urllib.request.urlopen(req)
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    return html


def get_img(html):
    p = r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])'
    iplist = re.findall(p, html)
    for each in iplist:
        print(each)


if __name__ == "__main__":
    url = "http://www.xsdaili.com/dayProxy/ip/1021.html"
    get_img(open_url(url))
