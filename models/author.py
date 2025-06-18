from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Author(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100),nullable= False)
    age =db.Column(db.Integer, nullable=False)
    books=db.relationship('Book', backref='author')


