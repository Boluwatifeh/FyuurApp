#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from enum import unique
import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
import logging
from flask_moment import Moment
from flask_migrate import Migrate
from logging import Formatter, FileHandler
from flask_wtf import Form
import sqlalchemy
from forms import *
from models import Show, Artist, Area, Venue
from models import db
#----------------------------------------------------------------------------#
# App Config. 
#----------------------------------------------------------------------------#

app = Flask(__name__)
db.init_app(app)
moment = Moment(app)
app.config.from_object('config')
migrate = Migrate(app, db)


# TODO: connect to a local postgresql database
        
# TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format, locale='en')

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')


#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
  # TODO: replace with real venues data.
  #       num_upcoming_shows should be aggregated based on number of upcoming shows per venue.
  data = Area.query.all()
  return render_template('pages/venues.html', areas=data);

@app.route('/venues/search', methods=['POST'])
def search_venues():
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for Hop should return "The Musical Hop".
  # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"
  searched_term = request.form.get('search_term')
  response = (Venue.query.filter((Venue.city.ilike('%' + searched_term + '%') |
                                  Venue.name.ilike('%' + searched_term + '%') |
                                  Venue.state.ilike('%' + searched_term + '%') |
                                  Venue.genres.ilike('%' + searched_term + '%'))))
  return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  # shows the venue page with the given venue_id
  # TODO: replace with real venue data from the venues table, using venue_id
  data = Venue.query.get(venue_id)
  upcoming_shows = Show.query.join(Venue).filter(Venue.id == venue_id).filter(Show.start_time > datetime.utcnow())
  past_shows = Show.query.join(Venue).filter(Venue.id == venue_id).filter(Show.start_time <= datetime.utcnow())
  return render_template('pages/show_venue.html', venue=data,upcoming_shows=upcoming_shows, past_shows=past_shows)

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion
  retrieve_data = request.form.get 
  area = Area.query.filter_by(city=retrieve_data('city'), state=retrieve_data('state')).first()

  if not area:
        area = Area(city=retrieve_data('city'), state=retrieve_data('state'))
        db.session.add(area)
        db.session.commit()
  try:
      new_venue = Venue(name=retrieve_data('name'), city=retrieve_data('city'), state=retrieve_data('state'), address=retrieve_data('address'),
                        phone=retrieve_data('phone'), genres=retrieve_data('genres'), website_link=retrieve_data('website_link'),
                        facebook_link=retrieve_data('facebook_link'),
                        seeking_talent=retrieve_data('seeking_talent'), seeking_description=retrieve_data('seeking_description'), area=area.id)
      db.session.add(new_venue)
      db.session.commit()
      flash('Venue ' + request.form['name'] + ' was successfully listed!')
  except:
      db.session.rollback()
      flash('An error occurred. Venue ' + retrieve_data('name') + ' could not be listed.')
  return render_template('pages/home.html')
  
# on successful db insert, flash success
#flash('Venue ' + request.form['name'] + ' was successfully listed!')
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  #return render_template('pages/home.html')

@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
  # TODO: Complete this endpoint for taking a venue_id, and using
  # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.
  
  '''
  venue = Venue.query.get(venue_id)
  try:
      venue.delete()
      db.session.commit()
      flash(f'Venue {venue.name} has been deleted')
      return redirect(url_for('index'))
  except:
      db.session.rollback()
      flash(f'Venue {venue.name} could not be deleted')
      return redirect(url_for('index'))
  '''
  # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage
  #return None

#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
  # TODO: replace with real data returned from querying the database
  data = Artist.query.all()
  return render_template('pages/artists.html', artists=data)

@app.route('/artists/search', methods=['POST'])
def search_artists():
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
  # search for "band" should return "The Wild Sax Band".
  searched_term = request.form.get('search_term')
  response = (Artist.query.filter((Artist.city.ilike('%' + searched_term + '%') |
                                    Artist.name.ilike('%' + searched_term + '%') |
                                    Artist.state.ilike('%' + searched_term + '%') |
                                    Artist.genres.ilike('%' + searched_term + '%'))))
  return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  # shows the artist page with the given artist_id
  # TODO: replace with real artist data from the artist table, using artist_id
  data = Artist.query.get(artist_id)
  return render_template('pages/show_artist.html', artist=data)

#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  form = ArtistForm()
  artist = Artist.query.get(artist_id)
  form.name.data = artist.name
  form.genres.data = artist.genres.split()
  form.state.data = artist.state
  form.city.data = artist.state
  form.phone.data = artist.phone
  form.facebook_link.data = artist.facebook_link
  form.website_link.data = artist.website_link
  form.seeking_venue.data = artist.seeking_venue
  # TODO: populate form with fields from artist with ID <artist_id>
  return render_template('forms/edit_artist.html', form=form, artist=artist)

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  # TODO: take values from the form submitted, and update existing
  # artist record with ID <artist_id> using the new attributes
  artist = Artist.query.get(artist_id)
  form = ArtistForm()
  artist.name = form.name.data
  artist.phone = form.phone.data
  artist.city = form.city.data
  artist.state = form.state.data
  artist.genres = request.form.getlist('genres')
  artist.image_link = form.image_link.data
  artist.facebook_link = form.facebook_link.data
  artist.website_link = form.website_link.data
  artist.seeking_description = form.seeking_description.data
  db.session.commit()

  return redirect(url_for('show_artist', artist_id=artist_id))

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  form = VenueForm()
  venue = Venue.query.get(venue_id)
  form.name.data = venue.name
  form.phone.data = venue.phone
  form.city.data = venue.state
  form.state.data = venue.state
  form.address.data = venue.address
  form.genres.data = venue.genres.split()
  form.image_link.data = venue.image_link
  form.facebook_link.data = venue.facebook_link
  form.website_link.data = venue.website_link
  form.seeking_talent.data = venue.seeking_talent
  # TODO: populate form with values from venue with ID <venue_id>
  return render_template('forms/edit_venue.html', form=form, venue=venue)

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  # TODO: take values from the form submitted, and update existing
  # venue record with ID <venue_id> using the new attributes
  form = VenueForm()
  venue = Venue.query.get(venue_id)
  venue.name = form.name.data
  venue.phone = form.phone.data
  venue.city = form.city.data
  venue.state = form.state.data
  venue.address = form.address.data
  venue.genres = request.form.getlist('genres')
  venue.image_link = form.image_link.data
  venue.facebook_link = form.facebook_link.data
  venue.website_link = form.website_link.data
  venue.seeking_talent = form.seeking_talent.data
  venue.seeking_description = form.seeking_description.data
  db.session.commit()
  return redirect(url_for('show_venue', venue_id=venue_id))

#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  # called upon submitting the new artist listing form
  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion
  retrieve_data = request.form.get
  form = ArtistForm()
  if request.method == "POST":
    try:

        new_artist = Artist(name=retrieve_data('name'), city=retrieve_data('city'), state=retrieve_data('state'),
                            phone=retrieve_data('phone'), genres=retrieve_data('genres'), website_link=retrieve_data('website_link'),
                            facebook_link=retrieve_data('facebook_link'), image_link=retrieve_data('image_link'),
                            seeking_venue=retrieve_data('seeking_venue'), seeking_description=retrieve_data('seeking_description'))
        db.session.add(new_artist)
        db.session.commit()
        flash('Artist' + request.form['name'] + ' was successfully listed!')
    except:
        db.session.rollback()
        flash('An error occurred. Artist ' + retrieve_data('name') + ' could not be listed.')
    return render_template('pages/home.html')
  else:
    return render_template('forms/new_artist.html', form=form)
  # on successful db insert, flash success
  #flash('Artist ' + request.form['name'] + ' was successfully listed!')
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Artist ' + data.name + ' could not be listed.')
  #return render_template('pages/home.html')


#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  # displays list of shows at /shows
  # TODO: replace with real venues data.
  data = Show.query.all()
  return render_template('pages/shows.html', shows=data)

@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  # called to create new shows in the db, upon submitting new show listing form
  # TODO: insert form data as a new Show record in the db, instead
  form = ShowForm()
  artist_id = request.form.get('artist_id')
  venue_id = request.form.get('venue_id')
  artist = Artist.query.get(artist_id)
  venue_name = Venue.query.get(venue_id).name
  show = Show(artist_id=artist.id,venue_id=venue_id, start_time=form.start_time.data)
  db.session.add(show)
  db.session.commit()

  # on successful db insert, flash success
  flash('Show was successfully listed!')
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Show could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  return render_template('pages/home.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
