from Resources.DB.MongoDBWriter import MongoDBWriter
from Filters.CommentFilter import CommentFilter
from Filters.ContentFilter import ContentFilter
from Filters.PostsFilter import PostsFilter
from Config.PrawConfig import PrawConfig
import datetime
import praw


def initialize_reddit_connection():
    r = praw.Reddit(client_id=PrawConfig.client_id,
                    client_secret=PrawConfig.client_secret,
                    password=PrawConfig.password,
                    user_agent=PrawConfig.user_agent,
                    username=PrawConfig.username)

    return r


reddit = initialize_reddit_connection()

subreddit = reddit.subreddit(PrawConfig.SUBREDDIT)

comment_filter = CommentFilter(subreddit)
comment_filter.filter_golden_comments()

posts_filter = PostsFilter(subreddit)
posts_filter.filter_golden_posts()

leads = posts_filter.leads + comment_filter.leads

writer = MongoDBWriter()
writer.connect()

for lead in leads:
    if not MongoDBWriter.does_user_exist(lead.user):
        writer.add_lead(lead)
    else:
        if not MongoDBWriter.does_lead_exist(lead):
            writer.add_lead_to_user(lead)
