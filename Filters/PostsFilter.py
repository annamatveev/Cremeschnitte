from Rules.ContentPublishingTitlePostRule import ContentPublishingTitlePostRule
from Rules.HighlyRatedPostRule import HighlyRatedPostRule
from Config.PrawConfig import PrawConfig
from Rules.Pipe import Pipe


# TODO: make static


class PostsFilter:

    @staticmethod
    def filter_leads(subreddit):
        return Pipe.run(subreddit.new(limit=PrawConfig.COMMENT_LIMIT),
                        [HighlyRatedPostRule, ContentPublishingTitlePostRule])
