import praw
from CommentFilter import CommentFilter
from PostsFilter import PostsFilter

TOP_COMMENTS = 10
TOP_POSTS = 10

# MAIN
r = praw.Reddit(client_id='', client_secret='',
                     password='', user_agent='',
                     username='')

subreddit = r.subreddit('OverwatchUniversity')

comment_filter = CommentFilter(subreddit)
#comment_filter.filter_golden_comments()

posts_filter = PostsFilter(subreddit)
posts_filter.filter_golden_posts()

