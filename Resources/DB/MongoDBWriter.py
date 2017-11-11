from Resources.DB.Models.Activity import Activity
from Utils.CustomJSONEncoder import CustomEncoder
from Resources.DB.Models.Lead import Lead
from Resources.DB.Models.User import User
from mongoengine import *
import datetime
import json


class MongoDBWriter:

    def connect(self):
        connect('cremeshnitte')

    def add_user(self, contents, user):
        activity_db_object = Activity(
            username=contents.username,
            link=contents.link,
            title=contents.title,
            body=contents.body,
            upvotes=contents.upvotes,
            rule=contents.match.description,
            score=contents.match.score,
            date_created=datetime.datetime.fromtimestamp(contents.publish_date)
        )
        user_db_object = User(
            username=user.username,
            karma=user.karma,
            score=user.score,
            relevant_comments=user.relevant_comments,
            relevant_posts=user.relevant_posts

        )
        lead_db_object = Lead(username=user.username,
                              activity=[activity_db_object],
                              user=user_db_object
                              )
        lead_db_object.save()

    @staticmethod
    def is_user_exists(username):
        for user_details in Lead.objects:
            if username == user_details.username:
                return True
        return False

    @staticmethod
    def add_user_content(username, activity):
        Lead.objects(username=username).update(push__contents=activity)
