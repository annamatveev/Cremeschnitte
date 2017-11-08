import praw
import time
from CSVWriter import CSVWriter
from Filters.PostsFilter import PostsFilter
from Filters.UsersFilter import UsersFilter
from Filters.CommentFilter import CommentFilter
from Config.PrawConfig import PrawConfig

golden_content = []
subreddit = {}


def find_duplicates(golden_content_with_dups):
    for golden_post in golden_content_with_dups:
        is_dup = False
        for original_golden_content in golden_content:
            if original_golden_content.user.fullname == golden_post.user.name:
                original_golden_content.user.score += golden_post.rule.score
                is_dup = True

        if not is_dup:
            try:
                golden_post.user = UsersFilter.find_user_info(golden_post.user)
                golden_post.user.score += golden_post.rule.score
                golden_content.append(golden_post)
            except:
                print("403 Error")


def initialize_reddit_connection():
    r = praw.Reddit(client_id=PrawConfig.client_id,
                    client_secret=PrawConfig.client_secret,
                    password=PrawConfig.password,
                    user_agent=PrawConfig.user_agent,
                    username=PrawConfig.username)

    subreddit = r.subreddit(PrawConfig.SUBREDDIT)


comment_filter = CommentFilter(subreddit)
comment_filter.filter_golden_comments()

posts_filter = PostsFilter(subreddit)
posts_filter.filter_golden_posts()

find_duplicates(comment_filter.golden_content);
find_duplicates(posts_filter.golden_content)

writer = CSVWriter()
writer.write_row(golden_content)
