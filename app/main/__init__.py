#coding:utf-8
from flask import Blueprint
main = Blueprint('main', __name__)#定义蓝图，装饰器要以@main打头
from . import views				  #必须保持这个顺序