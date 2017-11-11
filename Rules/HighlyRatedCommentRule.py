from Config.QualityThersholds import QualityThresholds
from Models.Lead import Lead
from Models.RuleMatch import RuleMatch
from Models.Activity import Activity
from Models.User import User
import praw


class HighlyRatedCommentRule:
    description = "Highly rated comment"

    @staticmethod
    def execute_rule(reddit_comment):
        if isinstance(reddit_comment, praw.models.Comment) \
                and QualityThresholds.is_high_rated_comment(reddit_comment):
            match = RuleMatch(HighlyRatedCommentRule.description,
                              QualityThresholds.content_quality_score(reddit_comment.body, reddit_comment.ups))
            golden_comment = Activity(reddit_comment.body,
                                      reddit_comment.submission.title,
                                      reddit_comment.ups,
                                      reddit_comment.permalink,
                                      reddit_comment.author.name,
                                      reddit_comment.created,
                                      match,
                                      reddit_comment)
            user = User(reddit_comment.author.name)
            lead = Lead(golden_comment, user)
            return lead
