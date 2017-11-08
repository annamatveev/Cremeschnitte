from Filters.UsersFilter import UsersFilter


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

    @staticmethod
    def resolve_duplicates(golden_content_unique_type, golden_content_unique_users):
        print(len(golden_content_unique_users))
        for golden_content in golden_content_unique_type:
            is_dup = False
            for original_golden_content in golden_content_unique_users:
                if original_golden_content.user.fullname == golden_content.user.name:
                    original_golden_content.user.score += golden_content.rule.score
                    is_dup = True

            if not is_dup:
                try:
                    golden_content.user = UsersFilter.find_user_info(golden_content.user)
                    golden_content.user.score += golden_content.rule.score
                    golden_content_unique_users.append(golden_content)
                except:
                    pass

        return golden_content_unique_users
