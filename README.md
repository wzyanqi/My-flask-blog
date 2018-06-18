# My-flask-blog
这个blog是我根据《Flask Web开发——基于Python的Web应用开发实践》上的代码，一步一步修改而成的一个轻量化小型博客，目前被部署在新浪的SAE代码托管上 **[一个汽车程序猿](http://iron.applinzi.com)**。

#### 代码结构
- /app 博客的主题实现部分 
- /migrations 迁移工具
- config.py 用于配置开发模式以及数据库地址
- mangage.py 起动博客
- dev.sql 测试模式下使用的数据库
- index.wsgi 新浪SAE模式
- venv.zip venv环境,需要解压到当前文件夹
- requirements.txt 安装环境

![](https://i.imgur.com/iZPv09g.png)
#### 数据库布置
原书上使用的是sqlite数据库，但是新浪云SAE不支持，就切换成mysql数据库，这里要引入**sae.const**。

    import sae.const
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' % (sae.const.MYSQL_USER, sae.const.MYSQL_PASS, sae.const.MYSQL_HOST, int(sae.const.MYSQL_PORT), sae.const.MYSQL_DB)
但在本地进行测试的时候，记得切换回来。

    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/dev'
### 数据库结构

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
数据库内容包括以上几个方面，在dev.sql编辑可以直接实现。文章内容请用Markdown撰写后，再用**migrations/markdown2html.py**生成后输入到content中即可。


