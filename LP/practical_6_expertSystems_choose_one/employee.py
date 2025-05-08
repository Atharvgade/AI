# Expert System for Employee Performance Evaluation

class KnowledgeBase:
    def __init__(self):
        self.criteria_weights = {
            "punctuality": 10,
            "task completion": 20,
            "teamwork": 15,
            "innovation": 15,
            "leadership": 20,
            "communication skills": 20
        }
        self.evaluation_scale = {
            (80, 100): "Outstanding",
            (60, 79): "Very Good",
            (40, 59): "Good",
            (20, 39): "Average",
            (0, 19): "Needs Improvement"
        }

class InferenceEngine:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def calculate_performance(self, scores):
        total_score = 0
        for criterion, score in scores.items():
            weight = self.kb.criteria_weights.get(criterion, 0)
            total_score += (score / 10) * weight  # Normalize score (out of 10)

        percentage = (total_score / 100) * 100  # Total weight = 100
        for (lower, upper), grade in self.kb.evaluation_scale.items():
            if lower <= percentage <= upper:
                return grade, percentage
        return "Unable to Evaluate", percentage

class ExpertSystem:
    def __init__(self):
        self.kb = KnowledgeBase()
        self.engine = InferenceEngine(self.kb)

    def start(self):
        print("------ Employee Performance Evaluation Expert System ------")
        print("Please provide ratings for each criteria (0 to 10):")
        
        scores = {}
        for criterion in self.kb.criteria_weights.keys():
            while True:
                try:
                    score = float(input(f"Rate {criterion.title()}: "))
                    if 0 <= score <= 10:
                        scores[criterion] = score
                        break
                    else:
                        print("Please enter a score between 0 and 10.")
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")

        grade, percentage = self.engine.calculate_performance(scores)
        print(f"\nFinal Evaluation: {grade}")
        print(f"Performance Percentage: {percentage:.2f}%")

# Main Execution
if __name__ == "__main__":
    es = ExpertSystem()
    es.start()

