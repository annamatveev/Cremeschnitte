from Config.QualityThersholds import QualityThresholds
from Models.RuleMatch import RuleMatch
from Models.Post import Post


class HighlyRatedPostRule:
    description = "Long and highly rated post"

    @staticmethod
    def execute_rule(reddit_post):
        if QualityThresholds.is_above_average_post(reddit_post):
            match = RuleMatch(HighlyRatedPostRule.description,
                              QualityThresholds.content_quality_score(reddit_post.selftext, reddit_post.ups))
            golden_post = Post(reddit_post.selftext,
                               reddit_post.title,
                               reddit_post.ups,
                               reddit_post.shortlink,
                               reddit_post.author,
                               reddit_post.created,
                               match,
                               reddit_post)

            return golden_post
