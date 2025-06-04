#!/usr/bin/env python3
"""A simple command-line chatbot."""

def respond(message: str) -> str:
    """Generate a response based on the user's message."""
    text = message.lower()
    if any(greeting in text for greeting in ("hello", "hi", "hey")):
        return "Hello! How can I help you today?"
    if any(bye in text for bye in ("bye", "goodbye", "exit")):
        return "Goodbye!"
    return f"You said: {message}"


def main() -> None:
    print("ChatBot initialized. Type 'bye' to exit.")
    while True:
        try:
            user_input = input("You: ")
        except EOFError:
            break
        response = respond(user_input)
        print(f"Bot: {response}")
        if response == "Goodbye!":
            break


if __name__ == "__main__":
    main()
