from Config.QualityThersholds import QualityThresholds
from Models.Lead import Lead
from Models.RuleMatch import RuleMatch
from Models.Activity import Activity
from Models.User import User


class HighlyRatedPostRule:
    description = "Long and highly rated post"

    @staticmethod
    def execute_rule(reddit_post):
        if QualityThresholds.is_above_average_post(reddit_post):
            match = RuleMatch(HighlyRatedPostRule.description,
                              QualityThresholds.content_quality_score(reddit_post.selftext, reddit_post.ups))
            golden_post = Activity(reddit_post.selftext,
                                   reddit_post.title,
                                   reddit_post.ups,
                                   reddit_post.shortlink,
                                   reddit_post.author.name,
                                   reddit_post.created,
                                   match,
                                   reddit_post)
            user = User(reddit_post.author.name)
            lead = Lead(golden_post, user)
            return lead
