from Resources.DB.MongoDBWriter import MongoDBWriter
from Filters.CommentFilter import CommentFilter
from Filters.ContentFilter import ContentFilter
from Filters.PostsFilter import PostsFilter
from Resources.CSVWriter import CSVWriter
from Config.PrawConfig import PrawConfig
import datetime
import praw


def initialize_reddit_connection():
    r = praw.Reddit(client_id=PrawConfig.client_id,
                    client_secret=PrawConfig.client_secret,
                    password=PrawConfig.password,
                    user_agent=PrawConfig.user_agent,
                    username=PrawConfig.username)

    return r.subreddit(PrawConfig.SUBREDDIT)


subreddit = initialize_reddit_connection()

golden_content = []

comment_filter = CommentFilter(subreddit)
comment_filter.filter_golden_comments()

posts_filter = PostsFilter(subreddit)
posts_filter.filter_golden_posts()

ContentFilter.resolve_duplicates(comment_filter.golden_content, golden_content)
ContentFilter.resolve_duplicates(posts_filter.golden_content, golden_content)

writer = MongoDBWriter()
writer.connect()

for content in golden_content:
    readable_time = datetime.datetime.fromtimestamp(content.publish_date)
    user_profile_link = PrawConfig.REDDIT_USER_PROFILE_PREFIX + content.user.fullname
    writer.write_row(user_profile_link,
                     content.thread_link,
                     content.rule.description,
                     content.title,
                     content.votes,
                     readable_time,
                     content.rule.score,
                     content.user.score,
                     content.user.karma,
                     content.user.comments_num,
                     content.user.posts_num)


