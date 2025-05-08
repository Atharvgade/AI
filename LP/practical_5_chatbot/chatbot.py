"""
Elementary Chatbot for Movie Ticket Booking
"""

from nltk.chat.util import Chat, reflections

# Movie and showtime data
movies = {
    'Interstellar': ['10:00 AM', '2:00 PM', '6:00 PM'],
    'The Dark Knight': ['11:00 AM', '3:00 PM', '7:00 PM'],
    'Dune': ['9:30 AM', '1:30 PM', '5:30 PM']
}

# Patterns and responses
patterns = [
    (r'hi|hello|hey', 
     ['Hello! How can I assist you today?', 'Hey there! Ready to book some movie tickets?']),
    
    (r'how are you', 
     ['I am good! How can I help you with booking today?']),
    
    (r'(.*) movies?', 
     ['Currently playing: ' + ', '.join(movies.keys()) + '.']),
    
    (r'(.*) showtimes?', 
     ['Here are the showtimes: ' + '; '.join(f"{movie}: {', '.join(times)}" for movie, times in movies.items())]),
    
    (r'(.*) book tickets?', 
     ['Sure! Let\'s proceed with booking your tickets.']),
    
    (r'(bye|exit|goodbye)', 
     ['Goodbye! Enjoy your movie. See you again!']),
]

# Create chatbot
movie_bot = Chat(patterns, reflections)

# Booking function
def book_tickets():
    movie = input("Which movie would you like to watch? ")
    tickets = int(input("How many tickets do you want to book? "))
    showtime = input("Preferred showtime (e.g., 2:00 PM): ")
    price = 150  # per ticket
    total = price * tickets
    print(f"Booking confirmed for '{movie}' at {showtime}. Total amount: Rs. {total}. Enjoy your show.")

# Main function
def main():
    print("Welcome to MovieBot!")
    while True:
        user_input = input("You: ")
        response = movie_bot.respond(user_input)
        print("MovieBot:", response)

        if "book" in user_input.lower():
            book_tickets()
        
        if any(word in user_input.lower() for word in ['bye', 'exit', 'goodbye']):
            break

# Start chatbot
if __name__ == "__main__":
    main()

