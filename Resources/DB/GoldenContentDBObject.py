from mongoengine import *
import datetime


class GoldenContentDBObject(Document):
    username = StringField(required=True, max_length=200)
    content_link = StringField(required=True, max_length=200)
    rule = StringField(required=True, max_length=200)
    title = StringField(required=True, max_length=3000)
    content_upvotes = IntField(required=True, max_length=200)
    content_score = IntField(required=True, max_length=200)
    user_score = IntField(required=True, max_length=200)
    karma = IntField(required=True, max_length=200)
    comments_in_subreddit = IntField(required=True, max_length=200)
    posts_in_subreddit = IntField(required=True, max_length=200)
    date_created = DateTimeField(default=datetime.datetime.utcnow)
    date_row_created = DateTimeField(default=datetime.datetime.utcnow)
