from Content import Content


class Comment(Content):
    def __init__(self, body, title, votes, parent_link, permalink, user, publish_date, rule, reddit_comment):
        full_link = 'http://www.reddit.com' + permalink
        super(Comment, self).__init__(body, title, votes, full_link, user, publish_date, rule, reddit_comment)
        self.parent_link = parent_link


