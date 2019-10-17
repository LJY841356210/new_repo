"""
编写unittest相关实现
    请求业务封装进api包
"""
# 导包
import json
import unittest
import requests
from parameterized import parameterized

from exm01_TPShop.api.UserAPI import UserLogin
from exm01_TPShop.app import PRO_PATH
# import os

# print(os.getcwd())

# 获取json文件数据



def read_json():
    data=[]
    # 项目绝对路径 C:\Users\home\Desktop\软件测试\就业班\6_接口测试\2_daima
    with open(PRO_PATH+"\exm01_TPShop/data/login_data.json","r",encoding="utf-8") as f:
        for value in json.load(f).values():
            data.append(
                (
                value.get("username"),
                value.get("password"),
                value.get("verify_code"),
                value.get("status"),
                value.get("msg")
                )
            )
    return data

# 创建测试类

class TestUser(unittest.TestCase):
    # 初始化函数
    def setUp(self):
        # 初始化session
        self.session=requests.Session()
        # 创建UserLogin()
        self.user_obj = UserLogin()
    # 资源销毁函数
    def tearDown(self):
        # 销毁session
        self.session.close()
    def test_get_verify_code(self):
        # 1.请求业务
        # 调用get_verify_code函数
        response=self.user_obj.get_verify_code(self.session)
        # 2.断言业务
        self.assertEqual(200,response.status_code)
        self.assertIn("image",response.headers.get("Content-Type"))

    @parameterized.expand(read_json())
    def test_login(self,username,password,verify_code,status,msg):
        # 1.请求业务
        # 调用get_verify_code函数
        response1=self.user_obj.get_verify_code(self.session)
        # 调用login函数
        response2=self.user_obj.login(self.session,username,password,verify_code)

        # 2.断言业务
        print(response2.json())
        self.assertEqual(status,response2.json().get("status"))
        self.assertIn(msg,response2.json().get("msg"))

