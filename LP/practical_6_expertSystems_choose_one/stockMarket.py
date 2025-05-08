# Expert System for Stock Market Trading

class KnowledgeBase:
    def __init__(self):
        self.market_conditions = {
            ("bullish", "strong economy", "low interest rates"): "Recommendation: BUY high growth and technology stocks.",
            ("bearish", "recession", "high interest rates"): "Recommendation: SELL risky stocks, invest in bonds or safe assets.",
            ("volatile", "high inflation", "political instability"): "Recommendation: HOLD existing positions or invest in stable dividend stocks.",
            ("stable", "moderate growth", "controlled inflation"): "Recommendation: HOLD and monitor for opportunities."
        }

class InferenceEngine:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def suggest_trading_action(self, indicators):
        indicators_set = set(indicator.lower() for indicator in indicators)

        for condition_group, action in self.kb.market_conditions.items():
            if indicators_set.intersection(condition_group):
                return action
        return "Market condition unclear. Consult a financial advisor for personalized advice."

class ExpertSystem:
    def __init__(self):
        self.kb = KnowledgeBase()
        self.engine = InferenceEngine(self.kb)

    def start(self):
        print("------ Stock Market Trading Expert System ------")
        print("Please select market indicators you're observing:")

        indicators_list = [
            "bullish", "bearish", "volatile", "stable",
            "strong economy", "recession", "high inflation",
            "low interest rates", "high interest rates", "political instability", "moderate growth", "controlled inflation"
        ]

        print("\nAvailable Indicators:")
        for ind in indicators_list:
            print(f"- {ind}")

        selected_indicators = input("\nEnter observed indicators separated by commas: ").split(",")
        selected_indicators = [s.strip() for s in selected_indicators]

        recommendation = self.engine.suggest_trading_action(selected_indicators)
        print(f"\n{recommendation}")

# Main Execution
if __name__ == "__main__":
    es = ExpertSystem()
    es.start()

