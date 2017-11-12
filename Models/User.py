class User:
    def __init__(self, reddit_id, username, karma, relevant_comments, relevant_posts):
        self.reddit_id = reddit_id
        self.username = username
        self.karma = karma
        self.score = 0
        self.relevant_comments = relevant_comments
        self.relevant_posts = relevant_posts



