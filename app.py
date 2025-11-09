# Simple console chatbot that demonstrates Azure Text Analytics integration.
from config import DefaultConfig
from echo_bot import EchoBot
import sys

def main():
    print("Azure Chatbot Demo\nType 'exit' or 'quit' to end.\n")
    cfg = DefaultConfig()
    print(f"Configuration: {cfg.as_dict()}")
    bot = EchoBot(cfg)

    try:
        while True:
            user = input("You: ").strip()
            if user.lower() in ('exit', 'quit'):
                print("Bot: Goodbye!")
                break
            if not user:
                print("Bot: I didn't catch that — please type something.")
                continue
            reply = bot.get_reply(user)
            print(f"Bot: {reply}")
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting...")
        sys.exit(0)

if __name__ == '__main__':
    main()
