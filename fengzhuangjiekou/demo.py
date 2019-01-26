import requests
import json


class RunMain():
    """含有构造器"""
    def __init__(self, url, method, data=None,headers=None):
        self.url=url
        self.method=method
        self.data=data
        self.headers=headers
        self.t = self.run_main(url, method, data, headers)

    def send_post(self, url, data,headers):
        r = requests.post(url=url, data=data,headers=headers)
        result = r.json()
        return json.dumps(result, indent=2, sort_keys=False, ensure_ascii=False)

    def send_get(self, url, data):
        r = requests.get(url=url, params=data)
        result = r.json()
        return json.dumps(result, indent=2, sort_keys=False, ensure_ascii=False)
        # 利用json.dumps将响应数据进行json格式的编码解析
        # indent=2将输出结果缩进2个字符显示
        # sort_keys=False，输出结果是否按照关键字排序
        # json.dumps 序列化时对中文默认使用的ascii编码，ensure_ascii=False才会输出中文
        # return result

    def run_main(self, url, method, data=None,headers=None):
        if method.upper() == 'GET':
            r = self.send_get(url, data)
        else:
            r = self.send_post(url, data,headers)
        return r,r.json()



if __name__ == '__main__':

    url = 'https://www.v2ex.com/api/nodes/show.json'
    data = {
        'name': 'python'
    }

    test = RunMain(url, 'GET', data)  # 因为有构造器 __init__，实例化时要带参数
    print(test.t)
