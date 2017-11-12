import praw

from Config.PrawConfig import PrawConfig
from Filters.CommentFilter import CommentFilter
from Filters.PostsFilter import PostsFilter
from Resources.DB.MongoDBWriter import MongoDBWriter

r = praw.Reddit(client_id=PrawConfig.client_id,
                client_secret=PrawConfig.client_secret,
                password=PrawConfig.password,
                user_agent=PrawConfig.user_agent,
                username=PrawConfig.username)

subreddit = r.subreddit(PrawConfig.SUBREDDIT)

leads = CommentFilter.filter_leads(subreddit) + PostsFilter.filter_leads(subreddit)

writer = MongoDBWriter()
writer.connect()

for lead in leads:
    if not MongoDBWriter.does_user_exist(lead.user):
        writer.add_lead(lead)
    else:
        if not MongoDBWriter.does_lead_exist(lead):
            writer.add_lead_to_user(lead)
