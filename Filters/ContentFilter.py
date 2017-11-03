class ContentFilter:
    def __init__(self, subreddit):
        self.golden_content = []
        self.subreddit = subreddit

    def apply_rules(self, contents, rules_list):
        for content in contents:
            for rule in rules_list:
                golden_content = rule.execute_rule(content)
                if golden_content is not None and self.golden_content.count(content) == 0:
                    self.golden_content.append(golden_content)
