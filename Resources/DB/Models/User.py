from mongoengine import *
import datetime


class User(EmbeddedDocument):
    username = StringField(required=True, max_length=50)
    karma = IntField(required=True)
    score = IntField(required=True)
    relevant_comments = IntField(required=True)
    relevant_posts = IntField(required=True)
