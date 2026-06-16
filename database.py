from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db=SQLAlchemy()
class MenuItem(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),nullable=False)
    description=db.Column(db.String(500),nullable=False)
    price=db.Column(db.Float,nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    category=db.Column(db.String(500),nullable=False)
    def __repr__(self):
        return f"MenuItem'{self.name}','{self.description}','{self.price}','{self.category}')"
class Message(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),nullable=False)
    phone=db.Column(db.String(50),nullable=False)
    content=db.Column(db.String(500),nullable=False)
    timestamp=db.Column(db.DateTime,default=datetime.utcnow)
    def __repr__(self):
        return f"Message('{self.name}','{self.phone}', '{self.content}', '{self.timestamp}')"