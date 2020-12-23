from flask import render_template, request
from . import main
from .. models import User


@main.route('/')
def index():
    return render_template('index.html')

'''
@main.route('/search')
def search():
    page = request.args.get('page', 1, type=int)
    pagination = User.query.filter().paginate(page, per_page=6, error_out=False)
    users = pagination.items
    return render_template('search.html', users=users, pagination=pagination)
'''

