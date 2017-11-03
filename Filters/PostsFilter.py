from Rules.HighlyRatedPostRule import HighlyRatedPostRule
from Filters.ContentFilter import ContentFilter
import copy

from Rules.ContentPublishingTitlePostRule import ContentPublishingTitlePostRule


class PostsFilter(ContentFilter):

    def __init__(self, subreddit):
        self.posts = subreddit.new(limit=50)
        super(PostsFilter, self).__init__(subreddit)

    def filter_golden_posts(self):
        # self.find_high_rated_posts()
        self.find_indicative_words_in_post()

    def find_high_rated_posts(self):
        for reddit_post in copy.copy(self.posts):
            golden_post = HighlyRatedPostRule.execute_rule(reddit_post)
            if golden_post is not None and self.golden_content.count(reddit_post) == 0:
                self.golden_content.append(golden_post)

    def find_indicative_words_in_post(self):
        for reddit_post in copy.copy(self.posts):
            golden_post = ContentPublishingTitlePostRule.execute_rule(reddit_post)
            if golden_post is not None and self.golden_content.count(reddit_post) == 0:
                self.golden_content.append(golden_post)

    def print_golden_posts(self):
        for post in self.golden_content:
            print(post.thread_link + " \t " + str(post.votes) + " \t " + post.rule + " \t " + post.title)
