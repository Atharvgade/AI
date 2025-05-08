# Expert System for Airline Scheduling and Cargo Scheduling

class KnowledgeBase:
    def __init__(self):
        self.flight_schedules = {
            "morning": "Flight A101 - Departure: 08:00 AM",
            "afternoon": "Flight B202 - Departure: 01:00 PM",
            "evening": "Flight C303 - Departure: 06:00 PM",
            "night": "Flight D404 - Departure: 11:00 PM"
        }
        self.cargo_schedules = {
            "perishable goods": "Scheduled for Morning Cargo Flight",
            "electronics": "Scheduled for Afternoon Cargo Flight",
            "documents": "Scheduled for Evening Cargo Flight",
            "heavy machinery": "Scheduled for Night Cargo Flight"
        }

class InferenceEngine:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def schedule_flight(self, preferred_time):
        preferred_time = preferred_time.lower()
        return self.kb.flight_schedules.get(preferred_time, "No scheduled flight available for the selected time.")

    def schedule_cargo(self, cargo_type):
        cargo_type = cargo_type.lower()
        return self.kb.cargo_schedules.get(cargo_type, "No cargo schedule available for the given item.")

class ExpertSystem:
    def __init__(self):
        self.kb = KnowledgeBase()
        self.engine = InferenceEngine(self.kb)

    def start(self):
        print("------ Airline Scheduling and Cargo Scheduling Expert System ------")
        mode = input("Select mode (flight/cargo): ").strip().lower()

        if mode == "flight":
            preferred_time = input("Enter preferred time slot (morning/afternoon/evening/night): ").strip().lower()
            flight_info = self.engine.schedule_flight(preferred_time)
            print(f"\nFlight Schedule: {flight_info}")

        elif mode == "cargo":
            cargo_type = input("Enter cargo type (e.g., perishable goods, electronics, documents, heavy machinery): ").strip().lower()
            cargo_info = self.engine.schedule_cargo(cargo_type)
            print(f"\nCargo Schedule: {cargo_info}")

        else:
            print("Invalid mode selected. Please restart and choose either 'flight' or 'cargo'.")

# Main Execution
if __name__ == "__main__":
    es = ExpertSystem()
    es.start()

