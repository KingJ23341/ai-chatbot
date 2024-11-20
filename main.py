import random
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

# Download NLTK data (run this once if needed)
nltk.download('punkt')
nltk.download('wordnet')

# Define a smarter response system
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm just a program, but I'm here to help!", "Doing great! You?"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "help": ["Sure, what do you need help with?", "I'm here to assist!"]
}

fallback_responses = [
    "Hmm, I'm not sure I understand.",
    "Can you rephrase that?",
    "I'm still learning! Could you ask differently?"
]

# Synonym matcher for keywords
def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return synonyms

# Tokenize and find the best response
def find_response(user_input):
    tokens = word_tokenize(user_input.lower())
    for keyword, replies in responses.items():
        # Check if any keyword or its synonyms match the user input
        if any(word in tokens for word in [keyword, *get_synonyms(keyword)]):
            return random.choice(replies)
    return random.choice(fallback_responses)

# Chatbot function with context tracking
def chatbot():
    print("AI: Hi! I'm your advanced assistant. Ask me anything (type 'exit' to stop).")
    context = None  # Track the topic of the conversation

    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("AI: Bye! Have a great day!")
            break

        # Generate a response
        response = find_response(user_input)

        # Maintain conversation flow
        if "help" in user_input or "need" in user_input:
            context = "help"
        elif "bye" in user_input:
            context = None  # Clear context on goodbye

        if context == "help":
            response += " Is there a specific problem you're facing?"

        print(f"AI: {response}")

# Run the chatbot
chatbot()
