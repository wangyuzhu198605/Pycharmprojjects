import requests
import json
class RunMain():
    """无构造器"""
    def send_get(self, url, data):
        res = requests.get(url=url, params=data).json()
        return res

    def send_post(self, url, data):
        res = requests.post(url=url, data=data).json()
        return res

    def run_main(self, url, method, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res


if __name__ == '__main__':
    url = 'http://192.168.0.53:7001/CommonService/api/control/controlProgress/query.v'
    data = {
            'controlSeq': '2018118325'
    }
    run = RunMain()  # 先实例化，实例化时不需要带参数
    print(run.run_main(url, 'get', data))
