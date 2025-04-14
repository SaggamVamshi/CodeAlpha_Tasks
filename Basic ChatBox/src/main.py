import os
from utils.helpers import load_data

def respond(user_input, training_data):
    """Generate a response based on user input and training data."""
    if any(greeting.lower() in user_input.lower() for greeting in training_data['greetings']):
        return "Hi there! How can I help you today?"
    else:
        return "I'm not sure how to respond to that."

def main():
    # Ensure directories exist
    os.makedirs('C:/Users/SAGGAM ARUN/OneDrive/Desktop/Basic ChatBox/text-chatbot/data', exist_ok=True)
    os.makedirs('C:/Users/SAGGAM ARUN/OneDrive/Desktop/Basic ChatBox/text-chatbot/logs', exist_ok=True)

    # Load training data
    training_data_path = 'C:/Users/SAGGAM ARUN/OneDrive/Desktop/Basic ChatBox/text-chatbot/data/training_data.json'
    if os.path.exists(training_data_path):
        training_data = load_data(training_data_path)
        print("Training data loaded:", training_data)
    else:
        print(f"File not found: {training_data_path}")
        return

    # Interactive chat loop
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye!")
            break
        response = respond(user_input, training_data)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
