import praw
from CommentFilter import CommentFilter
from PostsFilter import PostsFilter
from UsersFilter import UsersFilter
from CSVWriter import CSVWriter

r = praw.Reddit(client_id='', client_secret='',
                     password='', user_agent='',
                     username='')

subreddit = r.subreddit('OverwatchUniversity')

comment_filter = CommentFilter(subreddit)
comment_filter.filter_golden_comments()

posts_filter = PostsFilter(subreddit)
# posts_filter.filter_golden_posts()
users_filter = UsersFilter()
writer = CSVWriter()

# for golden_post in posts_filter.golden_posts:
#    golden_user = users_filter.find_user_info(golden_post.user)
#    golden_post.user = golden_user
# writer.write_row(posts_filter.golden_posts)

for golden_comment in comment_filter.golden_comments:
    golden_user = users_filter.find_user_info(golden_comment.user, subreddit)
    golden_comment.user = golden_user

writer.write_row(comment_filter.golden_comments)

