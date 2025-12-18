
def chatbot():
    print("Chatbot: Hello! Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine")
            print("Chatbot: How are you")

        elif user_input == "good":
            print("Chatbot: Great to Hear!")
        
        elif user_input == "what are your hobbies":
            print("Chatbot: sharing the information that you are in the need of! ")

        elif user_input == "that sounds great":
            print("Chatbot: thank you ")

        elif user_input == "ok bye":
            print("Chatbot: Goodbye! Have a nice day 😊")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")

chatbot()

input("\nPress Enter to exit...")
