import praw

from Config.QualityThersholds import QualityThresholds
from Models.Comment import Comment
from Models.RuleMatch import RuleMatch


class LongCommentRule:
    description = "Long comment"

    @staticmethod
    def execute_rule(reddit_comment):
        if isinstance(reddit_comment, praw.models.Comment) \
                and QualityThresholds.is_long_comment(reddit_comment):
            match = RuleMatch(LongCommentRule.description,
                              QualityThresholds.content_quality_score(reddit_comment.body, reddit_comment.ups))
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
