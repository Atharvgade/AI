import random

class ElementaryChatbot:
    def __init__(self):
        # Predefined responses for various types of user inputs
        self.greetings = ["Hello!", "Hi there!", "Greetings!"]
        self.goodbyes = ["Goodbye!", "See you later!", "Bye!"]
        self.responses = {
            "how are you": ["I'm good, thank you!", "I'm doing well, how about you?"],
            "your name": ["I'm a chatbot, you can call me Bot.", "I don't have a name, just call me Bot."],
            "joke": [
                "Why don't scientists trust atoms? Because they make up everything!",
                "What do you call fake spaghetti? An impasta!"
            ],
            "default": ["I'm not sure how to respond to that.", "Sorry, I didn't understand."]
        }

    def greet(self):
        # Print a random greeting message
        print(random.choice(self.greetings))

    def respond(self, user_input):
        # Convert input to lowercase for simple keyword matching
        user_input_lower = user_input.lower()
        for key, value in self.responses.items():
            if key in user_input_lower:
                return random.choice(value)
        # Return default response if no keyword matched
        return random.choice(self.responses["default"])

    def say_goodbye(self):
        # Print a random goodbye message
        print(random.choice(self.goodbyes))

    def chat(self):
        # Main loop for chatbot interaction
        self.greet()
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                self.say_goodbye()
                break
            response = self.respond(user_input)
            print(f"Bot: {response}")

# Start chatbot when this script is run
if __name__ == "__main__":
    bot = ElementaryChatbot()
    bot.chat()
