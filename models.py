from app import db


# Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    pages = db.Column(db.Integer)
    price = db.Column(db.Float)

    def __repr__(self):
        return "Book({self.title}, {self.author}, {self.pages}, {self.price})".format(self=self)


# Author model
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    second_name = db.Column(db.String(100))
    years_of_life = db.Column(db.String(9))
    books = db.relationship('Book', backref='author', lazy='select')

    def __repr__(self):
        return "Author({self.firs_name}, {self.second_name}, {self.years_of_life}, {self.price})".format(self=self)

