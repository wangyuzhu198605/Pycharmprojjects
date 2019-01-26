import os

import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner
import time
test = "./"

# testsuite = unittest.TestSuite()


discover=unittest.TestLoader().discover(test,pattern='test*.py')
# if __name__=="__main__":
#     testsuite = unittest.TestSuite()

#     this_dir = os.path.dirname(__file__)
#     print(this_dir)
#     discover=unittest.TestLoader().discover(this_dir,pattern='test*.py')
#     testsuite.addTests(discover)
now=time.strftime("%Y-%m-d% %H-%m-%s")
filename="./"+now+"test_result.html"
fp=open(filename,"wb")
runner=HTMLTestRunner(stream=fp,title="测试报告",description="用例描述：")
runner.run(discover)