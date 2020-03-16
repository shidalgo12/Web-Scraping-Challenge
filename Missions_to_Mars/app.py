# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def index():
    scrape = {'news_title': "Virginia Middle School Student Earns Honor of Naming NASA's Next Mars Rover",
 'news_p': 'NASA chose a seventh-grader from Virginia as winner of the agency\'s "Name the Rover" essay contest. Alexander Mather\'s entry for "Perseverance" was voted tops among 28,000 entries. ',
 'featured_image_url': 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA11591_hires.jpg',
 'mars_weather': 'InSight sol 457 (2020-03-10) low -95.7ºC (-140.3ºF) high -9.1ºC (15.6ºF)\nwinds from the SSE at 6.5 m/s (14.5 mph) gusting to 21.0 m/s (46.9 mph)\npressure at 6.30 hPa',
 'hemisphere_img_urls': [{'title': 'Cerberus Hemisphere Enhanced',
   'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif'},
  {'title': 'Schiaparelli Hemisphere Enhanced',
   'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif'},
  {'title': 'Syrtis Major Hemisphere Enhanced',
   'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif'},
  {'title': 'Valles Marineris Hemisphere Enhanced',
   'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif'}]}
    return render_template("index.html", dict=scrape)


if __name__ == "__main__":
    app.run(debug=True)
