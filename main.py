import requests
from bs4 import BeautifulSoup
import csv
import time
time.sleep(2)

url = "https://quotes.toscrape.com/"
data = []

while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        tags = [tag.text for tag in quote.find_all("a", class_="tag")]

        data.append([text, author, ", ".join(tags)])

    
    next_button = soup.find("li", class_="next")

    if next_button:
        next_link = next_button.find("a")["href"]
        url = "https://quotes.toscrape.com" + next_link
    else:
        break


with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tags"])
    writer.writerows(data)

print("All pages scraped automatically")