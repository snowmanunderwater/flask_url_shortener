from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

from flask_url_shortener.b62 import decode, encode

app = Flask(__name__)
app.config.from_object('websiteconfig')

db = SQLAlchemy(app)


def init_db():
    db.create_all()


class Links(db.Model):
    __tablename__ = 'links'
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(100), nullable=False)
    number = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Link: %r Number: %r>' % (self.link, self.number)


@app.route('/')
def index():
    return render_template('form.html')


@app.route('/process', methods=['POST'])
def process():

    link = request.form['link_to_shorten']

    # if link in database
    if link and not Links.query.filter_by(link=link).first():
        number = len(Links.query.all()) + 1
        l = Links(link=link, number=number)
        db.session.add(l)
        db.session.commit()

        return jsonify({'urll': 'localhost:5000/' + encode(number)})

    # if link not in database
    if link and Links.query.filter_by(link=link).first():
        number = Links.query.filter_by(link=link).first().number

        return jsonify({'urll': 'localhost:5000/' + encode(number)})

    return jsonify({'error': 'Missing data!'})


@app.route('/<urll>', methods=['GET'])
def urll(urll):
    number = decode(urll)
    newUrl = Links.query.filter_by(number=number).first()

    if newUrl:
        newUrl = newUrl.link

        if newUrl.startswith('https') or newUrl.startswith('http'):
            return redirect(f"{newUrl}", code=302)

        return redirect(f"http://{newUrl}", code=302)

    return ''
