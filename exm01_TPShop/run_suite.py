"""
组织测试套件生成测试报告
流程:
    1.导包
    2.创建套件对象
    3.创建文件流,并且使用工具执行套件,将执行结果写入文件流
"""
# 导包
import unittest

import time

from exm01_TPShop.app import PRO_PATH
from exm01_TPShop.case.TestTPShopUser import TestUser

# 创建测试套件对象
from exm01_TPShop.tools.HTMLTestRunner import HTMLTestRunner

suite=unittest.TestSuite()
# 添加测试类或测试函数
# suite.addTest(TestUser("test_login"))
suite.addTest(unittest.makeSuite(TestUser))
# 先创建文件

# 疑惑: PRO_PATH相互干扰(此方法下os.getcwd())
#  单独运行:项目绝对路径 C:\Users\home\Desktop\软件测试\就业班\6_接口测试\2_daima\exm01_TPShop
#  先运行TestTPShopUser.py再运行此文件  项目绝对路径 C:\Users\home\Desktop\软件测试\就业班\6_接口测试\2_daima\exm01_TPShop\exm01_TPShop

file_to=PRO_PATH+"/report/report"+time.strftime("%Y%m%d%H%M%S")+".html"
print(PRO_PATH)
print(file_to)
# 打开文件流,工具执行套件,并将结果写出
with open(file_to,"wb") as f:
    runner=HTMLTestRunner(f,title="我的测试报告",description="V1.0")
    runner.run(suite)




