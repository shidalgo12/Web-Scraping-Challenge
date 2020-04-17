# Convert Jupyter notebook into a Python script that will execute all of your scraping code and return one Python dictionary 
from splinter import Browser
from bs4 import BeautifulSoup as bs

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

def scrape_info():
  browser = Browser('chrome')
  mars = {}

  # ***MARS NEWS***
  # ===============
  # Visit news website
  news_url = "https://mars.nasa.gov/news/"
  browser.visit(news_url)

  # Scrape page into Soup
  html = browser.html
  soup = bs(html, "html.parser")

  # Get latest news title
  news = soup.find_all('div', class_='content_title')

  # Get latest news paragraph
  paragraph = soup.find('div', class_="article_teaser_body").text

  # DOES NOT WORK - Add variables to master dictionary
  mars["news"]=news[1].text
  mars["paragraph"]=paragraph

  # # Store data in a dictionary
  # mars = {
  #   "news": news[1].text,
  #   "paragraph": paragraph,
  #   # "table": fact_table
  # }

  # # Close the browser after scraping
  # browser.quit()

  # ***MARS FEATURED IMAGE***
  # =========================
  # Visit news website
  image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
  browser.visit(image_url)
  browser.find_by_id("full_image").click()
  browser.find_link_by_partial_text("more info").click()

  # Scrape page into Soup
  html = browser.html
  soup = bs(html, "html.parser")

  # Retrieve all elements that contain featured image
  feature = soup.find('figure', class_='lede')

  featured_href = feature.a.img["src"]

  featured_image_url = ('https://www.jpl.nasa.gov' + featured_href)
  

  # Add featured_image_url to master dictionary
  mars['featured_image_url']= featured_image_url
  print(mars)
  # Close the browser after scraping
  # browser.quit()

  # ***MARS WEATHER***
  # ==================
  # # Visit Twitter website
  # weather_url = 'https://twitter.com/marswxreport?lang=en'
  # browser.visit(weather_url)

  # # Scrape page into Soup
  # html = browser.html
  # soup = bs(html, "html.parser")

  # # Retrieve the latest Mars weather tweet
  # mars_weather = soup.find('div', class_='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0').text

  # # Add variable to master dictionary
  # mars["mars_weather"]=mars_weather
  
  # # Close the browser after scraping
  # browser.quit()

  # ***MARS FACT TABLE***
  # =====================
  # # Visit Fact Table Website
  # fact_url = 'https://space-facts.com/mars/'
  # browser.visit(fact_url)

  # # Scrape page into Soup
  # html = browser.html
  # soup = bs(html, "html.parser")

  # # Retrieve Mars Fact Table
  # fact_table = soup.find('table', class_='tablepress tablepress-id-p-mars')

  # # Close the browser after scraping
  # browser.quit()

  # ***MARS HEMISPHERE IMAGES***
  # ============================

  # Return results
  return mars

if __name__ == "__main__":
  print(scrape_info())



# # create a route called /scrape that will import your scrape_mars.py script and call your scrape function.
# @app.route("/scrape")
  # Store the return value in Mongo as a Python dictionary.

