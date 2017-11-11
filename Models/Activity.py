class Activity:
    def __init__(self, body, title, upvotes, link, username, publish_date, match, reddit_content):
        self.username = username
        self.link = link
        self.title = title
        self.body = body
        self.upvotes = upvotes
        self.match = match
        self.publish_date = publish_date
        self.reddit_content = reddit_content
