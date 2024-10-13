import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = 'https://www.bbc.com/news'

response = requests.get(url)


if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    headlines = soup.find_all('h2')
    data = []

    print("Latest News Headlines:")

    for headline in headlines:
        text = headline.get_text().strip()  # Get the text and strip any extra whitespace
        data.append({'headline': text})     # Store each headline as a dictionary

    # Convert the list of dictionaries into a pandas DataFrame
    df = pd.DataFrame(data)
    print(df)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
