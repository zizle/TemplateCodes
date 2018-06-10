# _*_ coding:utf-8 _*_
"""

Flask中request:
    不同的数据选择不同的属性来读:
        data:读取请求中的原始字符串， 比如前端之间放在请求体中的json字符串
        args:获取url中?后面的查询字符串
        form:获取请求体中form表单中的数据
        files:获取请求体中的文件数据
        cookie:获取请求体中cookie的数据

get请求和post请求:
    get请求擅长从服务器获取数据， 也可以向服务器发送数据，但是数据要暴露在url中
    post擅长向服务器发送数据，向服务器获取数据的效率不及get
"""
