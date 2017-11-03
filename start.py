import praw
from CSVWriter import CSVWriter
from Filters.PostsFilter import PostsFilter
from Filters.UsersFilter import UsersFilter
from Filters.CommentFilter import CommentFilter

r = praw.Reddit(client_id='', client_secret='',
                     password='', user_agent='',
                     username='')

subreddit = r.subreddit('OverwatchUniversity')

comment_filter = CommentFilter(subreddit)
comment_filter.filter_golden_comments()

posts_filter = PostsFilter(subreddit)
posts_filter.filter_golden_posts()

users_filter = UsersFilter()

golden_content = []

for golden_comment in comment_filter.golden_content:
    if any(content.user.fullname == golden_comment.user.fullname for content in
           golden_content) is not None:  # User exists in other content
        golden_user = users_filter.find_user_info(golden_comment.user, subreddit)
        golden_comment.user = golden_user
        golden_content.append(golden_comment)

for golden_post in posts_filter.golden_content:
    if any(content.user.fullname == golden_post.user.name for content in
           golden_content) is not None: # User exists in other content
        golden_user = users_filter.find_user_info(golden_post.user, subreddit)
        golden_post.user = golden_user
        golden_content.append(golden_post)

writer = CSVWriter()
writer.write_row(comment_filter.golden_content)
writer.write_row(posts_filter.golden_content)

