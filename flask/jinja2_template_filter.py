# _*_ coding:utf-8 _*_
def do_rank(num):
    """自定义模板过滤器"""
    if num == 1:
        return 'first'
    elif num == 2:
        return 'second'
    elif num == 3:
        return 'third'
    else:
        return ''


# 加入使用，参数二是在模板内使用的名字
app.add_template_filter(do_rank, 'rank')


# 定义装饰器装饰视图函数，先检测用户的登录状态
from functools import wraps


def decoration(views_func):
    @wraps(views_func)
    def wrapper(*args, **kwargs):
        pass
        return views_func(*args, **kwargs)
    return wrapper
