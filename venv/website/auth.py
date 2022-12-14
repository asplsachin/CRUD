from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)


@auth.route('/home')
def home():
    return render_template('home.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return "<p>logout<p>"


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

    return render_template('sign_up.html')
