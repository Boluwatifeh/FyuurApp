#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(300))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120), default=None)
    seeking_talent = db.Column(db.Boolean(), default=False)
    seeking_description = db.Column(db.String(), default=None)
    area = db.Column(db.Integer, db.ForeignKey('Area.id'), nullable=False)
    shows = db.relationship('Show', backref='venue', lazy=True)

    def __repr__(self) -> str:
        return f'<Venue {self.id} {self.name}>'

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(300))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120), default=None)
    seeking_venue = db.Column(db.String())
    seeking_description = db.Column(db.String())
    shows = db.relationship('Show', backref='artist', lazy=True)


class Area(db.Model):
    __tablename__ = 'Area'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50))
    state = db.Column(db.String(30))
    venues = db.relationship('Venue', backref='Area', lazy=True)


class Show(db.Model):
    __tablename__ = 'Show'
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
    start_time = db.Column(db.String(50), nullable=False)

