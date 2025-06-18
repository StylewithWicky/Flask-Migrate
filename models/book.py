from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Book(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    published_year=db.Column(db.Integer)
    author_id=db.Column(db.Integer, db.ForeignKey('author_id'))

    
