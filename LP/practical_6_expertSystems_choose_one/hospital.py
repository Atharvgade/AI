# Expert System for Hospitals and Medical Facilities

class KnowledgeBase:
    def __init__(self):
        self.symptoms_disease = {
            ("fever", "cough", "shortness of breath"): "COVID-19",
            ("fever", "headache", "fatigue"): "Influenza (Flu)",
            ("nausea", "vomiting", "abdominal pain"): "Food Poisoning"
        }
        self.hospital_directory = {
            "COVID-19": ["City Care Hospital", "Global Health Clinic"],
            "Influenza (Flu)": ["Metro Hospital", "Sunrise Medical Center"],
            "Food Poisoning": ["Green Valley Hospital", "Wellness Clinic"]
        }

class InferenceEngine:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def diagnose(self, symptoms):
        symptoms_set = set(symptoms)

        for symptom_group, disease in self.kb.symptoms_disease.items():
            if symptoms_set.issuperset(symptom_group):
                hospitals = self.kb.hospital_directory.get(disease, [])
                return disease, hospitals
        return "Unknown Condition", []

class ExpertSystem:
    def __init__(self):
        self.kb = KnowledgeBase()
        self.engine = InferenceEngine(self.kb)

    def start(self):
        print("------ Hospital and Medical Facilities Expert System ------")
        print("Please answer the following questions with 'yes' or 'no':")
        
        symptoms_input = []
        symptoms_list = ["fever", "cough", "shortness of breath", "headache", "fatigue", "nausea", "vomiting", "abdominal pain"]

        for symptom in symptoms_list:
            ans = input(f"Do you have {symptom}? (yes/no): ").strip().lower()
            if ans == "yes":
                symptoms_input.append(symptom)

        disease, hospitals = self.engine.diagnose(symptoms_input)
        
        if disease != "Unknown Condition":
            print(f"\nDiagnosis: {disease}")
            print("Recommended Hospitals:")
            for hospital in hospitals:
                print(f"- {hospital}")
        else:
            print("\nUnable to diagnose based on the symptoms provided. Please consult a medical professional.")

# Main Execution
if __name__ == "__main__":
    es = ExpertSystem()
    es.start()

