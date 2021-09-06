# import
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# settings
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# DATABASE
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    mail = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


# routs
@app.route('/')
@app.route('/home')
def index():
    articles = Article.query.order_by(Article.date).all()
    return render_template('index.html', articles=articles)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        mail = request.form['mail']

        article = Article(name=name, number=number, mail=mail)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except:
            return 'ERROR!!!!!!!!'
    else:
        return render_template('create-article.html')


# start
if __name__ == '__main__':
    app.run(debug=True)
