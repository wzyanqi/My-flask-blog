# My-flask-blog
这个blog是我根据《Flask Web开发——基于Python的Web应用开发实践》上的代码，一步一步修改而成的一个轻量化小型博客，目前被部署在新浪的SAE代码托管上 **[一个汽车程序猿](http://iron.applinzi.com)**。

![](https://i.imgur.com/iZPv09g.png)
#### 数据库布置
原书上使用的是sqlite数据库，但是新浪云SAE不支持，就切换成mysql数据库，这里要引入**sae.const**。

    import sae.const
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' % (sae.const.MYSQL_USER, sae.const.MYSQL_PASS, sae.const.MYSQL_HOST, int(sae.const.MYSQL_PORT), sae.const.MYSQL_DB)
但在本地进行测试的时候，记得切换回来。

    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/dev'
