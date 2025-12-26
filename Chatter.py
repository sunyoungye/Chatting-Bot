# Name: Sunyoung Chung
# uID: u1577102
# File: Chatter.py
# PURPOSE: Run the chatbot interaction loop with GoodBot or EvilBot

from ChatBot import GoodBot, EvilBot

def main():
    """
    Main loop for conversation.
    - Ask the user to choose a bot
    - Print the bot's greeting
    - Keep asking for user input until 'stop' is entered
    - Each input is sent to the bot and the response is printed

    """
    choice = input("Choose a bot (good/evil): ").strip().lower()
    if choice == "good":
        bot = GoodBot
    else:
        bot = EvilBot

    bot.greet()
    while True:
        user_text = input(">>> ")
        if user_text.lower() == "stop":
            break
        print("Computer: ", bot.respond(user_text))


if __name__ == "__main__":
    main()