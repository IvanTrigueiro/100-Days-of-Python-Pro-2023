from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)
    # return render_template('index.html')


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']
        new_book = Book(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit_rating", methods=['GET', 'POST'])
def edit_rating():
    if request.method == "POST":
        # Update Record
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    book_id = request.args.get("id")
    book_selected = Book.query.get(book_id)
    return render_template("edit_rating.html", book=book_selected)


@app.route("/edit_title", methods=['GET', 'POST'])
def edit_title():
    if request.method == "POST":
        # Update Record
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.title = request.form["title"]
        db.session.commit()
        return redirect(url_for("home"))
    book_id = request.args.get("id")
    book_selected = Book.query.get(book_id)
    return render_template("edit_title.html", book=book_selected)


if __name__ == "__main__":
    app.run(debug=True)
