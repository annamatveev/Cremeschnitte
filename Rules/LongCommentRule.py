from Config.QualityThersholds import QualityThresholds
from Decorators.UsersDecorator import UsersDecorator
from Models.RuleMatch import RuleMatch
from Models.Activity import Activity
from Models.Lead import Lead


class LongCommentRule:
    description = "Long comment"

    @staticmethod
    def execute_rule(reddit_comment):
        if QualityThresholds.is_long_comment(reddit_comment):
            match = RuleMatch(LongCommentRule.description,
                              QualityThresholds.content_quality_score(reddit_comment.body, reddit_comment.ups))
            golden_comment = Activity(reddit_comment.body,
                                      reddit_comment.submission.title,
                                      reddit_comment.ups,
                                      reddit_comment.permalink,
                                      reddit_comment.author.name,
                                      reddit_comment.created,
                                      match,
                                      reddit_comment)

            user = UsersDecorator.amend_user_details(reddit_comment.author)
            lead = Lead(golden_comment, user)
            return lead
