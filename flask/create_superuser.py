# _*_ coding:utf-8 _*_
from flask_script import Manager
manager = Manager()


@manager.option('-u', '-username', dest='username')
@manager.option('-p', '-password', dest='password')
@manager.option('-m', '-mobile', dest='mobile')
def createsuperuser(username, password, mobile):
    """创建超级管理员的脚本函数"""
    pass
    # try:
    #     db.session.add(obj)
    #     db.session.commit()
    #     print('创建成功!')
    # except Exception as e:
    #     print(e)
# 使用命令
# python create_superuser -u ... -p ... -m ...
