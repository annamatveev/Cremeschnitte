from Resources.DB.GoldenContentDBObject import GoldenContentDBObject
from Config.PrawConfig import PrawConfig
from mongoengine import *
import datetime


class MongoDBWriter:

    def connect(self):
        connect('cremeshnitte')

    def write_row(self, username, content_link, rule, title, content_upvotes, date_created, content_score, user_score,
                  karma, comments_in_subreddit, posts_in_subreddit):
        post = GoldenContentDBObject(username=username,
                                     content_link=content_link,
                                     rule=rule,
                                     title=title,
                                     content_upvotes=content_upvotes,
                                     date_created=date_created,
                                     content_score=content_score,
                                     user_score=user_score,
                                     karma=karma,
                                     comments_in_subreddit=comments_in_subreddit,
                                     posts_in_subreddit=posts_in_subreddit
                                     )
        post.save()
