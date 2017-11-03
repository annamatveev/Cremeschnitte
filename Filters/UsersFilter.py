from Models.User import User
import praw


class UsersFilter:

    def __init__(self):
        self.golden_users = []

    @staticmethod
    def find_user_info(reddit_user, relevant_subreddit):
        comments_counter = 0
        posts_counter = 0

        user_comments = reddit_user.comments.new(limit=5)
        for reddit_comment in user_comments:
            if isinstance(reddit_comment, praw.models.Comment) and reddit_comment.subreddit == 'OverwatchUniversity':
                comments_counter += 1

        user_posts = reddit_user.submissions.new(limit=5)
        for reddit_post in user_posts:
            if reddit_post.subreddit == relevant_subreddit.name:
                posts_counter += 1

        user = User(reddit_user.name, reddit_user.link_karma, comments_counter, posts_counter)
        return user