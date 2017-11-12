from Decorators.UsersDecorator import UsersDecorator

# TODO: make static


class ContentFilter:
    def __init__(self, subreddit):
        self.leads = []
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
        leads = self.find_content_by_rules(contents, rules_list)
        self.leads += leads
        self.leads += leads