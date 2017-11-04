class QualityThresholds:

    # Comments
    average_comment_upvotes = 2
    average_comment_body_length = 400
    high_rated_comment_upvotes = 20
    long_comment_body_length = 600

    # Posts
    average_post_upvotes = 10
    average_post_body_length = 500
    high_rated_post_upvotes = 20
    long_post_body_length = 1000

    @staticmethod
    def is_long_post(post):
        return QualityThresholds.is_above_average_post(post) \
               and len(post.body) > QualityThresholds.long_comment_body_length

    @staticmethod
    def is_long_comment(comment):
        return QualityThresholds.is_above_average_comment(comment) \
               and len(comment.body) > QualityThresholds.long_comment_body_length

    @staticmethod
    def is_high_rated_comment(comment):
        return QualityThresholds.is_above_average_comment(comment) \
               and comment.ups > QualityThresholds.high_rated_comment_upvotes

    @staticmethod
    def is_high_rated_post(post):
        return QualityThresholds.is_above_average_post(post) \
               and post.ups > QualityThresholds.high_rated_post_upvotes

    @staticmethod
    def is_above_average_post(post):
        return post.ups > QualityThresholds.average_post_upvotes \
               and len(post.selftext) > QualityThresholds.average_post_body_length

    @staticmethod
    def is_above_average_comment(comment):
        return comment.ups > QualityThresholds.average_comment_upvotes \
               and len(comment.body) > QualityThresholds.average_comment_body_length

    @staticmethod
    def content_quality_score(content, upvotes):
        return len(content) / 100 + upvotes
