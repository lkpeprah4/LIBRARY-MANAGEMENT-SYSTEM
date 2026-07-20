from config import db
class Books(db.Model):
    __tablename__="Books"
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    isbn=db.Column(db.String(20),nullable=False)
    total_copies=db.Column(db.Integer(), nullable=False)
    available_copies=db.Column(db.Integer(),nullable=False)
    author=db.Column(db.String(50),nullable=False)
    date_registered=db.Column(db.DateTime,nullable=False)


    def __repr__(self):
        return f'<BOOKS {self.title},{self.isbn},{self.total_copies}>'


