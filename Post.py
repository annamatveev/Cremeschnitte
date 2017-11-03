from Content import Content


class Post(Content):
    def __init__(self, body, title, votes, thread_link, user, publish_date, rule, reddit_post):
        super(Post, self).__init__(body, title, votes, thread_link, user, publish_date, rule, reddit_post)
