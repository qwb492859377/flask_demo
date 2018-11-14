# coding: utf-8

from app import app
from flask import Blueprint
from flask.views import View, MethodView


module = Blueprint('admin', __name__, url_prefix='/admin')


class IndexView(View):
    
    def dispatch_request(self):
        return 'admin hello index'


class HelloWorldView(MethodView):

    def get(self):
        return 'admin hello world, get'

    def post(self):
        return 'admin hello world, post'


class TestView(View):
    
    def dispatch_request(self):
        return 'admin hello test index'


module.add_url_rule('', view_func=IndexView.as_view('_'))
module.add_url_rule('/', view_func=TestView.as_view('index'))
module.add_url_rule('/hello', view_func=HelloWorldView.as_view('hello'))
