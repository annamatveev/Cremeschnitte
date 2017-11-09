from Resources.DB.GoldenContentDBObject import GoldenContentDBObject
from Config.PrawConfig import PrawConfig
from mongoengine import *
import datetime


class MongoDBWriter:

    def connect(self):
        connect('cremeshnitte')

    def write_row(self, golden_content):
        for content in golden_content:
            readable_time = datetime.datetime.fromtimestamp(content.publish_date)
            user_profile_link = PrawConfig.REDDIT_USER_PROFILE_PREFIX + content.user.fullname
            post = GoldenContentDBObject(username=user_profile_link,
                                         content_link=content.thread_link,
                                         rule=content.rule.description,
                                         title=content.title,
                                         content_upvotes=content.votes,
                                         date_created=readable_time,
                                         content_score=content.rule.score,
                                         user_score=content.user.score,
                                         karma=content.user.karma,
                                         comments_in_subreddit=content.user.comments_num,
                                         posts_in_subreddit=content.user.posts_num
                                         )
            post.save()

        for post in GoldenContentDBObject.objects:
            print('===' + post.title + '===')

        GoldenContentDBObject.objects.count()
