from Resources.DB.Models.Activity import Activity
from Resources.DB.Models.Lead import Lead
from Resources.DB.Models.User import User
from mongoengine import *
import datetime


class MongoDBWriter:

    @staticmethod
    def connect():
        connect('cremeschnitte')

    @staticmethod
    def add_lead(lead):
        activity_db_object = Activity(reddit_id=lead.activity.reddit_id,
                                      username=lead.activity.username,
                                      link=lead.activity.link,
                                      title=lead.activity.title,
                                      body=lead.activity.body,
                                      upvotes=lead.activity.upvotes,
                                      match=lead.activity.match.description,
                                      score=lead.activity.match.score,
                                      date_created=datetime.datetime.fromtimestamp(lead.activity.publish_date))
        user_db_object = User(reddit_id=lead.activity.reddit_id,
                              username=lead.user.username,
                              karma=lead.user.karma,
                              score=lead.user.score,
                              relevant_comments=lead.user.relevant_comments,
                              relevant_posts=lead.user.relevant_posts)
        lead_db_object = Lead(username=lead.user.username,
                              activity=[activity_db_object],
                              user=user_db_object)
        lead_db_object.save()

    @staticmethod
    def does_user_exist(user):
        for leads in Lead.objects:
            if user.username == leads.user.username:
                return True
        return False

    @staticmethod
    def does_lead_exist(lead):
        for lead_row in Lead.objects:
            if lead.user.username == lead_row.user.username:
                for activity in lead_row.activity:
                    if lead.activity.link == activity.link:
                        return True
        return False

    @staticmethod
    def add_lead_to_user(lead):
        activity_db_object = Activity(reddit_id=lead.activity.reddit_id,
                                      username=lead.activity.username,
                                      link=lead.activity.link,
                                      title=lead.activity.title,
                                      body=lead.activity.body,
                                      upvotes=lead.activity.upvotes,
                                      match=lead.activity.match.description,
                                      score=lead.activity.match.score,
                                      date_created=datetime.datetime.fromtimestamp(lead.activity.publish_date))
        Lead.objects(username=lead.user.username).update(push__activity=activity_db_object)
        Lead.objects(username=lead.user.username).update(date_updated=datetime.datetime.utcnow)
