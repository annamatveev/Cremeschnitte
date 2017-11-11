from Decorators.UsersDecorator import UsersDecorator

# TODO: make static


class ContentFilter:
    def __init__(self, subreddit):
        self.golden_content = []
        self.subreddit = subreddit

    @staticmethod
    def find_content_by_rules(contents, rules_list):
        golden_contents = []
        for content in contents:
            for rule in rules_list:
                lead = rule.execute_rule(content)
                if lead is not None:
                    golden_contents.append(lead)
        return golden_contents

    def modify_content_by_rules(self, contents, rules_list):
        golden_content = self.find_content_by_rules(contents, rules_list)
        self.golden_content += golden_content

    @staticmethod
    def resolve_duplicates(leads, unique_leads_so_far, reddit):
        for lead in leads:
            is_dup = False
            for leads_so_far in unique_leads_so_far:
                if leads_so_far.user.username == lead.activity.username:
                    leads_so_far.user.score += lead.activity.match.score
                    # is_dup = True

            if not is_dup:
                reddit_user = reddit.redditor(lead.activity.username)
                lead.user = UsersDecorator.amend_user_details(reddit_user)
                lead.user.score += lead.activity.match.score
                unique_leads_so_far.append(lead)

        return unique_leads_so_far
