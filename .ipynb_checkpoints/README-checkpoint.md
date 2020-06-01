# Web Scraping

## Background

A web application created scraping data from various websites related to the Mission to Mars.  All data later displayed in a single HTML page. Initial scraping completed in a Jupyter Notebook, using BeautifulSoup, Pandas, and Requests/Splinter coding.

## Scraping


### NASA Mars News
https://mars.nasa.gov/news/

The latest News Title and Paragraph Text scraped and assigned to variables that were added into a master dictionary for future referene. the text to variables that you can reference later.


### JPL Mars Space Images - Featured Image
https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars


Visit the url for JPL Featured Space Image here.


Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.


Make sure to find the image url to the full size .jpg image.


Make sure to save a complete url string for this image.



### Mars Weather
https://twitter.com/marswxreport?lang=en
Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called mars_weather.


### Mars Facts
https://space-facts.com/mars/
Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.


Use Pandas to convert the data to a HTML table string.



### Mars Hemispheres
https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars

Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.


You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.


Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.


Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.



#### MongoDB and Flask Application
Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.


Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.


Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.

Store the return value in Mongo as a Python dictionary.



Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.


Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.


