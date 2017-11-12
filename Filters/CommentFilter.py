from Rules.CommentToIndicativeWordsInTitleRule import CommentToIndicativeWordsInTitleRule
from Rules.AskingForHelpTitlePostRule import AskingForHelpTitlePostRule
from Rules.HighlyRatedCommentRule import HighlyRatedCommentRule
from Rules.LongCommentRule import LongCommentRule
from Config.PrawConfig import PrawConfig
from Rules.Pipe import Pipe


class CommentFilter:

    @staticmethod
    def filter_leads(subreddit):
        return Pipe.run(subreddit.comments(limit=PrawConfig.COMMENT_LIMIT),
                        [LongCommentRule, HighlyRatedCommentRule]) \
               + CommentFilter.filter_comment_leads_in_posts(subreddit)

    @staticmethod
    def filter_comment_leads_in_posts(subreddit):
        leads = []
        post_leads_with_indicative_words = Pipe.run(subreddit.new(limit=PrawConfig.POST_LIMIT),
                                                    [AskingForHelpTitlePostRule])
        if post_leads_with_indicative_words is not None:
            comments_on_posts = [lead.activity.reddit_content.comments for lead in
                                 post_leads_with_indicative_words if len(lead.activity.reddit_content.comments) > 0]
            for comment_thread in comments_on_posts:
                leads += Pipe.run(comment_thread, [CommentToIndicativeWordsInTitleRule])
        return leads
