import requests
from bs4 import BeautifulSoup
import pdfkit

# send an HTTP request to the website you want to scrape
response = requests.get('https://www.example.com')

# parse the HTML content of the website
soup = BeautifulSoup(response.text, 'html.parser')

# find all the links on the website
links = soup.find_all('a')

# create an empty list to store the URLs
urls = []

# loop through the links and extract the URLs
for link in links:
    url = link.get('href')
    urls.append(url)

# convert the list of URLs to a PDF
pdfkit.from_url(urls, 'website.pdf')
