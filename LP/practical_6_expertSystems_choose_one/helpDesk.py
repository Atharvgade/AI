# Expert System for Help Desk Management

class KnowledgeBase:
    def __init__(self):
        self.issue_department = {
            ("password reset", "account locked", "login issue"): "IT Support Team",
            ("software installation", "software update", "application error"): "Software Services Department",
            ("internet not working", "network downtime", "slow internet"): "Network Administration Team",
            ("printer not working", "hardware failure", "device not detected"): "Hardware Maintenance Unit"
        }

class InferenceEngine:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def find_department(self, issue_description):
        issue_description = issue_description.lower()
        for issue_group, department in self.kb.issue_department.items():
            if issue_description in issue_group:
                return department
        return "Issue not recognized. Please contact the general Help Desk."

class ExpertSystem:
    def __init__(self):
        self.kb = KnowledgeBase()
        self.engine = InferenceEngine(self.kb)

    def start(self):
        print("------ Help Desk Management Expert System ------")
        issue = input("Please describe your issue (e.g., password reset, internet not working): ").strip().lower()
        department = self.engine.find_department(issue)
        print(f"Suggested Department: {department}")

# Main Execution
if __name__ == "__main__":
    es = ExpertSystem()
    es.start()

