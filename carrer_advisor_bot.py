#!/usr/bin/env python3
# career_advisor_bot.py

import os
import sys

os.environ.setdefault("MPLBACKEND", "Agg")

try:
    from chatterbot import ChatBot
    from chatterbot.trainers import ChatterBotCorpusTrainer
except Exception as e:
    print("ChatterBot import failed. Install:")
    print("  pip install 'chatterbot==1.0.5' 'chatterbot-corpus==1.2.0' 'SQLAlchemy<2.0' 'mathparse==0.1.2'")
    print("Use Python 3.8/3.9 for best compatibility.")
    sys.exit(1)

def build_bot():
    return ChatBot(
        "CareerAdvisorBot",
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        database_uri="sqlite:///career_advisor.sqlite3",
        logic_adapters=[
            {
                "import_path": "chatterbot.logic.BestMatch",
                "default_response": (
                    "I didn’t understand. Ask about careers, skills, resume, interviews, "
                    "salaries, job search, or work-life balance."
                ),
                "maximum_similarity_threshold": 0.90,
            },
            {
                "import_path": "chatterbot.logic.SpecificResponseAdapter",
                "input_text": "help",
                "output_text": (
                    "Try: career advice, required skills, resume tips, interview prep, "
                    "salary expectations, job search tips, work-life balance."
                ),
            },
        ],
        read_only=False,
    )

def train_if_needed(bot):
    if not os.path.exists("career_advisor.sqlite3"):
        print("Training model (first run). This may take a minute…")
        trainer = ChatterBotCorpusTrainer(bot)
        trainer.train("chatterbot.corpus.english")
        trainer.train(
            "chatterbot.corpus.english.greetings",
            "chatterbot.corpus.english.conversations",
        )
        print("Training complete.\n")

def main():
    print("Welcome to Career Advisor Bot! Type 'help' or 'quit' to exit.")
    bot = build_bot()
    train_if_needed(bot)
    while True:
        try:
            text = input("You: ").strip()
            if not text:
                continue
            if text.lower() in {"quit", "exit"}:
                print("Career Advisor Bot: Goodbye!")
                break
            response = bot.get_response(text)
            print(f"Career Advisor Bot: {response}")
        except (KeyboardInterrupt, EOFError):
            print("\nCareer Advisor Bot: Goodbye!")
            break

if __name__ == "__main__":
    main()
