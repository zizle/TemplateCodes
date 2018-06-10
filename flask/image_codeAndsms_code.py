# _*_ coding:utf-8 _*_

# 容联云通讯的接入，结合yuntongxun文件夹内的sms.py文件
# 随机生成6位短信验证码
import random
from .yuntongxun.sms import CCP
sms_code = '%06d' % random.randint(0, 999999)
print('短信验证码:', sms_code)
# 发送短信
result = CCP().send_template_sms('15759566200', [sms_code, 3], 1)
print('结果:', result)

# image_code的生成
# 生成一个图片验证码,
from .captcha.captcha import captcha
name, text, image = captcha.generate_captcha()
