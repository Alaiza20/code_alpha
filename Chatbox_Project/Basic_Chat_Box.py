"""
Basic_Chat_Box.py

A simple Python-based chatbox that responds to basic greetings, questions, and requests for jokes.
Run the script and interact with the chatbox by selecting options and typing your questions.
"""

import random
def chat_data():
    replies= {
         "hi": [
        "Hello!", "Hi there!", "Hey! Glad you texted.", "Hi! How's your day?"
    ],
    "how's it going": [
        "I'm fine.", "Doing well!", "Better than before.", "Perfectly fine!"
    ],
    "whats your name": [
        "I'm a simple Python chatbot.", "They call me ChatBox.", "I'm just a training bot."
    ],
    "bye": [
        "Goodbye!", "See you later!", "Nice talking with you!", "Take care!"
    ],
    "thanks": [
        "You're welcome!", "No problem!", "Anytime!", "Glad I could help!"
    ],
    "tell me a joke": [
        "Why did the computer go to the doctor? Because it caught a virus!",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the Python file break up with the C file? Too many type issues!"
    ]
    } 
    return replies

def main():

    print("Welcome to mini chat box.")
    chat = chat_data()
    while(True):
        

        choice = int(input("1.Ask Question\n2.Exit\n"))
        if choice == 1:
            user_input = input("Ask question: ").lower()
            if user_input in chat: 
                 print("Chat box:", random.choice(chat[user_input]))
            else:
                print("Chat box: I don't understand complex questions!")

        elif choice == 2:  
            print("Nice talk with you!")
            exit()
        else :
            print("Entered choice is not supported!")
             


main()





