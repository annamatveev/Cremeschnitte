from Config.PrawConfig import PrawConfig
from Rules.ContentPublishingTitlePostRule import ContentPublishingTitlePostRule
from Rules.Pipe import Pipe
from Rules.HighlyRatedPostRule import HighlyRatedPostRule


# TODO: make static


class PostsFilter:

    @staticmethod
    def filter_leads(subreddit):
        return Pipe.run(subreddit.new(limit=PrawConfig.COMMENT_LIMIT),
                        [HighlyRatedPostRule, ContentPublishingTitlePostRule])
