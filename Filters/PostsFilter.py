from Rules.HighlyRatedPostRule import HighlyRatedPostRule
from Filters.ContentFilter import ContentFilter
import copy

from Rules.ContentPublishingTitlePostRule import ContentPublishingTitlePostRule


class PostsFilter(ContentFilter):

    def __init__(self, subreddit):
        self.posts = subreddit.new(limit=50)
        super(PostsFilter, self).__init__(subreddit)

    def filter_golden_posts(self):
        self.apply_rules(copy.copy(self.posts), [HighlyRatedPostRule, ContentPublishingTitlePostRule])


    def print_golden_posts(self):
        for post in self.golden_content:
            print(post.thread_link + " \t " + str(post.votes) + " \t " + post.rule + " \t " + post.title)
