-- MySQL dump 10.11
--
-- Host: localhost    Database: dev
-- ------------------------------------------------------
-- Server version	5.0.95-community

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `posts` (
  `id` int(11) NOT NULL auto_increment,
  `time` datetime default NULL,
  `type` text,
  `author` text,
  `title` text,
  `content` text,
  `abstract` text,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES (1,'2017-05-14 04:52:12','小说','王钊轶','你猜猜','<blockquote>\n<ul>\n<li>整理知识，学习笔记</li>\n<li>发布日记，杂文，所见所想</li>\n<li>撰写发布技术文稿（代码支持）</li>\n<li>撰写发布学术论文（LaTeX 公式支持）</li>\n</ul>\n</blockquote>\n<p><img alt=\"cmd-markdown-logo\" src=\"https://www.zybuluo.com/static/img/logo.png\" /></p>\n<p>除了您现在看到的这个 Cmd Markdown 在线版本，您还可以前往以下网址下载：</p>\n<h3><a href=\"https://www.zybuluo.com/cmd/\">Windows/Mac/Linux 全平台客户端</a></h3>\n<blockquote>\n<p>请保留此份 Cmd Markdown 的欢迎稿兼使用说明，如需撰写新稿件，点击顶部工具栏右侧的 <i class=\"icon-file\"></i> <strong>新文稿</strong> 或者使用快捷键 <code>Ctrl+Alt+N</code>。</p>\n</blockquote>\n<hr />\n<h2>什么是 Markdown</h2>\n<p>Markdown 是一种方便记忆、书写的纯文本标记语言，用户可以使用这些标记符号以最小 的输入代价生成极富表现力的文档：譬如您正在阅读的这份文档。它使用简单的符号标记不 同的标题，分割不同的段落，<strong>粗体</strong> 或者 <em>斜体</em> 某些文字，更棒的是，它还可以</p>\n<h3>1. 制作一份待办事宜 <a href=\"https://www.zybuluo.com/mdeditor?url=https://www.zybuluo.com/static/editor/md-help.markdown#13-待办事宜-todo-列表\">Todo 列表</a></h3>\n<ul>\n<li>[ ] 支持以 PDF 格式导出文稿</li>\n<li>[ ] 改进 Cmd 渲染算法，使用局部渲染技术提高渲染效率</li>\n<li>[x] 新增 Todo 列表功能</li>\n<li>[x] 修复 LaTex 公式渲染问题</li>\n<li>[x] 新增 LaTex 公式编号功能</li>\n</ul>\n<h3>2. 书写一个质能守恒公式[^LaTeX]</h3>\n<p>$$E=mc^2$$</p>\n<h3>3. 高亮一段代码[^code]</h3>\n<p>```python\n@requires_authorization\nclass SomeClass:\n    pass</p>\n<p>if <strong>name</strong> == \'<strong>main</strong>\':\n    # A comment\n    print \'hello world\'\n```</p>','你不在我不在~');
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-05-29 10:45:43
