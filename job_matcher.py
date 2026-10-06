import re


JOB_ROLES = {
    "Python Developer": [
        "Python",
        "Git",
        "Data Structures",
        "SQL"
    ],

    "Data Analyst": [
        "Python",
        "SQL",
        "MATLAB",
        "Data Structures"
    ],

    "Machine Learning Engineer": [
        "Python",
        "Machine Learning",
        "Data Structures",
        "SQL",
        "Git"
    ],

    "Software Developer": [
        "Python",
        "C",
        "Java",
        "Data Structures",
        "Git"
    ]
}


def skill_found(text, skill):

    pattern = r"\b" + re.escape(skill.lower()) + r"\b"

    return re.search(
        pattern,
        text.lower()
    ) is not None


def calculate_match(resume_text, required_skills):

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill_found(resume_text, skill):
            matched_skills.append(skill)

        else:
            missing_skills.append(skill)

    if required_skills:

        match_percentage = round(
            (len(matched_skills) / len(required_skills)) * 100
        )

    else:

        match_percentage = 0

    return (
        match_percentage,
        matched_skills,
        missing_skills
    )