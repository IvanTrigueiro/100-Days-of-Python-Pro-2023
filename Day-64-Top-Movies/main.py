from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests, os
TMDB_API_KEY = os.environ.get("TMDB_API_KEY")
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Create Table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()
    #
    # new_movie = Movie(
    #     title="Lawrence of Arabia",
    #     year=1962,
    #     description="The story of T.E. Lawrence, the English officer who successfully united and led the diverse, "
    #                 "often warring, Arab tribes during World War I in order to fight the Turks.",
    #     rating=8.3,
    #     ranking=10,
    #     review="Great movie.",
    #     img_url="https://sothebys-md.brightspotcdn.com/c1/c4/72e5c8c64cb6971a68c515ae832e/l19985-b9yft-01.jpg"
    # )
    # db.session.add(new_movie)
    # db.session.commit()


class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    ranking = StringField("Ranking out of 10", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()

    if form.validate_on_submit():
        movie_title = form.title.data
        response_tmdb = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": TMDB_API_KEY, "query": movie_title})
        # print(response_tmdb.status_code)
        # print(response_tmdb.json())
        data = response_tmdb.json()["results"]
        return render_template("select.html", options=data)

    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    movie_id = request.args.get("id")
    with app.app_context():
        if movie_id:
            movie_api_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
            response = requests.get(movie_api_url, params={"api_key": TMDB_API_KEY, "language": "en-US"})
            data = response.json()
            new_movie = Movie(
                title=data["title"],
                year=data["release_date"][0:4],
                img_url=f"https://image.tmdb.org/t/p/w500/{data['poster_path']}",
                description=data["overview"]
            )
            db.session.add(new_movie)
            db.session.commit()
            return redirect(url_for("home"))


@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        movie.ranking = form.ranking.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
