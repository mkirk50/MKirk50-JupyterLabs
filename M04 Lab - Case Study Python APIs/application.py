from flask import Flask, jsonify, request

# from werkzeug.datastructures import Authorization
app= Flask(__name__)
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.app_context().push()
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    book_name = db.Column(db.String(35), nullable=False)
    author = db.Column(db.String(35),nullable=False)
    publisher = db.Column(db.String(35),nullable=False)

    def __repr__(self):
        return f"Title: {self.book_name}       Author: {self.author}      Publisher: {self.publisher}"

@app.route('/')
def index():
    return 'Hello'

@app.route('/Books')
def get_books():
    books = Book.query.all()
    
    ouput=[]
    
    for book in books:
        book_data = {'Book_name': book.book_name, "Author":book.author, "Publisher":book.publisher}
        output.append(book_data)

    return {"books": output}

@app.route('/Books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'Book_name': book.book_name, "Author":book.author, "Publisher":book.publisher}

@app.route('/Books',methods=['POST'])
def add_drink():
       book=Book(book_name=request.json['book_name'],author=request.json['author'],publisher=request.json['publisher'])
       db.session.add(book)
       db.session.commit()
       return {'Book Added'}

@app.route('/Books/<id>', methods=['DELETE'])
def delete_book(id):
    book= Book.query.get(id)   
    if book is None:
        return {"error": "Not Found"}
    
    db.session.delete(book)
    db.session.commit()
    
@app.route('/Books/<id>', methods=['Post'])
def update_book(id):
    book= Book.query.get(id)   
    if book is None:
        return {"error": "Not Found"}
    db.session.delete(book)
    db.session.commit()
    
    book=Book(book_name=request.json['book_name'],author=request.json['author'],publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
      
