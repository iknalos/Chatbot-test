# Simple terminal chatbot using Python dictionary - no external libraries required.
# Author: Your Name
# Date: 2025-11-23

responses = {
    "good morning": "good morning.",
    "how are you": "I am doing very well, thank you for asking.",
    "you're welcome": "Do you like hats?",
    "yes": "Great, hats are wonderful!",
    "no": "That's okay, hats aren't for everyone."
}

def get_bot_response(user_input):
    lower_input = user_input.lower().strip()
    for key in responses:
        if key in lower_input:
            return responses[key]
    return "Tell me more..."

print("Welcome to TerminalBot! Type 'exit' to end.")
while True:
    user_input = input("user: ")
    if user_input.lower().strip() == "exit":
        print("bot: Goodbye!")
        break
    print(f"bot: {get_bot_response(user_input)}")
