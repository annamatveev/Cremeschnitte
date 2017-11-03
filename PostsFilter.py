import copy
from HighlyRatedPostRule import HighlyRatedPostRule
from ContentPublishingTitlePostRule import ContentPublishingTitlePostRule


class PostsFilter:

    def __init__(self, subreddit):
        self.posts = subreddit.new(limit=5)
        self.golden_posts = []

    def filter_golden_posts(self):
        # self.find_high_rated_posts()
        self.find_indicative_words_in_post()

    def find_high_rated_posts(self):
        for reddit_post in copy.copy(self.posts):
            golden_post = HighlyRatedPostRule.execute_rule(reddit_post)
            if golden_post is not None:
                self.golden_posts.append(golden_post)

    def find_indicative_words_in_post(self):
        for reddit_post in copy.copy(self.posts):
            golden_post = ContentPublishingTitlePostRule.execute_rule(reddit_post)
            if golden_post is not None:
                self.golden_posts.append(golden_post)

    def print_golden_posts(self):
        for post in self.golden_posts:
            print(post.thread_link + " \t " + str(post.votes) + " \t " + post.rule + " \t " + post.title)
