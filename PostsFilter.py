import copy
import re
from Post import Post

INDICATIVE_TITLE_WORDS_DICTIONARY = ['tips', 'guide', 'advice']
INDICATIVE_BAD_TITLE_WORDS_DICTIONARY = ['?', 'looking for']

class PostsFilter:

    def __init__(self, subreddit):
        self.posts = subreddit.new(limit=500)
        self.golden_posts = []

    def filter_golden_posts(self):
        self.find_high_rated_posts()
        self.find_indicative_words_in_post()
        self.print_golden_posts()

    def find_high_rated_posts(self):
        for reddit_post in copy.copy(self.posts):
            if len(reddit_post.selftext) > 1000 and reddit_post.ups > 15:
                golden_post = Post(reddit_post.selftext, reddit_post.title, reddit_post.ups, reddit_post.shortlink,
                                   reddit_post.author, reddit_post.created, "Long and highly rated post")
                self.golden_posts.append(golden_post)

    def find_indicative_words_in_post(self):
        for reddit_post in copy.copy(self.posts):
            title = reddit_post.title.lower()

            good_words_found = [word for word in INDICATIVE_TITLE_WORDS_DICTIONARY if word in title]
            bad_words_found = [word for word in INDICATIVE_BAD_TITLE_WORDS_DICTIONARY if word in title]

            if len(good_words_found) > 0 and len(bad_words_found) == 0:
                golden_post = Post(reddit_post.selftext, reddit_post.title, reddit_post.ups, reddit_post.shortlink,
                                   reddit_post.author, reddit_post.created, "Title has an indicative words in it: "
                                   + ', '.join(good_words_found)
                                                                         )
                self.golden_posts.append(golden_post)

    def print_golden_posts(self):
        for post in self.golden_posts:
            print(post.thread_link + " \t " + str(post.votes) + " \t " + post.rule + " \t " + post.title)
