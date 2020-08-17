import pymongo

# cluster = pymongo.MongoClient(
#     "mongodb+srv://Zach:X.oEyXBdG3C62@cluster0.b4an6.mongodb.net/<sample_airbnb>?retryWrites=true&w=majority"
# )
# db = cluster["InvestLikeTheBest"]
# collection = db["Podcasts"]


def create():
    cluster = pymongo.MongoClient(
        "mongodb+srv://Zach:X.oEyXBdG3C62@cluster0.b4an6.mongodb.net/<sample_airbnb>?retryWrites=true&w=majority"
    )
    db = cluster["InvestLikeTheBest"]
    return db


quotes = [
    {
        "_id": 1,
        "episode": 184,
        "quote": "Mindset of, even when in a difficult scenario, you can operate with grace.",
    },
    {
        "_id": 2,
        "episode": 184,
        "quote": "People are intuitive. They're empathic beings. They sense energy even through voice only or a Zoom and certainly in person. And if you're belittling someone else in your mind, even if you think you're covering it, you're not.",
    },
    {
        "_id": 3,
        "episode": 184,
        "quote": "Brand is the promise that a consumer believes that entity makes to them through how it communicates itself.",
    },
    {
        "_id": 4,
        "episode": 184,
        "quote": "Real brand sustainability comes down to two things, which is relevance and differentiation. And everything fits into one of those two buckets. Something either affects a brand's relevance. It is meaningful to my life today and its differentiation. It is unique and I can identify that uniqueness.",
    },
    {
        "_id": 5,
        "episode": 184,
        "quote": "And so it's either virtuous or vicious when you start extending the brand, that there is a way to actually strengthen a brand as it shows up in more places. It's not easy but there is a way.",
    },
    {
        "_id": 6,
        "episode": 184,
        "quote": "Do I really care if they're awesome at this thing they're going to do one time, or do I care that they're going to be awesome at the thing they're going to need to do over 20 years?",
    },
    {
        "_id": 7,
        "episode": 184,
        "quote": "And I learned that there were times where we really had the rose-colored glasses on as it related to the value that our brand would bring to someone else.",
    },
    {
        "_id": 8,
        "episode": 184,
        "quote": "And the lesson in that is that people who are close to the action know what the right thing to do is long before the leader makes the decision.",
    },
    {
        "_id": 9,
        "episode": 184,
        "quote": "I call it my “hot shot rule” where I envision a badass in my role tomorrow and I ask myself: what is one thing they would look at and immediately address.",
    },
    {
        "_id": 10,
        "episode": 184,
        "quote": "So I think the best advice I could offer is for anyone listening to just constantly check in with themselves. Give yourself permission to be on a journey.",
    },
]

db = create()
# podcasts["Quotes"].insert_many(quotes)
db.Quotes.find_one({"episode": 184})

