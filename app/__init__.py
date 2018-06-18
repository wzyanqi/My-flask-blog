#encoding:utf-8
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
	app =  Flask(__name__)						 #建立flask
	app.config.from_object(config[config_name]) #配置config
	config[config_name].init_app(app) 			#初始化flask配置
	bootstrap.init_app(app) 					#初始化bootstrap
	db.init_app(app) 							#初始SQLAlchemy数据库

	from .main import main as main_blueprint 	#导入蓝图
	app.register_blueprint(main_blueprint) 		#注册蓝图
	return app