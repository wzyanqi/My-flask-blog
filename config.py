#encoding:utf-8
import os
import getpass  
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = '\xc0\xf4\xab\x97~\xf8\xea\xa6j\xcc\xf3\x17\x02g\x8d\xdf,z\xee\xea\x11\xc9\x9dX'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	FLASKY_MAIL_SENDER = 'small_iron@126.com'
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	SQLALCHEMY_POOL_RECYCLE = 5
	
	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/dev'

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/dev'

class ProductionConfig(Config):
	pass
	# just for sina sae
	#import sae.const
	#SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' % (sae.const.MYSQL_USER, sae.const.MYSQL_PASS, sae.const.MYSQL_HOST, int(sae.const.MYSQL_PORT), sae.const.MYSQL_DB)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': TestingConfig
}