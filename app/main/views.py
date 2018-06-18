#coding:utf-8
from . import main
from flask import render_template, url_for, redirect
from app import db
import datetime

#-----CONFIG - BEGIN-----
PAPER_MAX_PAGE = 5
DOMAIN_NAME = ''
TAG_SPLIT = '#'
#-----CONFIG -  END -----

# #获取tag
def get_tag_cat():
	tag_dict = {}
	cat_dict = {}
	from ..models import Post
	#按照id排序
	all_post = Post.query.order_by(Post.id).all()[::-1]
	db.session.close()
	for (index, paper) in enumerate(all_post):
		if paper.type in cat_dict:
			cat_dict[paper.type].append(index)
		else:
			cat_dict.update({paper.type: [index]})
		tags = paper.tag.split(TAG_SPLIT)
		for(j, tag) in enumerate(tags):
			if tag in tag_dict:
				tag_dict[tag].append(index)
			else:
				tag_dict.update({tag: [index]})
	return all_post, tag_dict, cat_dict

@main.route('/about')
def about():
	db.session.close()
	return render_template('about.html')

@main.route('/tag')
def mytag():
	(all_post, tag_dict, cat_dict) = get_tag_cat()
	return render_template('tag.html', \
							tag_dict = tag_dict, \
							cat_dict = cat_dict, \
							all_post = all_post)
@main.route('/')
def home():
	(all_post, tag_dict, cat_dict) = get_tag_cat()
	if len(all_post) > PAPER_MAX_PAGE:
		num = PAPER_MAX_PAGE		#首页显示的文章数
	else:
		num = len(all_post)
	return render_template('home.html', num = num, \
							all_post = all_post,\
							cat_dict = cat_dict, \
							tag_dict = tag_dict)

@main.route('/page/<number>')
def page(number):
	(all_post, tag_dict, cat_dict) = get_tag_cat()
	post_num = len(all_post)
	if post_num >= (int(number) * PAPER_MAX_PAGE) :
		num = PAPER_MAX_PAGE
	elif (post_num - (int(number) - 1) * PAPER_MAX_PAGE) > 0 :
		num = post_num - (int(number) - 1) * PAPER_MAX_PAGE
	else:
		num = 0		#超出文章数，不显示
	post_page = all_post[PAPER_MAX_PAGE * (int(number) - 1) : \
						PAPER_MAX_PAGE * (int(number) - 1) + num]
	return render_template('page.html', number = number, \
							post_page = post_page, \
							post_num = post_num, \
							cat_dict = cat_dict, \
							tag_dict = tag_dict)

@main.route('/paper/<idx>')
def paper(idx):
	from ..models import Post
	mypost = Post.query.filter_by(id = int(idx)).all()[0]
	#last
	try:
		last_post = Post.query.filter_by(id = int(idx) - 1).all()[0]
		last_post_title = last_post.title
		last_post_url = str(int(idx) - 1)
	except:
		last_post_title = u'没有了'
		last_post_url = ''
	#next
	try:
		next_post = Post.query.filter_by(id = int(idx) + 1).all()[0]
		next_post_title = next_post.title
		next_post_url = str(int(idx) + 1)
	except:
		next_post_title = u'最新的了'
		next_post_url = ''
	(all_post, tag_dict, cat_dict) = get_tag_cat()
	return render_template('paper.html', mypost = mypost, \
							last_post_title = last_post_title, \
							next_post_title = next_post_title, \
							last_post_url = last_post_url, \
							next_post_url = next_post_url, \
							cat_dict = cat_dict, \
							tag_dict = tag_dict)

@main.route('/category')
def category():
	(all_post, tag_dict, cat_dict) = get_tag_cat()
	return render_template('category.html', \
							tag_dict = tag_dict, \
							cat_dict = cat_dict, \
							all_post = all_post)