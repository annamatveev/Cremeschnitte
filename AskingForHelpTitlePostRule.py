from Post import Post
from RuleMatch import RuleMatch
from IndicativeWordsDictionary import IndicativeWordsDictionary


class AskingForHelpTitlePostRule:
    description = "Indicative words in title that ask for help"
    upvotes_threshold = 5
    post_body_length_threshold = 1000

    @staticmethod
    def execute_rule(reddit_post):
        title = reddit_post.title.lower()

        good_words_found = [word for word in IndicativeWordsDictionary.GUIDE_CONTENT if word in title]
        bad_words_found = [word for word in IndicativeWordsDictionary.ASKING_FOR_HELP if word in title]

        if len(good_words_found) > 0 and len(bad_words_found) > 0:
            match = RuleMatch(AskingForHelpTitlePostRule.description + ': ' + ', '.join(good_words_found),
                              AskingForHelpTitlePostRule.calculate_score(reddit_post))
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
