import requests
from bs4 import BeautifulSoup

url = "https://learncodinganywhere.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
# Extracting the title of the webpage
title_element = soup.find('title')
if title_element:
    page_title = title_element.text
    print("Title of the webpage:", page_title)
else:
    print("Title element not found.")

url = "https://learncodinganywhere.com/codingbootcamps"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# Extracting the title of this webpage
title_element = soup.find('title')
if title_element:
    page_title = title_element.text
    print("Title of the webpage:", page_title)
else:    
    print("Title element not found.")

#Scrape and display the footer of the webpage "https://learncodinganywhere.com/"

url = "https://learncodinganywhere.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
footer_element = soup.find('footer')
if footer_element:
    footer_text = footer_element.text.strip()
    print("Footer of the webpage:", footer_text)
else:
    print("Footer element not found.")
    