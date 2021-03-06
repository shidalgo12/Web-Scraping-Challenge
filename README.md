# Web Scraping

## Background

A web application created scraping data from 8 different websites related to the Mission to Mars.  All data later displayed in a single HTML page. Initial scraping completed in a Jupyter Notebook, using BeautifulSoup, Pandas, and Requests/Splinter coding and later converted into a Python Script.  MongoDB used with Flask templating to insert all scraped information into the HTML file.

## Scraping

All data scraped and stored into a Python dictionary and sent to a MongoDB database to be used when building the HTML Page. 


#### NASA Mars News
Web elements observed to extract the latest News Title and Paragraph Text.

https://mars.nasa.gov/news/

#### JPL Mars Space - Featured Image
JPL website visited to scrape the data of the current feature image. Splinter coding was used to navigate the site and assign the URL string to a variable added to the dictionary.

https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars


#### Mars Weather
Mars Weather twitter account visited to scrape the latest Mars weather tweet. 

https://twitter.com/marswxreport?lang=en

#### Mars Facts
Pandas library used to scrape the table containing facts about the planet including Diameter, Mass, etc.  Data was then converted to an HTML table string allowing for visualization on the HTML page.

https://space-facts.com/mars/

#### Mars Hemispheres
High resolution images obtained for each of Mar's hemispheres.  The image URL string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name stored into the Python dictionary.

https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars

## MongoDB and Flask Application
MongoDB and Flask templating was run to update the structured HTML page that displays all the information that was scraped from the URLs above.

* Route created to import python script and run the scrape function.

* Return data stored in MongoDB as a Python dictionary.

* Mongo database queried to pass the mars data into an HTML template to display the data.

* HTML file created to display all the data in the appropriate HTML elements.

* HTML button used to renew queries and display the latest changing data.

![](Images/html_page1.png)
![](Images/html_page2.png)
![](Images/html_page3.png)
![](Images/html_page4.png)