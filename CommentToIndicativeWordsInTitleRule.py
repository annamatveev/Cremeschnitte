from Comment import Comment
import praw
from RuleMatch import RuleMatch
from QualityThersholds import QualityThresholds


class CommentToIndicativeWordsInTitleRule:
    description = "Highly rated comment to indicative words in title"

    @staticmethod
    def execute_rule(reddit_comment):
        if isinstance(reddit_comment, praw.models.Comment) \
                and QualityThresholds.is_high_rated_comment(reddit_comment):
            match = RuleMatch("Highly voted comment for post with indicative words in title",
                              CommentToIndicativeWordsInTitleRule.calculate_score(reddit_comment))
            golden_comment = Comment(reddit_comment.body,
                                     reddit_comment.submission.title,
                                     reddit_comment.ups,
                                     reddit_comment.permalink,
                                     reddit_comment.submission.shortlink,
                                     reddit_comment.author,
                                     reddit_comment.created,
                                     match,
                                     reddit_comment)
            return golden_comment

    @staticmethod
    def calculate_score(reddit_post):
        return reddit_post.ups
