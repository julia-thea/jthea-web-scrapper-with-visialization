import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://www.bbc.com/news'

# Send a request to fetch the content of the webpage
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all headlines in <h2> tags (Modify the tag based on the website structure)
    headlines = soup.find_all('h2')

    # Print each headline
    print("Latest News Headlines:")
    for headline in headlines:
        print(headline.get_text())
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
