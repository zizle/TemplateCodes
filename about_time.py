# _*_ coding:utf-8 _*_
import time, datetime

# 获取当前时间
t = time.localtime()
# 时间字符串
today_begin_str = '%d-%02d-%02d' % (t.tm_year, t.tm_mon, t.tm_mday)
# 时间对象
today_begin_date = datetime.datetime.strptime(today_begin_str, '%Y-%m-%d')

# 获取当前时间的前31天
# 添加时间列表
active_date = []
for i in range(0, 31):
    # 一天开始
    begin_date = today_begin_date - datetime.timedelta(days=i)
    # 一天结束
    end_date = today_begin_date - datetime.timedelta(days=(i - 1))
    active_date.append(datetime.datetime.strftime(begin_date, '%Y-%m-%d'))
