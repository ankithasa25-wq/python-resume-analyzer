# SmartResume: Intelligent Resume Analysis & Job Matching System

**SmartResume** is a Python-based desktop application designed to analyze resumes and provide structured insights into their skills, content, sections, ATS keywords, and suitability for different job roles.

The application combines resume parsing, rule-based skill detection, resume scoring, ATS keyword analysis, and job-specific skill matching in a user-friendly Tkinter interface.

## Key Features

* 📄 **DOCX and PDF Resume Support**
  Extracts text from both Word documents and PDF resumes.

* 🔍 **Skill Detection**
  Identifies technical skills such as Python, C, Java, SQL, MATLAB, Git, Machine Learning, and Data Structures.

* 📌 **Missing Skill Identification**
  Shows skills that are not detected in the resume.

* 📑 **Resume Section Analysis**
  Detects important sections such as Education, Skills, Projects, Certifications, Experience, and Career Objective.

* 📊 **Resume Scoring**
  Calculates a score out of 100 based on skills, resume sections, and content.

* 📈 **In-App Score Visualization**
  Displays Skills, Sections, Content, and Overall scores using a Tkinter-based graph.

* 🎯 **Job Role Matching**
  Compares the resume against predefined requirements for different job roles.

* 🔄 **Dynamic Job Matching**
  Automatically recalculates the job match when the selected target role is changed.

* 🤖 **ATS Keyword Analysis**
  Identifies frequently occurring keywords that can help evaluate resume content.

* 📝 **Report Generation**
  Generates a text-based resume analysis report.

* 🖥️ **Graphical User Interface**
  Provides an easy-to-use desktop interface using Tkinter.

## Supported Job Roles

SmartResume currently supports four target roles:

* Python Developer
* Data Analyst
* Machine Learning Engineer
* Software Developer

Each role contains a predefined set of required skills. The application compares these skills with the skills detected in the uploaded resume.

## Resume Scoring System

The application calculates the resume score using three categories:

| Category        | Maximum Score |
| --------------- | ------------: |
| Skills          |            60 |
| Resume Sections |            30 |
| Content         |            10 |
| **Overall**     |       **100** |

### Scoring Logic

**Skills Score**

Based on the number of detected skills from the predefined technical skill list.

**Section Score**

Based on the presence of important resume sections.

**Content Score**

Based on the amount of text extracted from the resume, with the content component capped at 10 points.

## Job Matching

The job matching system compares the resume with the required skills for the selected role.

For example:

```text
Required Skills:
Python
Git
Data Structures
SQL
```

If the resume contains:

```text
Python
Git
Data Structures
```

the application calculates the corresponding match percentage and identifies:

* Matching skills
* Missing job skills

The result automatically updates when a different job role is selected.

## ATS Keyword Analysis

The application extracts frequently occurring words from the resume and displays the top keywords.

This provides a basic way to understand which technical or professional terms appear most frequently in the resume.

## Technologies Used

* **Python**
* **Tkinter** – Desktop graphical user interface
* **python-docx** – DOCX text extraction
* **PyPDF2** – PDF text extraction
* **Regular Expressions (Regex)** – Skill, section, and keyword detection
* **Git & GitHub** – Version control and project management

## Project Architecture

```text
                 Resume
                   │
                   ▼
          Resume Text Extraction
             DOCX / PDF
                   │
                   ▼
          Resume Analysis Engine
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
     Skills     Sections    Content
        │          │          │
        └──────────┼──────────┘
                   ▼
             Score /100
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
 ATS Keyword Analysis    Job Role Matching
                              │
                              ▼
                     Match Percentage
                              │
                              ▼
                    Graphical Results
                              │
                              ▼
                       Analysis Report
```

## Project Structure

```text
python-resume-analyzer/
│
├── script.py
├── job_matcher.py
├── requirements.txt
├── .gitignore
│
├── resumes/
│   └── sample_resume.docx
│
└── reports/
```

> Generated reports and local backup files are excluded from the GitHub repository through `.gitignore`.

## Installation

Clone the repository:

```bash
git clone https://github.com/ankithasa25-wq/python-resume-analyzer.git
```

Navigate to the project:

```bash
cd python-resume-analyzer
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Run the main Python file:

```bash
python script.py
```

The SmartResume graphical interface will open.

### Usage

1. Click **Choose Resume**.
2. Select a DOCX or PDF resume.
3. Select the desired **Target Job Role**.
4. Click **Analyze Resume**.
5. Review the resume analysis and score.
6. Change the target job role to dynamically view another job match.
7. View the score graph inside the application.
8. Click **Save Report** to generate the analysis report.

## Example Analysis

The application can provide information such as:

```text
Total Words: 300+

Skills Found:
Python, C, Git, MATLAB, Data Structures

Missing Skills:
Java, SQL, HTML, CSS

Overall Score:
72/100

Target Role:
Python Developer

Job Match:
75%

Matching Job Skills:
Python, Git, Data Structures

Missing Job Skills:
SQL
```

## Future Enhancements

* Expand the number of supported job roles
* Add more advanced ATS analysis
* Add resume improvement recommendations
* Introduce machine-learning-based resume classification
* Add job description input for customized matching
* Support additional document formats

## Author

**Ankitha SA**

BE Electronics & Communication Engineering Student

GitHub: **ankithasa25-wq**

```

## Note

This project uses predefined skills and job-role requirements, so the analysis is based on basic text matching rather than advanced AI or NLP techniques.
