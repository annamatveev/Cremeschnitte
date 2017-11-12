from mongoengine import *


class Activity(EmbeddedDocument):
    username = StringField(required=True, max_length=50)
    link = StringField(required=True, max_length=200)
    title = StringField(required=True, max_length=300)
    body = StringField(required=True, max_length=10000)
    upvotes = IntField(required=True)
    match = StringField(required=True, max_length=100)
    score = IntField(required=True)
    date_created = DateTimeField(required=True)
