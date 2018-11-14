# coding: utf-8

from app import app
from flask import Blueprint
from flask.views import View, MethodView


module = Blueprint('index', __name__, url_prefix='/')


class IndexView(View):
    
    def dispatch_request(self):
        return 'hello index'


class HelloWorldView(MethodView):

    def get(self):
        return 'hello world, get'

    def post(self):
        return 'hello world, post'


class TestView(View):
    
    def dispatch_request(self):
        return 'hello test index'


module.add_url_rule('', view_func=IndexView.as_view('_'))
module.add_url_rule('index', view_func=IndexView.as_view('index'))
module.add_url_rule('hello', view_func=HelloWorldView.as_view('hello'))
module.add_url_rule('hello/', view_func=TestView.as_view('hello_test'))
