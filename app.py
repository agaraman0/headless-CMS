from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    slug = db.Column(db.String(255), nullable=False, 
unique=True)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    filename = db.Column(db.String(255), nullable=False, 
unique=True)

@app.route('/pages', methods=['GET'])
def get_pages():
    pages = Page.query.all()
    return jsonify([page.to_dict() for page in pages])

@app.route('/pages/<string:slug>', methods=['GET'])
def get_page(slug):
    page = Page.query.filter_by(slug=slug).first_or_404()
    return jsonify(page.to_dict())

@app.route('/images', methods=['GET'])
def get_images():
    images = Image.query.all()
    return jsonify([image.to_dict() for image in images])

@app.route('/images/<string:filename>', methods=['GET'])
def get_image(filename):
    image = 
Image.query.filter_by(filename=filename).first_or_404()
    return jsonify(image.to_dict())

if __name__ == '__main__':
    app.run(debug=True)

