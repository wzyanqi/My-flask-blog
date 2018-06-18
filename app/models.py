#coding:utf-8
from . import db

class Post(db.Model): #文章
	__tablename__ = 'posts'
	id = db.Column(db.Integer, primary_key = True) #主键
	time = db.Column(db.DateTime)	#日期与时间
	type = db.Column(db.Text)		#类别
	author = db.Column(db.Text)		#作者
	title = db.Column(db.Text)		#标题
	tag = db.Column(db.Text)		#标签
	abstract = db.Column(db.Text)	#摘要
	content = db.Column(db.Text)	#内容