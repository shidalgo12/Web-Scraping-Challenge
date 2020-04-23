# Convert Jupyter notebook into a Python script that will execute all of your scraping code and return one Python dictionary 
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

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
  # print(mars)
  

  # ***MARS WEATHER***
  # ==================
  # Visit Twitter website
  weather_url = 'https://twitter.com/marswxreport?lang=en'
  browser.visit(weather_url)

  # Pause Web Scrape
  time.sleep(10)

  # Scrape page into Soup
  html = browser.html
  soup = bs(html, "html.parser")

  # Retrieve the latest Mars weather tweet
  mars_weather = soup.find('div', class_='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0').text

  # Add variable to master dictionary
  mars["mars_weather"]=mars_weather

  #   # ***MARS FACT TABLE***
  # # =====================
  # # Visit Fact Table Website
  # fact_url = 'https://space-facts.com/mars/'
  # browser.visit(fact_url)

  # # Scrape page into Soup
  # html = browser.html
  # soup = bs(html, "html.parser")

  # # Retrieve Mars Fact Table
  # fact_table = soup.find('table', class_='tablepress tablepress-id-p-mars')

  # # Add variable to master dictionary
  # mars['fact_table']= fact_table
  # print(mars)

  # # Visit Fact Table Website
  # fact_url = 'https://space-facts.com/mars/'
  # # browser.visit(fact_url)

  # # # Scrape page into Soup
  # # html = browser.html
  # # soup = bs(html, "html.parser")

  # # Retrieve Mars Fact Table
  # fact_table = pd.read_html(fact_url)

  # # Add variable to master dictionary
  
  # df =  fact_table[0]
  # df.columns= ["attribute", "values"]
  # html_table = df.to_html()
  # html_table = html_table.replace('\n', " ")
  # mars['facts']=html_table
  # print(mars)

  # ***MARS HEMISPHERE IMAGES***
  # ============================

  # Links to Hemisphere websites
  hem1_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
  hem2_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
  hem3_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
  hem4_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
  
# ***HEMISPHERE IMAGE 1***
  # Retrieve all elements that contain hemisphere image and title
  browser.visit(hem1_url)

  # Scrape page into Soup
  html = browser.html
  soup = bs(html, "html.parser")

  # Retrieve all elements that contain hemisphere image and title
  content = soup.find('section', class_='block metadata')
  # print(content)

  title1 = content.find('h2').text
  # print(title1)

  img_content = soup.find('div', class_='downloads')
  img_ul = img_content.find("ul")
  img_li= img_ul.find("li")
  img_link = img_li.find("a")
  href1 = img_link["href"]

  # hem_img_url
  mars['href1']= href1
  mars['title1']= title1
  
  # ***HEMISPHEERE IMAGE 2***
  # Retrieve all elements that contain hemisphere image and title
  browser.visit(hem2_url)

  # Scrape page into Soup
  html = browser.html
  soup = bs(html, "html.parser")

  # Retrieve all elements that contain hemisphere image and title
  content = soup.find('section', class_='block metadata')
  # print(content)

  title2 = content.find('h2').text
  # print(title1)

  img_content = soup.find('div', class_='downloads')
  img_ul = img_content.find("ul")
  img_li= img_ul.find("li")
  img_link = img_li.find("a")
  href2 = img_link["href"]
  # print(img_href1)

  # hem_img_url
  mars['href2']= href2
  mars['title2']= title2

  # ***HEMISPHEERE IMAGE 3***
  # Retrieve all elements that contain hemisphere image and title
  browser.visit(hem3_url)

  # Scrape page into Soup
  html = browser.html
  soup = bs(html, "html.parser")

  # Retrieve all elements that contain hemisphere image and title
  content = soup.find('section', class_='block metadata')
  # print(content)

  title3 = content.find('h2').text
  # print(title1)

  img_content = soup.find('div', class_='downloads')
  img_ul = img_content.find("ul")
  img_li= img_ul.find("li")
  img_link = img_li.find("a")
  href3 = img_link["href"]

  # hem_img_url
  mars['href3']= href3
  mars['title3']= title3

  # ***HEMISPHEERE IMAGE 4***
  # Retrieve all elements that contain hemisphere image and title
  browser.visit(hem4_url)

  # Scrape page into Soup
  html = browser.html
  soup = bs(html, "html.parser")

  # Retrieve all elements that contain hemisphere image and title
  content = soup.find('section', class_='block metadata')
  # print(content)

  title4 = content.find('h2').text
  # print(title1)

  img_content = soup.find('div', class_='downloads')
  img_ul = img_content.find("ul")
  img_li= img_ul.find("li")
  img_link = img_li.find("a")
  href4 = img_link["href"]

  # hem_img_url
  mars['href4']= href4
  mars['title4']= title4
  
  # Close browser after all web scrappings
  browser.quit()

  # Add Web Scrappings to MongoDB
  return mars

if __name__ == "__main__":
  print(scrape_info())



# # create a route called /scrape that will import your scrape_mars.py script and call your scrape function.
# @app.route("/scrape")
  # Store the return value in Mongo as a Python dictionary.

