print("Welcome to Customer Support Chatbot")
print("Type 'bye' to exit\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How can I help you?")

    elif "product" in user:
        print("Bot: We provide laptops, mobiles, and accessories.")

    elif "price" in user:
        print("Bot: Prices start from Rs. 10,000.")

    elif "order" in user:
        print("Bot: Your order will be delivered within 3-5 days.")

    elif "contact" in user:
        print("Bot: You can contact us at support@example.com")

    elif "thank" in user:
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Thank you for visiting. Goodbye!")
        break

    else:
        print("Bot: Sorry, I did not understand your question.")