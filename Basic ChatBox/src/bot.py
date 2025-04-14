from nlp.processor import NLPProcessor

class Chatbot:
    def __init__(self):
        self.nlp_processor = NLPProcessor()
        self.conversation_history = []

    def get_user_input(self):
        return input("You: ")

    def respond(self, user_input):
        response = self.nlp_processor.generate_response(user_input)
        self.conversation_history.append({"user": user_input, "bot": response})
        print(f"Bot: {response}")

    def run(self):
        print("Chatbot is ready to chat! Type 'exit' to end the conversation.")
        while True:
            user_input = self.get_user_input()
            if user_input.lower() == 'exit':
                print("Chatbot: Goodbye!")
                break
            self.respond(user_input)

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.run()