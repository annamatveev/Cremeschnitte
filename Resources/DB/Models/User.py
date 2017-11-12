from mongoengine import *

class User(EmbeddedDocument):
    reddit_id = StringField(required=True, max_length=50)
    username = StringField(required=True, max_length=50)
    karma = IntField(required=True)
    score = IntField(required=True)
    relevant_comments = IntField(required=True)
    relevant_posts = IntField(required=True)
