def chatbot():
    print("welcome to the chatbot and if u need to quit just type 'exit'")
    while True:
        user_input = input("You : ")
        if user_input.lower() == 'exit':
            print("Exiting the chatbot. Goodbye!")
            break
        elif user_input.strip() == "":
            print("Please enter a valid input.")
        elif user_input.lower() in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I assist you today?")
        elif user_input.lower() in ["how are you", "how's it going"]:
            print("Chatbot: I'm just a program, but thanks for asking! How can I help you?")
        elif user_input.lower() in ["what's your name", "who are you"]:
            print("Chatbot: I'm a simple chatbot created to assist you. You can call me Chatbot!")
        elif user_input.lower() in ["what can you do", "what are your capabilities"]:
            print("Chatbot: I can answer questions, provide information, and assist with various tasks. How can I help you today?")
        else:
            print("Chatbot: I'm not sure how to respond to that. Can you please rephrase or ask something else?")

if __name__ == "__main__":
    chatbot()