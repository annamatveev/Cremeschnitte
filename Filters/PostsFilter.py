from Rules.ContentPublishingTitlePostRule import ContentPublishingTitlePostRule
from Rules.HighlyRatedPostRule import HighlyRatedPostRule
from Filters.ContentFilter import ContentFilter
from Config.PrawConfig import PrawConfig
import copy

# TODO: make static


class PostsFilter(ContentFilter):

    def __init__(self, subreddit):
        self.posts = subreddit.new(limit=PrawConfig.POST_LIMIT)
        super(PostsFilter, self).__init__(subreddit)

    def filter_golden_posts(self):
        self.modify_content_by_rules(copy.copy(self.posts), [HighlyRatedPostRule, ContentPublishingTitlePostRule])
