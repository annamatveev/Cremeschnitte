from Config.IndicativeWordsDictionary import IndicativeWordsDictionary


class SpanContentInCommentRule:
    description = "Remove comments that contain span"

    @staticmethod
    def execute_rule(reddit_comment):
        for message in IndicativeWordsDictionary.SPAM_COMMENTS:
            if message in reddit_comment.body.lower():
                return None
            else:
                return reddit_comment

    @staticmethod
    def calculate_score(reddit_post):
        return reddit_post.ups
