from Post import Post
from RuleMatch import RuleMatch
from IndicativeWordsDictionary import IndicativeWordsDictionary
from QualityThersholds import QualityThresholds

class ContentPublishingTitlePostRule:
    description = "Indicative words for content publishing in title"

    @staticmethod
    def execute_rule(reddit_post):
        title = reddit_post.title.lower()

        content_words_found = [word for word in IndicativeWordsDictionary.GUIDE_CONTENT if word in title]
        advice_words_found = [word for word in IndicativeWordsDictionary.ASKING_FOR_HELP if word in title]

        if len(content_words_found) > 0 and len(advice_words_found) == 0 \
                and QualityThresholds.is_above_average_post(reddit_post):
            match = RuleMatch(ContentPublishingTitlePostRule.description + ': ' + ', '.join(content_words_found),
                              ContentPublishingTitlePostRule.calculate_score(reddit_post))
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
        return reddit_post.ups
