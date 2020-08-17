import requests
from bs4 import BeautifulSoup
import os
import pymongo


cluster = pymongo.MongoClient(
    "mongodb+srv://Zach:X.oEyXBdG3C62@cluster0.b4an6.mongodb.net/<sample_airbnb>?retryWrites=true&w=majority"
)
db = cluster["InvestLikeTheBest"]
collection = db["Podcasts"]


class Episode:
    myFile = "episodes.csv"

    def __init__(self, number, guest, title, link):
        self.number = number
        self.guest = guest
        self.title = title
        self.link = link

    def __repr__(self):
        return f"Ep.{self.number} - {self.guest}"

    def to_csv(self):
        with open(Episode.myFile, "a") as f:
            f.write(f"{self.number},{self.guest},{self.title},{self.link}\n")

    def mongo(self):
        return {
            "_id": self.number,
            "guest": self.guest,
            "title": self.title,
            "link": self.link,
        }


class Information:
    def __init__(self, guest):
        self.guest = guest


base_url = "http://investorfieldguide.com/podcast"


def get_some_data():
    soup = BeautifulSoup(requests.get(base_url).text, features="html.parser")
    lst = soup.select("p a")[3:]
    success, fail = 0, 0
    for item in lst[3:]:

        # print(item)
        text = item.text.split(" – ")
        if len(text) == 3:
            ep = Episode(text[0].strip("Ep."), text[1], text[2], item.attrs["href"])

            collection.insert_one(ep.mongo())
            # ep.to_csv()
            success += 1
        else:
            fail += 1
        # for some of the first episodes, number and guest are not separated by ( big dash )
        # if len(text) == 2:
        # print(text[0])  # includes both number and guest

    print(f"{success} successes")
    print(f"{fail} failures")
    print(f"{success/(success+fail) * 100}% successful")


if __name__ == "__main__":
    get_some_data()

