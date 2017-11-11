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

golden_content = []

comment_filter = CommentFilter(subreddit)
comment_filter.filter_golden_comments()

posts_filter = PostsFilter(subreddit)
posts_filter.filter_golden_posts()

ContentFilter.resolve_duplicates(comment_filter.golden_content, golden_content, reddit)
ContentFilter.resolve_duplicates(posts_filter.golden_content, golden_content, reddit)

writer = MongoDBWriter()
writer.connect()

for lead in golden_content:
    readable_time = datetime.datetime.fromtimestamp(lead.activity.publish_date)
    user_profile_link = PrawConfig.REDDIT_USER_PROFILE_PREFIX + lead.activity.username
    if not MongoDBWriter.is_user_exists(user_profile_link):
        writer.add_user(lead.activity, lead.user)
    else:
        writer.add_user_content(user_profile_link, lead.content)
