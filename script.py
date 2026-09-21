from docx import Document
import os

while True:

    print("\n==============================")
    print("       RESUME ANALYZER")
    print("==============================")

    print("\n1. Analyze Resume")
    print("2. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        resume_folder = "resumes"

        resume_files = []

        for file in os.listdir(resume_folder):
            if file.lower().endswith(".docx"):
                resume_files.append(file)

        if len(resume_files) == 0:
            print("\nNo Word resume files found.")
            continue

        print("\nAvailable Resumes:")

        for i in range(len(resume_files)):
            print(i + 1, ".", resume_files[i])

        file_choice = input("\nEnter resume number: ")

        if not file_choice.isdigit():
            print("\nInvalid choice.")
            continue

        file_number = int(file_choice)

        if file_number < 1 or file_number > len(resume_files):
            print("\nInvalid resume number.")
            continue

        file_name = resume_files[file_number - 1]

        file_path = os.path.join(resume_folder, file_name)

        document = Document(file_path)

        text = ""

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

        resume_text = text.lower()

        word_count = len(text.split())

        # Skills
        skill_variations = {
            "Python": ["python", "python programming"],
            "C": ["c programming", "c language"],
            "Java": ["java"],
            "SQL": ["sql", "mysql"],
            "HTML": ["html"],
            "CSS": ["css"],
            "JavaScript": ["javascript"],
            "MATLAB": ["matlab"],
            "Machine Learning": ["machine learning", "ml"],
            "Data Structures": ["data structures", "dsa"],
            "Git": ["git", "github"]
        }

        found_skills = []
        missing_skills = []

        for skill, variations in skill_variations.items():

            skill_found = False

            for variation in variations:
                if variation in resume_text:
                    skill_found = True
                    break

            if skill_found:
                found_skills.append(skill)
            else:
                missing_skills.append(skill)

        # Sections
        sections = [
            "Education",
            "Skills",
            "Projects",
            "Certifications",
            "Experience",
            "Career Objective"
        ]

        found_sections = []

        for section in sections:
            if section.lower() in resume_text:
                found_sections.append(section)

        # Resume score
        score = 0

        skill_score = int((len(found_skills) / len(skill_variations)) * 40)
        score += skill_score

        section_score = int((len(found_sections) / len(sections)) * 30)
        score += section_score

        if word_count >= 300:
            word_score = 20
        elif word_count >= 200:
            word_score = 15
        elif word_count >= 100:
            word_score = 10
        else:
            word_score = 5

        score += word_score

        if "Certifications" in found_sections:
            certification_score = 10
        else:
            certification_score = 0

        score += certification_score

        # Display analysis
        print("\n------------------------------")
        print("RESUME ANALYSIS")
        print("------------------------------")

        print("Resume:", file_name)
        print("Total words:", word_count)

        print("\nSkills Found:")

        for skill in found_skills:
            print("-", skill)

        print("Total skills found:", len(found_skills))

        print("\nMissing Skills:")

        for skill in missing_skills:
            print("-", skill)

        print("\nResume Sections Found:")

        for section in found_sections:
            print("-", section)

        print("Total sections found:", len(found_sections))

        print("\nResume Score:", score, "/ 100")

        # Suggestions
        print("\nSuggestions:")

        if "Certifications" not in found_sections:
            print("- Consider adding a Certifications section.")

        if len(found_skills) < 5:
            print("- Consider adding more relevant technical skills.")

        if word_count < 250:
            print("- Consider adding more relevant resume content.")

        if len(found_skills) >= 5 and len(found_sections) >= 5:
            print("- Your resume has good basic coverage.")

        # Job roles
        job_roles = {
            "Python Developer": [
                "Python",
                "Data Structures",
                "SQL",
                "Git"
            ],
            "Data Analyst": [
                "Python",
                "SQL",
                "Data Structures",
                "MATLAB"
            ],
            "Machine Learning": [
                "Python",
                "Machine Learning",
                "Data Structures",
                "MATLAB"
            ]
        }

        print("\nAvailable Job Roles:")
        print("1. Python Developer")
        print("2. Data Analyst")
        print("3. Machine Learning")

        role_choice = input("\nEnter job role number: ")

        if role_choice == "1":
            role = "Python Developer"
        elif role_choice == "2":
            role = "Data Analyst"
        elif role_choice == "3":
            role = "Machine Learning"
        else:
            role = ""

        if role:

            required_skills = job_roles[role]

            matched_skills = []
            missing_job_skills = []

            for required_skill in required_skills:

                variations = skill_variations[required_skill]

                skill_found = False

                for variation in variations:
                    if variation in resume_text:
                        skill_found = True
                        break

                if skill_found:
                    matched_skills.append(required_skill)
                else:
                    missing_job_skills.append(required_skill)

            match_percentage = int(
                (len(matched_skills) / len(required_skills)) * 100
            )

            print("\nJob Role:", role)

            print("Matched Skills:")

            for skill in matched_skills:
                print("-", skill)

            print("Missing Skills:")

            for skill in missing_job_skills:
                print("-", skill)

            print("Job Match:", match_percentage, "%")

            # Final summary
            print("\nFinal Analysis Summary")
            print("----------------------")
            print("Resume Score:", score, "/ 100")
            print("Selected Role:", role)
            print("Job Match:", match_percentage, "%")

            # Save report
            report_folder = "reports"

            if not os.path.exists(report_folder):
                os.makedirs(report_folder)

            report_path = os.path.join(
                report_folder,
                "resume_analysis_report.txt"
            )

            with open(report_path, "w") as report:

                report.write("RESUME ANALYZER REPORT\n")
                report.write("======================\n\n")

                report.write("Resume: " + file_name + "\n")
                report.write("Total Words: " + str(word_count) + "\n")
                report.write("Resume Score: " + str(score) + "/100\n\n")

                report.write("Skills Found:\n")

                for skill in found_skills:
                    report.write("- " + skill + "\n")

                report.write("\nMissing Skills:\n")

                for skill in missing_skills:
                    report.write("- " + skill + "\n")

                report.write("\nResume Sections Found:\n")

                for section in found_sections:
                    report.write("- " + section + "\n")

                report.write("\nSelected Job Role: " + role + "\n")
                report.write(
                    "Job Match: "
                    + str(match_percentage)
                    + "%\n"
                )

                report.write("\nMatched Job Skills:\n")

                for skill in matched_skills:
                    report.write("- " + skill + "\n")

                report.write("\nMissing Job Skills:\n")

                for skill in missing_job_skills:
                    report.write("- " + skill + "\n")

            print("\nReport saved successfully!")
            print("Location:", report_path)

        else:
            print("Invalid job role.")

    elif choice == "2":

        print("\nThank you for using Resume Analyzer!")
        break

    else:

        print("\nInvalid choice.")