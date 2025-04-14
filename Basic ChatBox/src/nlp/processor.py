class NLPProcessor:
    def __init__(self):
        import nltk
        from nltk.chat.util import Chat, reflections
        
        # Ensure necessary NLTK resources are downloaded
        nltk.download('punkt')
        
        self.reflections = reflections
        self.chatbot = Chat(self.pairs, self.reflections)

    def process_input(self, user_input):
        # Tokenize the user input
        tokens = nltk.word_tokenize(user_input)
        return tokens

    def generate_response(self, user_input):
        # Generate a response based on user input
        response = self.chatbot.respond(user_input)
        return response

    # Example pairs for the chatbot
    pairs = [
        (r'hi|hello|hey', ['Hello!', 'Hi there!']),
        (r'how are you?', ['I am doing well, thank you!', 'I am just a computer program, but thanks for asking!']),
        (r'quit', ['Bye! Take care!']),
    ]