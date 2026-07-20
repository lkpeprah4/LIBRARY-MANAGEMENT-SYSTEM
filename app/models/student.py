from config import db
class Student(db.Model):
    __tablename__="Student"
    id = db.Column(db.Integer, primary_key=True)
    index_number=db.Column(db.Integer(), nullable=False, unique=True)
    first_name= db.Column(db.String(30), nullable=False )
    last_name= db.Column(db.String(30), nullable=False )
    others_name= db.Column(db.String(30), nullable=False )
    password_hash=db.Column(db.String(200),nullable=False)
    phone_number= db.Column(db.String(10), unique=True, nullable=False )
    hostel=db.Column(db.String(15),nullable=False)
    course=db.Column(db.String(20),nullable=False)
    status=db.Column(db.String(15),nullable=False)

    def __repr__(self):
        return f'<Student {self.index_number},{self.first_name},{self.last_name}>'
