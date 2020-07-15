from tools.api import request_tool
'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''
def test_a_zhuce(pub_data):
    pub_data["phone"] = "自动生成 手机号"
    pub_data["userName"] = "自动生成 字符串 7,9 数字字母"
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '注册'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/signup"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
  {
  "phone": "${phone}",
  "pwd": "aaa123",
  "rePwd": "aaa123",
  "userName": "${userName}"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"cstId": '$.data.cstId'}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method, url=uri, pub_data=pub_data, json_data=json_data, status_code=status_code,
                         expect=expect, feature=feature, story=story, title=title, json_path=json_path)


def test_denglu(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "pwd": "aaa123",
  "userName": "${userName}"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method, url=uri, pub_data=pub_data, json_data=json_data, status_code=status_code,
                         expect=expect, feature=feature, story=story, title=title)

def test_zengjia(pub_data):
    pub_data["productCode"] = "自动生成 字符串 5 数字字母 w"
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '增加产品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {
        "token": pub_data["token"]
    }
        # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "brand": "小米",
  "colors": [
    "炫酷黑","经典红"
  ],
  "price": 9999,
  "productCode": "${productCode}",
  "productName": "红米note999",
  "sizes": [
    "64g","128g"
  ],
  "type": "数码"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    json_path = [{"skuCode":"$.data[0].skuCode"}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(json_path=json_path,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_bianmacha(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '根据编码查'  # allure报告中二级分类
    title = "查询单个用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSkuByProdCode"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = {"prodCode":'${productCode}'}
    headers = {
        "token": pub_data["token"]
    }
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_xiugaijiage(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "修改价格"  # allure报告中一级分类
    story = '修改商品价格'  # allure报告中二级分类
    title = "锁定用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePrice"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"SKU":"${skuCode}","price":'8888'}
    headers = {
        "token": pub_data["token"]
    }
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_piliangxiugai(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '批量修改'  # allure报告中二级分类
    title = "锁定用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePriceByProdCode"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"price":'7777',"prodCode":"${productCode}"}
    headers = {
        "token": pub_data["token"]
    }
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_bianmachashangpin(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '根据产品编码查商品'  # allure报告中二级分类
    title = "查询单个用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSkuByProdCode"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = {"prodCode":'${productCode}'}
    headers = {
        "token": pub_data["token"]
    }
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_xiajia(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '下架'  # allure报告中二级分类
    title = "锁定用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/soldOut"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"productCode":'${productCode}'}
    headers = {
        "token": pub_data["token"]
    }
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_yushou(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '预售'  # allure报告中二级分类
    title = "锁定用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/toPreSale"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"productCode":'${productCode}'}
    headers = {
        "token": pub_data["token"]
    }
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

#商品库存模块
def test_tianzhengkucun(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '全量调整单个商品库存'  # allure报告中二级分类
    title = "锁定用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/fullSku"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"qty":'100',"skuCode":"${skuCode}"}
    headers = {
        "token": pub_data["token"]
    }
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

