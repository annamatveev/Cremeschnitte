import praw
import time
from User import User

class UsersFilter:

    def __init__(self):
        self.golden_users = []

    def find_user_info(self, reddit_user):
        comments_counter = 0
        posts_counter = 0

        time.sleep(10)

        user_comments = reddit_user.comments.new(limit=50)
        for reddit_comment in user_comments:
            if isinstance(reddit_comment, praw.models.Comment) and reddit_comment.subreddit == 'OverwatchUniversity':
                comments_counter += 1

        user_posts = reddit_user.submissions.new(limit=50)
        for reddit_post in user_posts:
            if reddit_post.subreddit == 'OverwatchUniversity':
                posts_counter += 1

        user = User(reddit_user.name, reddit_user.link_karma, comments_counter, posts_counter)
        return user