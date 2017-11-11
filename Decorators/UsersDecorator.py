from Config.PrawConfig import PrawConfig
from Models.User import User
import praw


class UsersDecorator:

    @staticmethod
    def amend_user_details(reddit_user):
        comments_counter = 0
        posts_counter = 0

        user_comments = reddit_user.comments.new(limit=PrawConfig.USERS_NEW_COMMENTS_LIMIT)
        for reddit_comment in user_comments:
            if isinstance(reddit_comment, praw.models.Comment) \
                    and reddit_comment.subreddit.display_name == PrawConfig.SUBREDDIT:
                comments_counter += 1

        user_posts = reddit_user.submissions.new(limit=PrawConfig.USERS_NEW_COMMENTS_LIMIT)
        for reddit_post in user_posts:
            if reddit_post.subreddit.display_name == PrawConfig.SUBREDDIT:
                posts_counter += 1

        user = User(reddit_user.name, reddit_user.link_karma, comments_counter, posts_counter)
        return user
