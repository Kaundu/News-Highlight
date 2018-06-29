from flask import render_template,request,redirect,url_for,abort
from . import main
from ..requests import get_updates, get_articles



# Views


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    political_articles = get_updates('politics')
    print(political_articles)
    business_articles = get_updates('business')
    # print(business_articles)
    tech = get_updates('technology')
    entertainment = get_updates('entertainment')
    title = 'News- Updates'
    return render_template('index.html', title=title,politics=political_articles, business=business_articles, technology=tech, entertainment=entertainment)


@main.route('/templates/update/<id>')
def source(id):
    articles = get_articles(id)
    print(articles)
    return render_template('update.html', articles=articles)
