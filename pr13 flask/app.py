# import
from flask import Flask, render_template, redirect, url_for
from forms import LoginForm, RegisterForm
from flask_sqlalchemy import SQLAlchemy



# app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'kuki'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Database
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), unique=True)
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String(), unique=True)

# routs
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['post', 'get'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                return redirect(url_for('dashboard'))

        return '<h1>Invalid password</h1>'

    return render_template('login.html', form=form)


@app.route('/signup', methods=['post', 'get'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return '<h1>New user has been created!</h1>'

    return render_template('signup.html', form=form)


@app.route('/dashboard')
def dashboard():
    users = User.query.order_by(User.username).all()
    return render_template('dashboard.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
