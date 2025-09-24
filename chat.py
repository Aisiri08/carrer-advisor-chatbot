#!/usr/bin/env python3
import sys
import textwrap

WRAP = 88
wrap = lambda s: textwrap.fill(s, width=WRAP)

WELCOME = "Hello! I’m your Career Advisor Chatbot. Let’s find next steps that fit interests and strengths."
PROMPT = "> "

CAREER_MAP = {
    "coding": ["Software Developer", "Data Scientist", "Web Developer", "AI Engineer", "Cybersecurity Specialist"],
    "art": ["Graphic Designer", "Animator", "Creative Director", "Illustrator", "Fashion Designer"],
    "writing": ["Content Writer", "Technical Writer", "Editor", "Copywriter", "Journalist"],
    "healthcare": ["Doctor", "Nurse", "Healthcare Analyst", "Physical Therapist", "Pharmacist"],
    "management": ["Project Manager", "Business Analyst", "HR Manager", "Operations Manager", "Marketing Manager"],
    "science": ["Biologist", "Chemist", "Physicist", "Environmental Scientist", "Astronomer"],
    "education": ["Teacher", "Professor", "Educational Consultant", "School Counselor", "Curriculum Designer"],
    "finance": ["Financial Analyst", "Accountant", "Investment Banker", "Auditor", "Risk Manager"],
    "law": ["Lawyer", "Paralegal", "Legal Analyst", "Compliance Officer", "Contract Manager"],
    "marketing": ["Digital Marketer", "SEO Specialist", "Brand Manager", "Content Strategist", "Social Media Manager"],
    "dance": ["Choreographer", "Dance Instructor", "Performer", "Artistic Director", "Movement Coach"],
    "singing": ["Vocalist", "Voice Coach", "Music Producer", "Sound Engineer", "Recording Artist"],
}

SKILLS_NEEDED = {
    "coding": [
        "Programming (e.g., Python, Java, JS)",
        "Data structures and algorithms",
        "Version control (Git)",
        "Testing and debugging",
        "Problem‑solving"
    ],
    "writing": [
        "Grammar and style",
        "Research and outlining",
        "Editing and proofreading",
        "SEO basics",
        "Portfolio building"
    ],
    "dance": [
        "Technique and choreography",
        "Stamina and flexibility",
        "Performance practice",
        "Teaching methods",
        "Networking in arts"
    ],
    "singing": [
        "Vocal technique and breath control",
        "Ear training and music theory",
        "Studio/Live performance",
        "Mic technique",
        "Repertoire development"
    ],
    "healthcare": [
        "Clinical knowledge",
        "Patient care",
        "Medical ethics",
        "Certifications/licensure",
        "Team communication"
    ],
}

RESUME_TIPS = {
    "default": [
        "Keep to one page (early career) or two (experienced).",
        "Use clear headings: Summary, Skills, Experience, Education.",
        "Bullet achievements with metrics (e.g., Increased retention by 12%).",
        "Tailor keywords to the role description."
    ],
    "coding": [
        "Showcase projects with links and repositories.",
        "List core stacks, tools, and impact metrics."
    ],
    "writing": [
        "Link to a portfolio of articles or samples.",
        "Highlight audience growth and engagement metrics."
    ],
    "healthcare": [
        "List licenses/certifications and clinical rotations.",
        "Emphasize patient outcomes and teamwork."
    ],
}

INTERVIEW_TIPS = {
    "default": [
        "Research the company’s product, market, and culture.",
        "Prepare 2–3 accomplishment stories using STAR.",
        "Practice concise, structured answers and clarifying questions."
    ],
    "coding": [
        "Practice DSA in a REPL/whiteboard; review system design basics.",
        "Explain trade‑offs and complexity; think aloud."
    ],
    "writing": [
        "Bring clips; discuss editing cycles and voice adaptation.",
        "Describe research and fact‑check processes."
    ],
    "healthcare": [
        "Prepare patient‑care scenarios and ethical reasoning.",
        "Highlight interprofessional collaboration."
    ],
}

JOB_SEARCH = [
    "Target 10–20 companies and tailor resumes/cover letters.",
    "Use referrals and alumni networks; optimize LinkedIn.",
    "Track applications; follow up within 7–10 days.",
    "Attend meetups, conferences, and online communities."
]

SALARY = {
    "coding": "Entry 6–10 LPA, Mid 10–25 LPA, Senior 25+ LPA; varies by region/industry.",
    "writing": "Entry 3–6 LPA, Mid 6–12 LPA, Senior 12+ LPA.",
    "dance": "Highly variable; combine teaching, gigs, choreography.",
    "singing": "Variable mix of performance, teaching, studio work.",
    "healthcare": "Role‑dependent; check local scales/certifications.",
    "default": "Varies by role, region, experience; consult local salary surveys."
}

WORK_LIFE = {
    "default": [
        "Define working hours and boundaries.",
        "Plan weekly priorities; batch tasks.",
        "Schedule exercise, hobbies, and social time."
    ],
    "coding": [
        "Set focus blocks and async norms.",
        "Avoid scope creep; estimate and negotiate.",
        "Take micro‑breaks; protect off‑hours."
    ],
    "dance": [
        "Balance practice with rest and recovery.",
        "Cross‑train to prevent injury; set rehearsal limits."
    ],
    "singing": [
        "Schedule vocal rest; hydrate and warm up.",
        "Plan recording/performance days to avoid strain."
    ],
}

def safe_input(prompt):
    try:
        return input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
        sys.exit(0)

def menu():
    print()
    print(wrap("Choose an option:"))
    print("  1) Suggest careers from interests/skills")
    print("  2) Skills needed for a field")
    print("  3) Resume tips")
    print("  4) Interview preparation")
    print("  5) Job search advice")
    print("  6) Salary expectations")
    print("  7) Work‑life balance tips")
    print("  8) Quit")

def suggest_careers(interests, skills):
    interestsl = (interests or "").lower()
    skillsl = (skills or "").lower()
    results = []
    for key, roles in CAREER_MAP.items():
        if key in interestsl or key in skillsl:
            results.extend(roles)
    uniq = sorted(set(results))
    if uniq:
        return "Based on inputs, consider: " + ", ".join(uniq)
    return ("No direct match found. Try specifying keywords like: "
            "coding, writing, healthcare, management, science, education, finance, law, marketing, dance, singing.")

def skills_needed(field):
    key = (field or "").lower().strip()
    tips = SKILLS_NEEDED.get(key)
    if not tips:
        return "No preset skills for this field. Try: coding, writing, dance, singing, healthcare."
    return "Core skills for " + key + ":\n- " + "\n- ".join(tips)

def resume_tips(field):
    fieldl = (field or "default").lower().strip()
    lines = RESUME_TIPS.get("default", []) + RESUME_TIPS.get(fieldl, [])
    return "Resume tips:\n- " + "\n- ".join(lines)

def interview_tips(field):
    fieldl = (field or "default").lower().strip()
    lines = INTERVIEW_TIPS.get("default", []) + INTERVIEW_TIPS.get(fieldl, [])
    return "Interview prep:\n- " + "\n- ".join(lines)

def job_search_advice():
    return "Job search tips:\n- " + "\n- ".join(JOB_SEARCH)

def salary_expectations(field):
    key = (field or "default").lower().strip()
    return f"Salary guide for {key}: {SALARY.get(key, SALARY['default'])}"

def work_life_balance(field):
    key = (field or "default").lower().strip()
    lines = WORK_LIFE.get(key, WORK_LIFE["default"])
    return "Work‑life balance:\n- " + "\n- ".join(lines)

def main():
    print(wrap(WELCOME))
    while True:
        menu()
        choice = safe_input(PROMPT)
        if not choice:
            print(wrap("Tip: Enter 1–8, or type 'quit' to exit."))
            continue
        low = choice.lower()
        if low in ("8", "quit", "exit", "q"):
            print("Goodbye!")
            return
        if low in ("help", "h"):
            print(wrap("Type a number (1–8). Use 'quit' anytime."))
            continue

        if low == "1":
            interests = safe_input("Enter your interests (comma‑separated): ")
            skills = safe_input("Enter your skills (comma‑separated): ")
            print(wrap(suggest_careers(interests, skills)))
        elif low == "2":
            field = safe_input("Enter a field (e.g., coding, writing, dance, singing, healthcare): ")
            print(wrap(skills_needed(field)))
        elif low == "3":
            field = safe_input("Enter a field for resume tips (or leave blank): ")
            print(wrap(resume_tips(field)))
        elif low == "4":
            field = safe_input("Enter a field for interview prep (or leave blank): ")
            print(wrap(interview_tips(field)))
        elif low == "5":
            print(wrap(job_search_advice()))
        elif low == "6":
            field = safe_input("Enter a field for salary expectations (or leave blank): ")
            print(wrap(salary_expectations(field)))
        elif low == "7":
            field = safe_input("Enter a field for work‑life balance (or leave blank): ")
            print(wrap(work_life_balance(field)))
        else:
            print(wrap("Invalid choice. Please select 1–8."))

if __name__ == "__main__":
    try:
        sys.exit(main() or 0)
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)
