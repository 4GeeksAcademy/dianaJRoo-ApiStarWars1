from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class People(db.Model):
     __tablename__ = "people"
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(120), unique=True, nullable=False)
     eyes_color = db.Column(db.String(120), unique=True, nullable=False)


     def __init__(self, name, eyes_color):
        self.name = name
        self.eyes_color = eyes_color


     def __repr__(self):
        return f'<People {self.name}>'


     def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eyes_color": self.eyes_color
        }

class Planet(db.Model):
     __tablename__ = "planet"
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(120), unique=True, nullable=False)
     population = db.Column(db.Interger, unique=True, nullable=False)

     def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population
        }


class Favorites(db.Model):
     __tablename__ = "favorites"
     id = db.Column(db.Integer, primary_key=True)

     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
     user = db.relationship(User)

     people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
     people = db.relationship(People)

     planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
     planet = db.relationship(Planet)  