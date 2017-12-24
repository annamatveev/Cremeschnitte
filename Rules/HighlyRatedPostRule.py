from Config.QualityThersholds import QualityThresholds
from Decorators.UsersDecorator import UsersDecorator
from Models.RuleMatch import RuleMatch
from Models.Activity import Activity
from Models.Lead import Lead


class HighlyRatedPostRule:
    description = "Posted highly rated post"

    @staticmethod
    def execute_rule(reddit_post):
        if QualityThresholds.is_above_average_post(reddit_post):
            match = RuleMatch(HighlyRatedPostRule.description,
                              QualityThresholds.content_quality_score(reddit_post.selftext, reddit_post.ups))
            if reddit_post.author is None:  # User was deleted
                return
            golden_post = Activity(reddit_post.id,
                                   reddit_post.selftext,
                                   reddit_post.title,
                                   reddit_post.ups,
                                   reddit_post.shortlink,
                                   reddit_post.author.name,
                                   reddit_post.created,
                                   match,
                                   reddit_post)

            user = UsersDecorator.amend_user_details(reddit_post.author)
            lead = Lead(golden_post, user)
            return lead
