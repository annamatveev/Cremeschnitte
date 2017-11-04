import praw
from CSVWriter import CSVWriter
from Filters.PostsFilter import PostsFilter
from Filters.UsersFilter import UsersFilter
from Filters.CommentFilter import CommentFilter
from Config.PrawConfig import PrawConfig

r = praw.Reddit(client_id=PrawConfig.client_id,
                client_secret=PrawConfig.client_secret,
                password=PrawConfig.password,
                user_agent=PrawConfig.user_agent,
                username=PrawConfig.username)

subreddit = r.subreddit(PrawConfig.SUBREDDIT)

comment_filter = CommentFilter(subreddit)
comment_filter.filter_golden_comments()

posts_filter = PostsFilter(subreddit)
posts_filter.filter_golden_posts()

users_filter = UsersFilter()

golden_content = []
count = 0
print(len(comment_filter.golden_content + posts_filter.golden_content))

for golden_comment in comment_filter.golden_content:
    print(count)

    # Find duplicates
    dup = False
    for unique_golden_comment in golden_content:
        if unique_golden_comment.user.fullname == golden_comment.user.name:
            unique_golden_comment.user.score += golden_comment.rule.score
            dup = True
    if not dup:
        golden_comment.user = users_filter.find_user_info(golden_comment.user)
        golden_comment.user.score = golden_comment.rule.score
        golden_content.append(golden_comment)

    count += 1

for golden_post in posts_filter.golden_content:
    print(count)
    # Find duplicates
    dup = False
    for unique_golden_post in golden_content:
        if unique_golden_post.user.fullname == golden_post.user.name:
            unique_golden_post.user.score += golden_post.rule.score
            dup = True
    if not dup:
        golden_post.user = users_filter.find_user_info(golden_post.user)
        golden_post.user.score = golden_post.rule.score
        golden_content.append(golden_post)
    count += 1

writer = CSVWriter()
writer.write_row(golden_content)
