# Expert System for Information Management

class KnowledgeBase:
    def __init__(self):
        self.documents = {
            "project report": "Stored in Server A under Project Files directory.",
            "financial record": "Stored in Server B under Finance Folder.",
            "employee data": "Stored in Server C under HR Documents.",
            "technical manual": "Stored in Server D under Technical Resources."
        }

class InferenceEngine:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def infer_location(self, document_type):
        document_type = document_type.lower()
        if document_type in self.kb.documents:
            return self.kb.documents[document_type]
        else:
            return "Document type not recognized. Please verify the document category."

class ExpertSystem:
    def __init__(self):
        self.kb = KnowledgeBase()
        self.engine = InferenceEngine(self.kb)

    def start(self):
        print("------ Information Management Expert System ------")
        doc_type = input("Enter the type of document you are looking for (e.g., project report, financial record): ")
        location = self.engine.infer_location(doc_type)
        print(f"Result: {location}")

# Main Execution
if __name__ == "__main__":
    es = ExpertSystem()
    es.start()

