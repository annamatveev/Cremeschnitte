import csv
import datetime


class CSVWriter:

    @staticmethod
    def write_row(golden_posts):
        with open('golden_redditors.csv', 'w') as csvfile:
            fieldnames = ['Username', 'Post/Comment Link', 'Rule', 'Post Title', 'Post/Comment Upvotes', 'Date Created', 'Karma',
                          'Comments in subreddit', 'Posts in subreddit','Date Created (Unix Timestamp)']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for post in golden_posts:
                readable_time = datetime.datetime.fromtimestamp(post.publish_date).strftime('%H:%M:%S %d-%m-%Y ')
                user_profile_link = 'http://www.reddit.com/user/' + post.user.fullname
                writer.writerow({'Username': user_profile_link,
                                 'Post/Comment Link': post.thread_link,
                                 'Post Title': post.title,
                                 'Rule': post.rule,
                                 'Post/Comment Upvotes': post.votes,
                                 'Date Created': readable_time,
                                 'Karma': post.user.karma,
                                 'Comments in subreddit': post.user.comments_num,
                                 'Posts in subreddit': post.user.posts_num,
                                 'Date Created (Unix Timestamp)': post.publish_date})
