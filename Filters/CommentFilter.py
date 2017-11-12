from Config.PrawConfig import PrawConfig
from Rules.AskingForHelpTitlePostRule import AskingForHelpTitlePostRule
from Rules.CommentToIndicativeWordsInTitleRule import CommentToIndicativeWordsInTitleRule
from Rules.Pipe import Pipe
from Rules.HighlyRatedCommentRule import HighlyRatedCommentRule
from Rules.LongCommentRule import LongCommentRule


class CommentFilter:

    @staticmethod
    def filter_leads(subreddit):
        return Pipe.run(subreddit.comments(limit=PrawConfig.COMMENT_LIMIT),
                        [LongCommentRule, HighlyRatedCommentRule]) \
               + CommentFilter.filter_comment_leads_in_indicative_words_post(subreddit)

    @staticmethod
    def filter_comment_leads_in_indicative_words_post(subreddit):
        leads = []
        post_leads_with_indicative_words = Pipe.run(subreddit.new(limit=PrawConfig.POST_LIMIT),
                                                                          [AskingForHelpTitlePostRule])
        if post_leads_with_indicative_words is not None:
            comments_on_posts = [lead.activity.reddit_content.comments for lead in
                                 post_leads_with_indicative_words if len(lead.activity.reddit_content.comments) > 0]
            for comment_thread in comments_on_posts:
                leads += Pipe.run(comment_thread, [CommentToIndicativeWordsInTitleRule])
        return leads
