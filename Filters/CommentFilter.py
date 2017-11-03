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
        self.apply_rules(copy.copy(self.comments), [LongCommentRule, HighlyRatedCommentRule])
        self.filter_comments_to_indicative_words_post()
        print(len(self.golden_content))

    def filter_comments_to_indicative_words_post(self):
        golden_post_with_indicative_words = self.apply_rules(self.subreddit.new(limit=PrawConfig.POST_LIMIT), [AskingForHelpTitlePostRule])
        if golden_post_with_indicative_words is not None:
            self.apply_rules(golden_post_with_indicative_words.reddit_content.comments,
                             [CommentToIndicativeWordsInTitleRule])

    def remove_spam_messages(self):
        for comment in copy.copy(self.comments):
            comment = SpanContentInCommentRule.execute_rule(comment)
            if comment is not None:  # Tagged as spam
                self.comments.remove(comment)

    def print_golden_comments(self):
        for comment in self.golden_content:
            print(PrawConfig.REDDIT_DOMAIN + comment.comment_link + " " + str(comment.votes))
