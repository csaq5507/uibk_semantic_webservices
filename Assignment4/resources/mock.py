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

def get_random_item(items):
    return items[randrange(0, len(items)- 1)]

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
    #"http://www.brixn.at/feed/",
    #"https://www.events-magazin.de/feed/"
    ]

url = 'cities.csv'
cities_df = pd.read_csv(url, parse_dates=True, delimiter=",", decimal=",")


# ---------------------------------------------------------------------------------
# Start mocking

myDB.data["/locations"] = {}
myDB.data["/events"] = {}
myDB.data["/authors"] = {}



# ---------------------------------------------------------------------------------
# Mock location resource

location_ids = []
for index, row in cities_df.iterrows():
    id = db.next_id()
    location_ids.append(id)
    myDB.add_(id, "locations", {
        "@context": "/api/contexts/Location.jsonld",
        "@type": "http://schema.org/City",
        "name": row["city"],  
        "latitude": row["lat"],
        "longitude": row["lng"],
        "population": row["pop"],
        "countryAddress": row["country"],
        "state": row["province"],
        "@id": "http://localhost:5000/api/locations/{}".format(id)
    })



id = db.next_id()
myDB.add_(id, "reviews", {
  "@context": "/api/contexts/Review.jsonld",
  "@type": "http://schema.org/Review",
  "author": "Author 1",
  "reviewBody": "review 1",
  "@id": "http://localhost:5000/api/reviews/" + id
})

id = db.next_id()
myDB.add_(id, "reviews", {
  "@context": "/api/contexts/Review.jsonld",
  "@type": "http://schema.org/Review",
  "author": "Author 2",
  "reviewBody": "review 2",
  "@id": "http://localhost:5000/api/reviews/" + id
})

# ---------------------------------------------------------------------------------
# Mock event resource

author_ids = []
for i in range(0, 10): 
    id = db.next_id()
    author_ids.append(id)
    myDB.add_(id, "authors", {
        "@context": "/api/contexts/Author.jsonld",
        "@type": "http://schema.org/Author",
        "familyName": "Musterman " + str(i),
        "givenName": "Max" + str(i),
        "email": "max.musterman.{}@hotmail.com".format(i),
        "@id": "http://localhost:5000/api/authors/" + str(id)
    })

actor_ids = []
for i in range(0, 10): 
    id = db.next_id()
    actor_ids.append(id)
    myDB.add_(id, "actors", {
        "@context": "/api/contexts/Actor.jsonld",
        "@type": "http://schema.org/Actor",
        "familyName": "Musterman " + str(i),
        "givenName": "Max" + str(i),
        "gender": "male",
        "birthDate": "01.02.2003",
        "@id": "http://localhost:5000/api/actors/" + str(id)
    })

event_ids = []
for i in range(0, 10): 
    id = db.next_id()
    event_ids.append(id)
    myDB.add_(id, "events", {
    "@context": "/api/contexts/Event.jsonld",
    "@type": "https://schema.org/Event",
    "name": "Event {}".format(id),
    "actor": "/api/actors/{}".format(random.choice(actor_ids)),
    "location": "/api/locations/{}".format(random.choice(location_ids)),
    "description": "Event for {}".format(id),
    "start_date": get_next_rnd_date(),
    "end_date": get_next_rnd_date(),
    "@id": "/api/events/{}".format(id)
    })


review_ids = []
for i in range(0, 10): 
    id = db.next_id()
    review_ids.append(id)
    myDB.add_(id, "reviews", {
        "@context": "/api/contexts/Review.jsonld",
        "@type": "http://schema.org/Review",
        "reviewBody": "Review number " + str(i),
        "itemReviewed": "/api/events/{}".format(random.choice(event_ids)),
        "@id": "http://localhost:5000/api/reviews/" + str(id)
    })

rating_ids = []
for i in range(0, 10): 
    id = db.next_id()
    review_ids.append(id)
    myDB.add_(id, "ratings", {
        "@context": "/api/contexts/Rating.jsonld",
        "@type": "http://schema.org/Rating",
        "author": "/api/authors/{}".format(random.choice(author_ids)),
        "ratingValue": random.choice([0,1,2,3,4,5]),
        "itemRated": "/api/events/{}".format(random.choice(event_ids)),
        "@id": "http://localhost:5000/api/ratings/" + str(id)
    })







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

        test_entry = {
            "@context": "/api/contexts/Event.jsonld",
            "@id": "/api/events/139",
            "@type": "Event",
            "name": "Halloween",
            "description": "This is halloween, this is halloween",
            "start_date": "2015-10-31T00:00:00Z",
            "end_date": "2015-10-31T23:59:59Z"
        }

        myDB.add("event", test_entry)


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