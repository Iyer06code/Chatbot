from ai import get_ai_response
print("Welcome to AI chatbot")
print("Chatbot started! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    
    response = get_ai_response(user_input)
    print(f"AI: {response}")