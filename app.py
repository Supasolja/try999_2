from flask import Flask, request, jsonify
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from models import Book, Author

# Init app
app = Flask(__name__)
app.config.from_object(Configuration)
# Init db
db = SQLAlchemy(app)


# Create a Book
@app.route('/Book', methods=['POST'])
def add_book():
    title = request.json['title']
    author = request.json['author']
    pages = request.json['pages']
    price = request.json['price']

    new_book = Book(title, author, pages, price)

    db.session.add(new_book)
    db.session.commit()

    return jsonify(new_book)


# Get all books
@app.route('/Books', methods=['GET'])
def get_books():
    all_books = Book.query.all()
    return jsonify(all_books)


# Get single book
@app.route('/Book/<id>', methods=['GET'])
def get_book(id):
    book = Book.query.get(id)
    return jsonify(book)


# Get single author
@app.route('/Author/<id>', methods=['GET'])
def get_author(id):
    author = Author.query.get(id)
    return jsonify(author)


# Get all authors
@app.route('/Author', methods=['GET'])
def get_authors():
    all_authors = Author.query.all()
    return jsonify(all_authors)


# Get books price by Author
@app.route('/Author/Books_price', methods=['GET'])
def get_books_price_by_author():
    books_price = db.session.query(Author.first_name, db.func.sum(Book.price))\
        .outerjoin(Book, Author.id == Book.author_id).group_by(Author.first_name).all()
    return jsonify(books_price)


# Get library author-book list
@app.route('/Lib_list', methods=['GET'])
def get_author_book_list():
    full_list = db.session.query(Author.first_name, Book.title).outerjoin(Book, Author.id == Book.author_id).all()
    return jsonify(full_list)


# Update a Book
@app.route('/Book/<id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get(id)

    title = request.json['title']
    author = request.json['author']
    pages = request.json['pages']
    price = request.json['price']

    book.title = title
    book.author = author
    book.pages = pages
    book.price = price

    db.session.commit()

    return jsonify(book)


# Delete single book
@app.route('/Book/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()

    return jsonify(book)


# Run server
if __name__ == '__main__':
    app.run(debug=True)

