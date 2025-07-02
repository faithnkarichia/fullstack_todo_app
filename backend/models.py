
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db=SQLAlchemy()

class Todo(db.Model, SerializerMixin):
    __tablename__= 'todos'
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String, nullable=True)
    description=db.Column(db.String, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "user_id": self.user_id,
        }

    


class User(db.Model, SerializerMixin):
    __tablename__='users'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    email=db.Column(db.String)
    phone_number=db.Column(db.Integer)
    password=db.Column(db.String     )

    todos=db.relationship('Todo',backref='user')
    serializer_rules=('-todos.user','-password')
    






