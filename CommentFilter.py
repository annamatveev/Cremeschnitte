import praw
import copy
from Comment import Comment

SPAM_MESSAGES = []
INDICATIVE_GOOD_TITLE_WORDS_DICTIONARY = ['tips', 'guide', 'advice']
INDICATIVE_ADVICE_WORDS_DICTIONARY = ['?', 'looking for']

class CommentFilter:
    def __init__(self, subreddit):
        self.comments = subreddit.comments(limit=500)
        self.subreddit = subreddit;
        self.golden_comments = []

    def filter_golden_comments(self):
        #self.filter_high_rated_comments()
        #self.filter_long_comments()
        #self.remove_spam_messages()
        self.filter_comments_to_indicative_words_post()
        self.print_golden_comments()

    def filter_long_comments(self):
        for reddit_comment in copy.copy(self.comments):
            if isinstance(reddit_comment, praw.models.Comment) and len(reddit_comment.body) > 1000:
                golden_comment = Comment(reddit_comment.body, reddit_comment.submission.title, reddit_comment.ups,
                                         reddit_comment, reddit_comment.submission.shortlink, reddit_comment.author,
                                         reddit_comment.created)
                self.golden_comments.append(golden_comment)

    def filter_high_rated_comments(self):
        for reddit_comment in copy.copy(self.comments):
            if isinstance(reddit_comment, praw.models.Comment) and reddit_comment.score > 5 and  len(reddit_comment.body) > 500:
                golden_comment = Comment(reddit_comment.body, reddit_comment.submission.title, reddit_comment.ups,
                                         reddit_comment, reddit_comment.submission.shortlink, reddit_comment.author,
                                         reddit_comment.created, "Highly rated comment")
                self.golden_comments.append(golden_comment)

    def filter_comments_to_indicative_words_post(self):
        for reddit_post in copy.copy(self.subreddit.new(limit=500)):
            title = reddit_post.title.lower()

            good_words_found = [word for word in INDICATIVE_GOOD_TITLE_WORDS_DICTIONARY if word in title]
            advice_words_found = [word for word in INDICATIVE_ADVICE_WORDS_DICTIONARY if word in title]

            if len(good_words_found) > 0 and len(advice_words_found) > 0:
                golden_post_comments = reddit_post.comments
                for reddit_comment in golden_post_comments:
                    if isinstance(reddit_comment, praw.models.Comment) and reddit_comment.score > 5 and  len(reddit_comment.body) > 500:
                        golden_comment = Comment(reddit_comment.body, reddit_comment.submission.title, reddit_comment.ups,
                                                 reddit_comment.permalink, reddit_comment.submission.shortlink, reddit_comment.author,
                                                 reddit_comment.created, "Highly voted comment for post with indicative words in title: "
                                         + ', '.join(good_words_found))
                        self.golden_comments.append(golden_comment)

    def remove_spam_messages(self):
        for comment in self.golden_comments:
            for message in SPAM_MESSAGES:
                if message in comment.body.lower():
                    self.golden_comments.remove(comment)

    def print_golden_comments(self):
        for comment in self.golden_comments:
            print("http://reddit.com/" + comment.comment_link + " " + str(comment.votes))
