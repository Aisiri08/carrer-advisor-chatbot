#!/usr/bin/env python3
# career_advisor.py
# A lightweight console chatbot for career guidance.

import sys
import textwrap

WELCOME = "Hello! I’m your Career Advisor Chatbot. How can I help today?"

CAREER_MAP = {
    "coding": [
        "Software Developer",
        "Data Scientist",
        "Web Developer",
        "AI Engineer",
        "Cybersecurity Specialist",
    ],
    "art": [
        "Graphic Designer",
        "Animator",
        "Creative Director",
        "Illustrator",
        "Fashion Designer",
    ],
    "writing": [
        "Content Writer",
        "Technical Writer",
        "Editor",
        "Copywriter",
        "Journalist",
    ],
    "healthcare": [
        "Doctor",
        "Nurse",
        "Healthcare Analyst",
        "Physical Therapist",
        "Pharmacist",
    ],
    "management": [
        "Project Manager",
        "Business Analyst",
        "HR Manager",
        "Operations Manager",
        "Marketing Manager",
    ],
    "science": [
        "Biologist",
        "Chemist",
        "Physicist",
        "Environmental Scientist",
        "Astronomer",
    ],
    "education": [
        "Teacher",
        "Professor",
        "Educational Consultant",
        "School Counselor",
        "Curriculum Designer",
    ],
    "finance": [
        "Financial Analyst",
        "Accountant",
        "Investment Banker",
        "Auditor",
        "Risk Manager",
    ],
    "law": [
        "Lawyer",
        "Paralegal",
        "Legal Analyst",
        "Compliance Officer",
        "Contract Manager",
    ],
    "marketing": [
        "Digital Marketer",
        "SEO Specialist",
        "Brand Manager",
        "Content Strategist",
        "Social Media Manager",
    ],
    "dance": [
        "Choreographer",
        "Dance Instructor",
        "Performer",
        "Artistic Director",
        "Movement Coach",
    ],
    "singing": [
        "Vocalist",
        "Voice Coach",
        "Music Producer",
        "Sound Engineer",
        "Recording Artist",
    ],
}

SKILLS_NEEDED = {
    "coding": [
        "Programming (e.g., Python, Java, JS)",
        "Data structures and algorithms",
        "Version control (Git)",
        "Testing and debugging",
        "Problem-solving",
    ],
    "writing": [
        "Grammar and style",
        "Research and outlining",
        "Editing and proofreading",
        "SEO basics",
        "Portfolio building",
    ],
    "dance": [
        "Technique and choreography",
        "Stamina and flexibility",
        "Performance practice",
        "Teaching methods",
        "Networking in arts",
    ],
    "singing": [
        "Vocal technique and breath control",
        "Ear training and music theory",
        "Studio/Live performance",
        "Mic technique",
        "Repertoire development",
    ],
    "healthcare": [
        "Clinical knowledge",
        "Patient care",
        "Medical ethics",
        "Certifications/licensure",
        "Team communication",
    ],
}

RESUME_TIPS = {
    "default": [
        "Keep to one page (early career) or two (experienced).",
        "Use clear headings: Summary, Skills, Experience, Education.",
        "Bullet achievements with metrics (e.g., ‘Reduced cost by 15%’).",
        "Tailor keywords to the role description.",
    ],
    "coding": [
        "Showcase projects with links and repositories.",
        "List core stacks, tools, and impact metrics.",
    ],
    "writing": [
        "Link to a portfolio of articles or samples.",
        "Highlight audience growth and engagement metrics.",
    ],
    "healthcare": [
        "List licenses/certifications and clinical rotations.",
        "Emphasize patient outcomes and teamwork.",
    ],
}

INTERVIEW_TIPS = {
    "default": [
        "Research the company’s product, market, and culture.",
        "Prepare 2–3 accomplishment stories using STAR.",
        "Practice concise, structured answers and clarifying questions.",
    ],
    "coding": [
        "Practice DS&A on a whiteboard/REPL; review system design basics.",
        "Explain trade-offs and complexity; think aloud.",
    ],
    "writing": [
        "Bring clips; discuss editing cycles and voice adaptation.",
        "Describe your research and fact-check processes.",
    ],
    "healthcare": [
        "Prepare patient-care scenarios and ethical reasoning.",
        "Highlight interprofessional collaboration experiences.",
    ],
}

JOB_SEARCH = [
    "Target 10–20 companies and tailor resumes/cover letters.",
    "Use referrals and alumni networks; optimize LinkedIn.",
    "Track applications; follow up within 7–10 days.",
    "Attend meetups, conferences, and online communities.",
]

SALARY = {
    "coding": "Entry: 6–10 LPA; Mid: 10–25 LPA; Senior: 25+ LPA (varies by region/industry).",
    "writing": "Entry: 3–6 LPA; Mid: 6–12 LPA; Senior: 12+ LPA.",
    "dance": "Highly variable; combine teaching, gigs, and choreography.",
    "singing": "Variable; performance, teaching, and studio work mix.",
    "healthcare": "Role-dependent; check local scales and certifications.",
    "default": "Varies by role, region, experience; use local salary surveys.",
}

WORK_LIFE = {
    "coding": [
        "Set focus blocks and async communication norms.",
        "Avoid scope creep; estimate and negotiate.",
        "Take regular micro-breaks and protect off-hours.",
    ],
    "dance": [
        "Balance practice with rest and recovery.",
        "Cross-train to prevent injury; set rehearsal limits.",
    ],
    "singing": [
        "Schedule vocal rest; hydrate and warm up properly.",
        "Plan recording/performance days to avoid strain.",
    ],
    "default": [
        "Define working hours and boundaries.",
        "Plan weekly priorities; batch tasks.",
        "Schedule exercise, hobbies, and social time.",
    ],
}

MENU = """
Choose an option:
  1) Suggest careers from interests/skills
  2) Skills needed for a field
  3) Resume tips
  4) Interview preparation
  5) Job search advice
  6) Salary expectations
  7) Work-life balance tips
  8) Quit
"""

def wrap(text: str) -> str:
    return textwrap.fill(text, width=88)

def suggest_career(interests: str, skills: str) -> str:
    interests_l = interests.lower()
    skills_l = skills.lower()
    results = []
    for key, roles in CAREER_MAP.items():
        if key in interests_l or key in skills_l:
            results.extend(roles)
    if results:
        uniq = sorted(set(results))
        return "Based on inputs, consider: " + ", ".join(uniq)
    return (
        "No direct match found. Try specifying keywords like coding, writing, "
        "healthcare, management, science, education, finance, law, marketing, dance, singing."
    )

def skills_needed(field: str) -> str:
    key = field.lower().strip()
    tips = SKILLS_NEEDED.get(key)
    if not tips:
        return "No preset skills for this field. Try: coding, writing, dance, singing, healthcare."
    return f"Core skills for {field}: " + "; ".join(tips) + "."

def resume_tips(field: str) -> str:
    field_l = field.lower().strip()
    lines = RESUME_TIPS.get("default", []) + RESUME_TIPS.get(field_l, [])
    return "Resume tips:\n- " + "\n- ".join(lines)

def interview_tips(field: str) -> str:
    field_l = field.lower().strip()
    lines = INTERVIEW_TIPS.get("default", []) + INTERVIEW_TIPS.get(field_l, [])
    return "Interview prep:\n- " + "\n- ".join(lines)

def job_search_advice() -> str:
    return "Job search tips:\n- " + "\n- ".join(JOB_SEARCH)

def salary_expectations(field: str) -> str:
    key = field.lower().strip()
    return f"Salary guide for {field}: " + SALARY.get(key, SALARY["default"])

def work_life_balance(field: str) -> str:
    key = field.lower().strip()
    lines = WORK_LIFE.get(key, WORK_LIFE["default"])
    return "Work-life balance:\n- " + "\n- ".join(lines)

def main() -> int:
    print(wrap(WELCOME))
    while True:
        print(MENU)
        choice = input("Enter choice [1-8]: ").strip()
        if choice == "1":
            interests = input("Enter your interests (comma-separated): ")
            skills = input("Enter your skills (comma-separated): ")
            print(wrap(suggest_career(interests, skills)))
        elif choice == "2":
            field = input("Enter a field (e.g., coding, writing, dance, singing, healthcare): ")
            print(wrap(skills_needed(field)))
        elif choice == "3":
            field = input("Enter a field for resume tips (or leave blank): ") or "default"
            print(resume_tips(field))
        elif choice == "4":
            field = input("Enter a field for interview prep (or leave blank): ") or "default"
            print(interview_tips(field))
        elif choice == "5":
            print(job_search_advice())
        elif choice == "6":
            field = input("Enter a field for salary expectations (or leave blank): ") or "default"
            print(wrap(salary_expectations(field)))
        elif choice == "7":
            field = input("Enter a field for work-life balance (or leave blank): ") or "default"
            print(work_life_balance(field))
        elif choice == "8":
            print("Goodbye!")
            return 0
        else:
            print("Invalid choice. Please select 1–8.")
        print("-" * 88)
    # Unreachable
    # return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted. Goodbye!")
        sys.exit(130)
