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
        "coding": ["Software Developer", "Data Scientist", "Web Developer", "AI Engineer", "Cybersecurity Specialist"],
        "art": ["Graphic Designer", "Animator", "Creative Director", "Illustrator", "Fashion Designer"],
        "writing": ["Content Writer", "Technical Writer", "Editor", "Copywriter", "Journalist"],
        "healthcare": ["Doctor", "Nurse", "Healthcare Analyst", "Physical Therapist", "Pharmacist"],
        "management": ["Project Manager", "Business Analyst", "HR Manager", "Operations Manager", "Marketing Manager"],
        "science": ["Biologist", "Chemist", "Physicist", "Environmental Scientist", "Astronomer"],
        "education": ["Teacher", "Professor", "Educational Consultant", "School Counselor", "Curriculum Developer"],
        "dance": ["Professional Dancer", "Choreographer", "Dance Instructor", "Dance Therapist"],
        "singing": ["Singer", "Vocal Coach", "Music Producer", "Songwriter"]
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

def skills_needed(career):
    skill_requirements = {
        "singing": "Vocal techniques, breath control, song writer, , and music theory.",
        "dance": "Hiphop, bharathanatyam, zumba dance , choreography skills, and performance techniques.",
        "coding": "Python,java,c++, problem-solving, debugging, and software development methodologies.",
        "writing": "Creativity, grammar proficiency, storytelling, and handwritten,typing ."
        # Add more careers and skills as needed
    }
    return skill_requirements.get(career.lower(), "I'm sorry, I don't have specific skills listed for that career.")

def related_careers(current_career):
    related_career_map = {
        "dance": ["Choreographer", "Dance Instructor", "Physical Therapist", "Fitness Trainer"],
        "singing": ["Music Producer", "Songwriter", "Voice Actor", "Vocal Coach"],
        "writing": ["Editor", "Copywriter", "Journalist", "Technical Writer"],
        "coding": ["Software Developer", "Data Scientist", "Game Developer", "AI Researcher"]
        # Add more current careers and their related options
    }
    return related_career_map.get(current_career.lower(), "I'm sorry, I couldn't find related careers for that field.")

def career_transition():
    return "Thinking about a career change? Identify transferable skills from your current job and explore new fields that match your interests and strengths. Consider upskilling or taking courses to bridge knowledge gaps."

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

        elif "career advice" in user_input.lower():
            print("You can provide your interests and skills, and I can suggest some career options for you. You can also ask about required skills or industry trends for specific careers.")

        elif "skills needed" in user_input.lower():
            career = input("Which career are you interested in? ")
            print(f"To pursue a career in {career}, you typically need: {skills_needed(career)}")

        elif "industry trends" in user_input.lower():
            industry = input("Which industry are you interested in? ")
            print(f"To stay updated in the {industry} industry, consider following recent advancements, attending relevant conferences, and networking with professionals in the field.")

        elif "related careers" in user_input.lower():
            current_career = input("What is your current career? ")
            print(f"Careers related to {current_career} include: {', '.join(related_careers(current_career))}")

        elif "career transition" in user_input.lower():
            print(career_transition())

        else:
            print("I'm sorry, I didn't understand that. Could you ask in a different way? For example, you can ask about skills, related careers, or trends.")

if __name__ == "__main__":
    main()
