from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe name', validators=[DataRequired()])
    cafe_location_url = StringField('Cafe location on Google Maps(URL)', validators=[DataRequired()])
    open_time = StringField('Open time e.g. 8:30AM', validators=[DataRequired()])
    close_time = StringField('Close time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee rating', choices=['☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'],
                                validators=[DataRequired()])
    wifi_rating = SelectField('Wifi rating',
                              choices=['✘', '💪💪💪💪💪', '💪💪💪💪', '💪💪💪', '💪💪', '💪'],
                              validators=[DataRequired()])
    power_rating = SelectField('Power outlet rating',
                               choices=['✘', '🔌🔌🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌', '🔌🔌', ' 🔌'],
                               validators=[DataRequired()])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    cafe_form = CafeForm()
    if cafe_form.validate_on_submit():
        form_entry = [entry.data for entry in cafe_form][:-2]
        form_entry[0] = '\n' + form_entry[0]
        with open('cafe-data.csv', mode='a') as data_file:
            entry_data = ','.join(form_entry)
            data_file.write(entry_data) # There is a problem here, will fix it later
        return render_template('/add.html', form=cafe_form)
    return render_template('/add.html', form=cafe_form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('/cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
