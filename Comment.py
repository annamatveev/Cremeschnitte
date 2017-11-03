from Content import Content


class Comment(Content):
    def __init__(self, body, title, votes, comment_link, thread_link, user, publish_date, rule):
        super(Comment, self).__init__(body, title, votes, thread_link, user, publish_date, rule)
        self.comment_link  = comment_link


