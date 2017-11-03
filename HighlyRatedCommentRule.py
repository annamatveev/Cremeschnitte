from Comment import Comment
import praw
from RuleMatch import RuleMatch


class HighlyRatedCommentRule:
    description = "Long and highly rated comment"
    upvotes_threshold = 20
    post_body_length_threshold = 500

    @staticmethod
    def execute_rule(reddit_comment):
        if isinstance(reddit_comment, praw.models.Comment) \
                and reddit_comment.score > HighlyRatedCommentRule.upvotes_threshold \
                and len(reddit_comment.body) > HighlyRatedCommentRule.post_body_length_threshold:
            match = RuleMatch(HighlyRatedCommentRule.description, HighlyRatedCommentRule)
            golden_comment = Comment(reddit_comment.body,
                                     reddit_comment.submission.title,
                                     reddit_comment.ups,
                                     reddit_comment.submission.shortlink,
                                     reddit_comment.permalink,
                                     reddit_comment.author,
                                     reddit_comment.created,
                                     match,
                                     reddit_comment)

            return golden_comment

    @staticmethod
    def calculate_score(reddit_comment):
        return len(reddit_comment.selftext) / 100 + reddit_comment.ups