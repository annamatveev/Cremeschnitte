from Rules.CommentToIndicativeWordsInTitleRule import CommentToIndicativeWordsInTitleRule
from Rules.AskingForHelpTitlePostRule import AskingForHelpTitlePostRule
from Rules.SpamContentInCommentRule import SpanContentInCommentRule
from Rules.HighlyRatedCommentRule import HighlyRatedCommentRule
from Rules.LongCommentRule import LongCommentRule
from Filters.ContentFilter import ContentFilter
from Config.PrawConfig import PrawConfig
import copy


class CommentFilter(ContentFilter):

    def __init__(self, subreddit):
        self.comments = subreddit.comments(limit=PrawConfig.COMMENT_LIMIT)
        super(CommentFilter, self).__init__(subreddit)

    def filter_golden_comments(self):
        self.modify_content_by_rules(copy.copy(self.comments), [LongCommentRule, HighlyRatedCommentRule])
        self.filter_comments_to_indicative_words_post()
        var = []

    def filter_comments_to_indicative_words_post(self):
        golden_post_with_indicative_words = self.find_content_by_rules(self.subreddit.new(limit=PrawConfig.POST_LIMIT),
                                                             [AskingForHelpTitlePostRule])
        if golden_post_with_indicative_words is not None:
            posts_comments = [post.reddit_content.comments for post in golden_post_with_indicative_words
                        if len(post.reddit_content.comments) > 0]
            for comment_thread in posts_comments:
                self.modify_content_by_rules(comment_thread, [CommentToIndicativeWordsInTitleRule])

    def remove_spam_messages(self):
        for comment in copy.copy(self.comments):
            comment = SpanContentInCommentRule.execute_rule(comment)
            if comment is not None:  # Tagged as spam
                self.comments.remove(comment)
