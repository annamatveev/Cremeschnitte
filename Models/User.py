class User:
    def __init__(self, username, karma=None, relevant_comments=None, relevant_posts=None):
        self.username = username
        self.karma = karma
        self.score = 0
        self.relevant_comments = relevant_comments
        self.relevant_posts = relevant_posts



