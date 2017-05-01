from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash, _app_ctx_stack
from werkzeug import check_password_hash, generate_password_hash
from data import *

# create our little application :)
app = Flask(__name__)
app.secret_key = 'my secret key'
app.config['SESSION_TYPE'] = 'filesystem'


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = get_user_by_userid(session['user_id'])

@app.route('/')
@app.route('/index')
def index():
    user = None
    if g.user:
        user = g.user
    category_list = get_category_list()
    return render_template("category_list.html",
                           title='Pick Category',
                           user=user,
                           category_list = category_list)


@app.route('/category/<category_name>')
def category_choice(category_name):
    user = None
    if g.user:
        user = g.user
    scenarios_list = get_scenario_list(category_name)
    return render_template("scenario_list.html",
                           title='Scenarios',
                           scenarios_list = scenarios_list)




@app.route('/event/<scenario_name>')
def scenario_choice(scenario_name):
    user = None
    if g.user:
        user = g.user
    word_list = get_word_list(scenario_name)
    return render_template("word_list.html",
                           title='Words related to ' + scenario_name,
                           word_list = word_list)


@app.route('/word/<word_id>/<word>')
def word_choice(word_id,word):
    word_row = get_word(word_id)
    sentence_list = get_sentence_list(word)
    user = None
    if g.user:
        user = g.user
    return render_template("sentence_list.html",
                           title='Sample sentences for <' + word + '>',
                           word_row = word_row,
                           sentence_list = sentence_list)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registers the user."""
    if g.user:
        return redirect(url_for('index'))
    error = None
    if request.method == 'POST':
        if not request.form['username']:
            error = 'You have to enter a username'
        elif not request.form['email'] or \
                '@' not in request.form['email']:
            error = 'You have to enter a valid email address'
        elif not request.form['password']:
            error = 'You have to enter a password'
        elif request.form['password'] != request.form['password2']:
            error = 'The two passwords do not match'
        elif get_user_id(request.form['username']) is not None:
            error = 'The username is already taken'
        else:
            create_user(request.form['username'],request.form['email'],generate_password_hash(request.form['password']))
            flash('You are successfully registered and can login now')
            return redirect(url_for('login'))
    return render_template('register.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Logs the user in."""
    if g.user:
        return redirect(url_for('index'))
    error = None
    if request.method == 'POST':
        user = get_user_id(request.form['username'])
        if user is None:
            error = 'Invalid username'
        elif not check_password_hash(user.pw_hash,
                                     request.form['password']):
            error = 'Invalid password'
        else:
            flash('You are now logged in')
            session['user_id'] = user.user
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    """Logs the user out."""
    flash('You were logged out')
    session.pop('user_id', None)
    return redirect(url_for('index'))

# if __name__ == "__main__":
#     app.secret_key = 'my secret key'
#     app.config['SESSION_TYPE'] = 'filesystem'

#     app.debug = True
#     app.run(port=80,host= '0.0.0.0')