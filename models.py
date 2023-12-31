"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy


DEFAULT_IMAGE_URL = "https://tinyurl.com/demo-cupcake"

db = SQLAlchemy()

# MODELS GO BELOW!

class Cupcake(db.Model):
    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)

    flavor = db.Column(db.Text, nullable=False)

    size = db.Column(db.Text, nullable=False)

    rating = db.Column(db.Float, nullable=False)

    image = db.Column(db.Text, nullable=False, default = DEFAULT_IMAGE_URL)

    def serialization(self):
        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }
    
    def __repr__(self):
        return f"<Cupcake {self.id} flavor={self.flavor} size={self.size} rating={self.rating} image={self.rating}"
        

def connect_db(app):
    db.app = app
    db.init_app (app)