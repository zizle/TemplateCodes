# _*_ coding:utf-8 _*_

import logging
from logging.handlers import RotatingFileHandler


def setup_log():
    # 设置日志的记录等级
    logging.basicConfig(level=logging.DEBUG)  # 调试debug级
    # 创建日志记录器, 指明日志保存的路径, 每个日志文件的最大大小,保存日志的文件上限个数
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志文件的记录格式            时间            文件名        行数                等级          信息
    formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    # 为日志记录器设置日志的记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志对象添加日志记录器
    logging.getLogger().addHandler(file_log_handler)