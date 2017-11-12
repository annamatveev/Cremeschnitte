class Activity:
    def __init__(self, reddit_id, body, title, upvotes, link, username, publish_date, match, reddit_content):
        self.reddit_id = reddit_id
        self.username = username
        self.link = link
        self.title = title
        self.body = body
        self.upvotes = upvotes
        self.match = match
        self.publish_date = publish_date
        self.reddit_content = reddit_content
