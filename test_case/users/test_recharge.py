import pytest

from test_case.conftest import pub_data
from tools.api import request_tool
from tools.data import excel_tool

data = excel_tool.get_test_case("test_case/users/充值测试2(1).xls")
@pytest.mark.parametrize("a,b,c",data[1],ids=data[0])
def test_a_chongzhi(a,b,c):
    pub_data["a"] = a
    pub_data["b"] = b
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    uri = "/acc/recharge"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "accountName": "${a}",
  "changeMoney": ${b}
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method, url=uri, pub_data=pub_data, json_data=json_data, status_code=status_code,
                         expect=expect, feature=feature, story=story, title=title)
