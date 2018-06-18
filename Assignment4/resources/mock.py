import db
import ctx
import random
import feedparser
from datetime import datetime
import pandas as pd
from random import randrange
from datetime import timedelta
import manager

myDB = db.db

# ---------------------------------------------------------------------------------
# utils to generate random dates in future

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def get_next_rnd_date():
    d1 = datetime.strptime('1/1/2018 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('1/1/2019 4:50 AM', '%m/%d/%Y %I:%M %p')
    return random_date(d1, d2)


# ---------------------------------------------------------------------------------
# Load data from rss feeds

rss_event_feeds = [
    "http://www.brixn.at/feed/",
    "https://www.events-magazin.de/feed/"
    ]

url = 'cities.csv'
df = pd.read_csv(url, parse_dates=True, delimiter=",", decimal=",")


# ---------------------------------------------------------------------------------
# Start mocking

myDB.data["/locations"] = {}
myDB.data["/events"] = {}
myDB.data["/authors"] = {}


# ---------------------------------------------------------------------------------
# Mock location resource

for index, row in df.iterrows():
    myDB.data["/locations"][db.next_id()] = { 
            "name": row["city"],  
            "lat": row["lat"],
            "lng": row["lng"],
            "pop": row["pop"],
            "country": row["country"],
            "province": row["province"]
        }

location_ids = list(myDB.data["/locations"].keys())


# ---------------------------------------------------------------------------------
# Mock event resource

for url in rss_event_feeds:
    feed = feedparser.parse(url)
    for entry in feed[ "items" ]:   
       
        # ---------------------------------------------------------------------------------
        # add authors from feed to db

        authors = [author["name"] for author in entry["authors"]]
        authors_list = []
        for author_name in authors:
            author_id = db.next_id()

            author_entry = { 
                "name": author_name,
                "self": "{}/{}/{}".format(ctx.base_url, "authors", author_id) 
            }

            authors_list.append(author_entry)
            myDB.data["/authors"][author_id] = author_entry

        categories = [t.term for t in entry.get('tags', [])]

        event_id = db.next_id()
        location_id = random.choice(location_ids)
        location_name = myDB.data["/locations"][location_id]["name"]

        myDB.data["/events"][event_id] = { 
            "title": entry["title"], 
            "description": entry["description"], 
            "categories": categories, 
            "authors": authors_list, 
            "location": { 
                "id": location_id,
                "name": location_name,
                "self": "{}/{}/{}".format(ctx.base_url, "locations", location_id) 
            },
            "date": get_next_rnd_date(),
            "link": entry["link"],
            "self": "{}/{}/{}".format(ctx.base_url, "events", event_id) 
        }


# ---------------------------------------------------------------------------------
# Entry-Points (index)

myDB.data["/"] = {}
for resource in manager.get_all_resources():
    id = resource.strip("/")
    if not id:
        continue

    myDB.data["/"][id] = {
            "name": id,
            "self": "{}{}".format(ctx.base_url, resource) 
        }


myDB.data["/api"] = {
  "@context": "/hydra/api-demo/contexts/EntryPoint.jsonld",
  "@id": "/hydra/api-demo/",
  "@type": "EntryPoint",
  "issues": "/hydra/api-demo/isssssssssssssssssssues/",
  "register_user": "/hydra/api-demo/users/",
  "users": "/hydra/api-demo/users/"
}