import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://www.bbc.com/news'

response = requests.get(url)


if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    headlines = soup.find_all('h2')
    data = []

    print("Latest News Headlines:")

    for headline in headlines:
        text = headline.get_text().strip()
        data.append({'headline': text})

    # Convert the list of dictionaries into a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Visualizing the data
    # Count the occurrences of keywords in headlines
    keywords = ['Elon Musk', 'election', 'Russia', 'climate', 'health']
    counts = {keyword: df['headline'].str.contains(keyword, case=False, na=False).sum() for keyword in keywords}

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(counts.keys(), counts.values(), color='skyblue')
    plt.title('Frequency of Keywords in News Headlines')
    plt.xlabel('Keywords')
    plt.ylabel('Number of Occurrences')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
