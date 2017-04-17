from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash, _app_ctx_stack
from werkzeug import check_password_hash, generate_password_hash
from data import *

# create our little application :)
app = Flask(__name__)


# @app.before_request
# def before_request():
#     g.user = None
#     if 'user_id' in session:
#         g.user = query_db('select * from user where user_id = ?',
#                           [session['user_id']], one=True)

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    category_list = get_category_list()
    return render_template("category_list.html",
                           title='Home',
                           user=user,
                           category_list = category_list)


@app.route('/category/<category_name>')
def category_choice(category_name):
    scenarios_list = get_scenario_list(category_name)
    return render_template("scenario_list.html",
                           title='Scenarios',
                           scenarios_list = scenarios_list)




@app.route('/event/<scenario_name>')
def scenario_choice(scenario_name):
    word_list = get_word_list(scenario_name)
    return render_template("word_list.html",
                           title='Words related to ' + scenario_name,
                           word_list = word_list)


@app.route('/word/<word_id>/<word>')
def word_choice(word_id,word):
    sentence_list = get_sentence_list(word)
    return render_template("sentence_list.html",
                           title='Sample sentences for <' + word + '>',
                           sentence_list = sentence_list)


if __name__ == "__main__":
    app.run()