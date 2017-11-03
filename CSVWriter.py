import csv
import datetime

from Config.PrawConfig import PrawConfig


class CSVWriter:

    @staticmethod
    def write_row(golden_content):
        with open('golden_redditors.csv', 'w') as csvfile:
            fieldnames = ['Username',
                          'Post/Comment Link',
                          'Rule',
                          'Post Title',
                          'Post/Comment Upvotes',
                          'Date Created',
                          'Score',
                          'Karma',
                          'Comments in subreddit',
                          'Posts in subreddit',
                          'Date Created (Unix Timestamp)'
                          ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for content in golden_content:
                readable_time = datetime.datetime.fromtimestamp(content.publish_date).strftime('%H:%M:%S %d-%m-%Y ')
                user_profile_link = PrawConfig.REDDIT_USER_PROGILE_PREFIX + content.user.fullname
                writer.writerow({'Username': user_profile_link,
                                 'Post/Comment Link': content.thread_link,
                                 'Post Title': content.title,
                                 'Rule': content.rule.description,
                                 'Post/Comment Upvotes': content.votes,
                                 'Date Created': readable_time,
                                 'Score': content.rule.score,
                                 'Karma': content.user.karma,
                                 'Comments in subreddit': content.user.comments_num,
                                 'Posts in subreddit': content.user.posts_num,
                                 'Date Created (Unix Timestamp)': content.publish_date})
