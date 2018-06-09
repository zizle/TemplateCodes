# _*_ coding:utf-8 _*_

# flask项目中mysql数据库SQLAlchemy数据表模型

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置连接数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysql@127.0.0.1:3306/db_module_test?charset=utf8'
# 设置不追踪数据库该表，稍微提升点性能
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 先配置, 不然会报警告错误
db = SQLAlchemy(app)

'''
1. 一对多
    示例场景：
    用户与其发布的帖子(用户表与帖子表)
    角色与所属于该角色的用户(角色表与多用户表)
'''


class Role(db.Model):
    """角色表模型映射"""
    __tablename__ = 'tb_roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)
    # 添加两张表的关系模型， 关系添加在一的一方
    uses = db.relationship('User', backref='role', lazy='dynamic')


class User(db.Model):
    """用户表模型映射"""
    __tablename__ = 'tb_users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, index=True)
    # 添加关系外键(关系字段，外键在多的一方)
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id))


"""
2. 多对多
    示例场景:
    讲师与其上课的班级(讲师表与班级表)
    用户与其收藏的新闻(用户表与新闻表)
    学生与其选修的课程(学生表与选修课程表)
"""
# 多对多中间表直接建表
tb_student_course = db.Table('tb_student_course',
                             db.Column('student_id', db.Integer, db.ForeignKey('tb_students.id')),
                             db.Column('course_id', db.Integer, db.ForeignKey('tb_courses.id'))
                             )


class Student(db.Model):
    """学生表模型映射"""
    __tablename__ = 'tb_students'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)
    # 两张表多对多关系, secondary中间表的名字
    course = db.relationship('Course', secondary=tb_student_course,
                             backref=db.backref('students', lazy='dynamic'),
                             lazy='dynamic')


class Course(db.Model):
    """课程表模型映射"""
    __tablename__ = 'tb_courses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)


"""
3.自关联一对多
    示例场景
    区域表
    评论与该评论的子评论(评论表)
    参考网易新闻
"""


class Comment(db.Model):
    """评论表与该评论的子评论"""
    __tablename__ = 'tb_comments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 评论内容, 不允许为空
    content = db.Column(db.Text, nullable=False)
    # 父评论id
    parent_id = db.Column(db.Integer, db.ForeignKey('tb_comments.id'))
    # 父评论
    parent = db.relationship('Comment', remote_side=[id],
                             backref=db.backref('childs', lazy='dynamic'))

    """
    测试数据:
        p1 = Comment(content='今天天气真好呀!')
        p2 = Comment(content='这个写得真心不错..')
        c1 = Comment(content='好个球，我这里下雨。')
        c2 = Comment(content='我也觉得不错。。点赞')
        c1.parent = p1
        c2.parent = p2
        db.session.add_all([c1, c2])
        db.session.commit()
    """


"""
4. 自关联多对多
    示例场景
    用户关注其他用户(用户表，中间表)
"""


class PersonUser(db.Model):
    """用户表"""
    # 中间表
    tb_user_followers = db.Table('tb_user_followers',
                                 db.Column('follower_id', db.Integer, db.ForeignKey('tb_user_info.id'), primary_key=True),
                                 db.Column('followed_id', db.Integer, db.ForeignKey('tb_user_info.id'), primary_key=True),
                                 )

    __tablename__ = 'tb_user_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    # 用户所有的粉丝，添加了反向引用followed，代表用户都关注了哪些人
    followers = db.relationship('PersonUser',
                                secondary=tb_user_followers,
                                primaryjoin=id == tb_user_followers.c.follow_id,
                                secondaryjoin=id == tb_user_followers.c.follow_id,
                                backref=db.backref('followed', lazy='dynamic'),
                                lazy='dynamic')


if __name__ == '__main__':
    # db.drop_all()
    db.create_all()
    app.run(debug=True)
