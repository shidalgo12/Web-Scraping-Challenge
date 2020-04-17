# Convert Jupyter notebook into a Python script that will execute all of your scraping code and return one Python dictionary 
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

# def init_browser():
#     # @NOTE: Replace the path with your actual path to the chromedriver
#     # executable_path = {'C:/Users/admin/HW/Web-Scraping-Challenge/Missions_to_Mars': 'chromedriver.exe'}
#     return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = Browser('chrome')

    # Visit news website
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get latest news title
    news = soup.find_all('div', class_='content_title')
    print(news[1].text)

    # Get latest news paragraph
    paragraph = soup.find('div', class_="article_teaser_body").text
    print(paragraph)

    # Store data in a dictionary
    mars = {
        "news": news,
        "paragraph": paragraph
    }
    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars