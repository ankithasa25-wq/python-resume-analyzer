# Python Resume Analyzer

A simple Python-based application that analyzes resumes and provides useful insights such as detected skills, resume sections, resume score, and job-role matching.

## Features

* Extracts text from Word (`.docx`) resumes
* Detects technical skills
* Identifies important resume sections
* Calculates a resume score out of 100
* Identifies missing skills
* Matches resumes with selected job roles
* Generates an analysis report
* Allows multiple resumes to be analyzed

## Job Roles

The analyzer currently supports matching for:

* Python Developer
* Data Analyst
* Machine Learning

## Technologies Used

* Python
* python-docx
* File Handling
* Basic text processing

## How It Works

1. Select a resume from the `resumes` folder.
2. The program extracts the resume text.
3. It checks for skills and important sections.
4. It calculates a resume score.
5. It compares the detected skills with the selected job role.
6. It displays the results and generates an analysis report.

## Project Structure

```text
python-resume-analyzer/
│
├── resumes/
│   └── sample_resume.docx
│
├── script.py
├── requirements.txt
└── .gitignore
```

## Installation

Install the required library:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python script.py
```

## Note

This project uses predefined skills and job-role requirements, so the analysis is based on basic text matching rather than advanced AI or NLP techniques.
