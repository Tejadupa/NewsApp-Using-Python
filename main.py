import requests
import json

query=input("Enter the topic : ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2024-10-16&sortBy=publishedAt&apiKey=021eb4df086448c6847caf0a75799b3f"
r=requests.get(url)
news=json.loads(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print(article["urlToImage"])
    print("------------------------------------------------------------------------->>>>>>>>>>")