import random

def greet():
    greetings = [
        "Hello! I'm your Career Advisor Chatbot.",
        "Hi there! Need help with career advice?",
        "Greetings! Let's discuss your career options."
    ]
    return random.choice(greetings)

def offer_help():
    return "How can I assist you today? For example, you can ask about career paths, required skills, or industry trends."

def suggest_career(interests, skills):
    """
    Provides a suggestion based on interests and skills.
    """
    career_map = {
        "coding": ["Software Developer", "Data Scientist", "Web Developer"],
        "art": ["Graphic Designer", "Animator", "Creative Director"],
        "writing": ["Content Writer", "Technical Writer", "Editor"],
        "healthcare": ["Doctor", "Nurse", "Healthcare Analyst"],
        "management": ["Project Manager", "Business Analyst", "HR Manager"]
    }

    # Find matches based on the user's inputs
    careers = []
    for key, career_options in career_map.items():
        if key in interests.lower() or key in skills.lower():
            careers.extend(career_options)

    if careers:
        return f"Based on your interests and skills, you could explore these careers: {', '.join(careers)}."
    else:
        return "I couldn't find a specific match for your interests and skills, but you can explore new areas or provide more details."

def main():
    print(greet())
    print(offer_help())

    while True:
        user_input = input("You: ")

        if "exit" in user_input.lower() or "quit" in user_input.lower():
            print("Thank you for chatting with me. Good luck with your career!")
            break

        elif "suggest career" in user_input.lower():
            interests = input("What are your interests? ")
            skills = input("What are your skills? ")
            print(suggest_career(interests, skills))

        else:
            print("I'm sorry, I didn't understand that. Could you ask in a different way?")

if __name__ == "__main__":
    main()
