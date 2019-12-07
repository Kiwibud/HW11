# ----------------------------------------------------------------------
# Name:        retaurants
# Purpose:     Demonstrate web development with Flask and Alchemy
#
# Author:      Kiwibud
# ----------------------------------------------------------------------
"""
Module containing a starter web application with database access.

Download and save into your PyCharm project.
Run the program.
Point your browser to http://localhost:5000/
"""
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurants.db'
db = SQLAlchemy(app)

"""
Each restaurant will have the following  information:

    name:  the restaurant name.
    location: the name of the city where the restaurant is located. 
    category: what kind of food does this restaurant serve? 
    price:  1 for cheap to 4 for expensive. 
"""
class Restaurant(db.Model):

    """
    Class to represent and access the restaurant table.
    Attributes:
    name (string): the restaurant name.
    location (string): the name of the city where the restaurant is located.
    category (string): what kind of food does this restaurant serve?
    grade (integer): 1 for cheap to 4 for expensive.
    """

    __tablename__ = "restaurant"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    category = db.Column(db.String)
    price = db.Column(db.Integer)


@app.route('/')
@app.route('/home')
def welcome():
    results = Restaurant.query.all()
    results.reverse()
    return render_template('home.html', results=results[:5])

@app.route('/add', methods=["POST","GET"])
def add():
    if request.method == "POST":
        name_input= request.form.get('name')
        category_input= request.form.get('category')
        location_input= request.form.get('location')
        price_input = request.form.get('price')
        new_restaurant = Restaurant(name=name_input,
                                    category=category_input,
                                    location=location_input, price=price_input)
        db.session.add(new_restaurant)
        db.session.commit()
    return render_template('add.html')


@app.route('/view')
def view():
    return render_template('view.html')

def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
