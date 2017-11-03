from Post import Post
from RuleMatch import RuleMatch
from QualityThersholds import QualityThresholds


class HighlyRatedPostRule:
    description = "Long and highly rated post"

    @staticmethod
    def execute_rule(reddit_post):
        if QualityThresholds.is_above_average_post(reddit_post):
            match = RuleMatch(HighlyRatedPostRule.description, HighlyRatedPostRule.calculate_score(reddit_post))
            golden_post = Post(reddit_post.selftext,
                               reddit_post.title,
                               reddit_post.ups,
                               reddit_post.shortlink,
                               reddit_post.author,
                               reddit_post.created,
                               match,
                               reddit_post)

            return golden_post

    @staticmethod
    def calculate_score(reddit_post):
        return len(reddit_post.selftext) / 100 + reddit_post.ups