import requests
from bs4 import BeautifulSoup
import time

def card_url():
    for pages in range(1, 7):
        url = f"https://scrapingclub.com/exercise/list_basic/?page={pages}"

        response = requests.get(url)
        site = BeautifulSoup(response.text, "lxml")

        blocks = site.find_all("div", class_="w-full rounded border")
        for block in blocks:
            block_url = "https://scrapingclub.com" + block.find("a").get("href")
            yield block_url

def array():
    for url in card_url():
        response = requests.get(url)
        site = BeautifulSoup(response.text, "lxml")
        time.sleep(1)

        card_block = site.find("div", class_="my-8 w-full rounded border")

        title = card_block.find("h3").text
        price = card_block.find("h4").text
        description = card_block.find("p").text
        picture = "https://scrapingclub.com" + card_block.find("img").get("src")

        yield title, price, description, picture
