# Convert Jupyter notebook into a Python script that will execute all of your scraping code and return one Python dictionary 
# Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.
# Store the return value in Mongo as a Python dictionary.
# Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
# Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    # Find one record of data from the mongo database
    mars= mongo.db.mars.find_one()

    # Return template and data
    return render_template("index.html", mars=mars)

# Create a route called /scrape that will import your scrape_mars.py script and call your scrape function
@app.route("/scrape")
def scrape():
    mars=mongo.db.mars
    # Run the scrape function
    mars_data= scrape_mars.scrape_info()

    # Return value in Mongo as a Python dictionary
    mars.update({}, mars_data, upsert=True)

    return redirect('/')

if __name__ == "__main__":
    app.run(port=5001)