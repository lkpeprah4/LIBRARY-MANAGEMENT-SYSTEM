from config import db
class Borrows(db.Model):
    __tablename__="Borrows"
    id=db.Column(db.Integer, primary_key=True)
    borrowed_at=db.Column(db.DateTime)
    return_at=db.Column(db.DateTime)
    fine_amount=db.Column(db.Integer,nullable=True)
    due_date=db.Column(db.DateTime)

    Book_id=db.Column(db.Integer, db.ForeignKey('Books.id'),nullable=False)
    Student_index_number=db.Column(db.Integer,  db.ForeignKey('Student.index_number'),nullable=False)

    Book=db.relationship('Books',backref='borrows')

    def __repr__(self):
        return f'<Borrows-Book_id{self.Book_id},Borrowed_at {self.borrowed_at}>'

