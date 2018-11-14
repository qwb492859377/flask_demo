# coding: utf-8

from app import app
from flask import Blueprint
from flask.views import View, MethodView


module = Blueprint('profile.index', __name__, url_prefix='/profile')


class IndexView(View):
    
    def dispatch_request(self):
        return 'hello profile index'


module.add_url_rule('', view_func=IndexView.as_view('_'))
