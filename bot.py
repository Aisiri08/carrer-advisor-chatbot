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
        "singing": "Vocal techniques, breath control, music theory, performance skills.",
        "dance": "Hip-hop, Bharatanatyam, Zumba, choreography skills, performance techniques.",
        "coding": "Python, Java, C++, problem-solving, debugging, software development methodologies.",
        "writing": "Creativity, grammar proficiency, storytelling, typing skills."
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

def resume_tips(career):
    tips = {
        "coding": "Highlight your programming skills, mention projects, use action verbs like 'developed' and 'implemented'.",
        "writing": "Showcase your writing portfolio, emphasize your editing and proofreading skills, mention relevant writing tools.",
        "dance": "Emphasize your performance experience, highlight choreography and teaching skills, mention notable productions or performances.",
        "singing": "Showcase your vocal range and performance experience, mention training and notable performances, highlight any songwriting or production skills.",
        "healthcare": "Highlight your clinical experience, certifications, and patient care skills. Mention any specialized training or areas of expertise."
    }
    return tips.get(career.lower(), "I'm sorry, I don't have specific resume tips for that career.")

def interview_prep(career):
    questions = {
        "coding": "Prepare for questions about algorithms, data structures, past projects, and technical challenges.",
        "writing": "Be ready to discuss your writing process, your editing skills, and examples of your work.",
        "dance": "Be prepared to discuss your training, performance experience, and approach to choreography. You may also be asked to demonstrate techniques or routines.",
        "singing": "Expect questions about your vocal training, performance experience, and songwriting or production skills. Be ready to perform a song or demonstrate techniques.",
        "healthcare": "Prepare for questions about your clinical experience, patient care philosophy, and how you handle stressful situations. Be ready to discuss specific cases or scenarios."
    }
    return questions.get(career.lower(), "I'm sorry, I don't have specific interview tips for that career.")

def job_search_tips():
    return "Use job search engines, attend industry events, network with professionals on LinkedIn, and tailor your resume to each job application."

def salary_expectations(career):
    salaries = {
        "coding": "Software Developers earn between $70,000 and $120,000 annually depending on experience and location.",
        "writing": "Content Writers typically earn between $40,000 and $70,000 annually.",
        "dance": "Professional Dancers can earn between $30,000 and $80,000 annually, depending on the type of work and location.",
        "singing": "Singers' earnings vary widely based on performance frequency and contracts, but many earn between $40,000 and $100,000 annually.",
        "healthcare": "Healthcare professionals' salaries vary by role, with Doctors earning between $150,000 and $300,000 annually, Nurses between $60,000 and $100,000, and other roles falling in between."
    }
    return salaries.get(career.lower(), "I'm sorry, I don't have salary data for that career.")

def work_life_balance(career):
    tips = {
        "coding": "Set boundaries for work hours, take regular breaks, and make time for hobbies and physical activities.",
        "writing": "Create a dedicated workspace, manage your time effectively, and prioritize self-care.",
        "dance": "Ensure you have time for rest and recovery, maintain a healthy diet and exercise routine, and set aside time for personal interests.",
        "singing": "Maintain vocal health by staying hydrated and taking care of your voice. Balance performance and practice with personal time and relaxation.",
        "healthcare": "Set clear work-life boundaries, prioritize self-care, and schedule regular downtime to prevent burnout. Engage in hobbies and physical activities outside of work."
    }
    return tips.get(career.lower(), "I'm sorry, I don't have work-life balance tips for that career.")
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
            print(f"To pursue a career as a {career}, you typically need skills in areas such as communication, problem-solving, and technical proficiency related to the field.")

        elif "industry trends" in user_input.lower():
            industry = input("Which industry are you interested in? ")
            print(f"To stay updated in the {industry} industry, consider following recent advancements, attending relevant conferences, and networking with professionals in the field.")

        elif "related careers" in user_input.lower():
            current_career = input("What is your current career? ")
            print(f"If you're looking for careers related to {current_career}, consider roles that utilize similar skills or industries that value your experience.")
       
        elif "resume tips" in user_input.lower():
            career = input("Which career are you interested in? ")
            print(f"To improve your resume for a career in {career}, consider these tips: {resume_tips(career)}")

        elif "interview prep" in user_input.lower():
            career = input("Which career are you preparing for? ")
            print(f"For a career in {career}, you should prepare for these common interview questions and topics: {interview_prep(career)}")

        elif "job search tips" in user_input.lower():
            print(job_search_tips())

        elif "salary expectations" in user_input.lower():
            career = input("Which career are you interested in? ")
            print(f"The average salary for a career in {career} is: {salary_expectations(career)}")

        elif "work-life balance" in user_input.lower():
            career = input("Which career are you interested in? ")
            print(f"To maintain a good work-life balance in a {career} career, consider these tips: {work_life_balance(career)}")

        else:
            print("I'm sorry, I didn't understand that. Could you ask in a different way?")

if __name__ == "__main__":
    main()
