class ContentFilter:
    def __init__(self, subreddit):
        self.golden_content = []
        self.subreddit = subreddit

    def find_content_by_rules(self, contents, rules_list):
        golden_contents = []
        for content in contents:
            for rule in rules_list:
                golden_content = rule.execute_rule(content)
                if golden_content is not None and self.golden_content.count(content) == 0:
                    golden_contents.append(golden_content)
        return golden_contents

    def modify_content_by_rules(self, contents, rules_list):
        golden_content = self.find_content_by_rules(contents, rules_list)
        self.golden_content += golden_content
