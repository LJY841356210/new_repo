"""
封装case请求中所需要的请求业务
"""
from exm01_TPShop import app


class UserLogin:
    # 函数1:验证码获取请求
    def get_verify_code(self,session):
        # session.get("验证码的url")
        return session.get(app.BASE_URL+"index.php?m=Home&c=User&a=verify")

    # 函数2,登录请求
    def login(self,session,username,password,verify_code):
        # session.post("登录的url",data="登录数据")
        log_data={"username":username,"password":password,"verify_code":verify_code}
        return session.post(app.BASE_URL+"index.php?m=Home&c=User&a=do_login",data=log_data)
