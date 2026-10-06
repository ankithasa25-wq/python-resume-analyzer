from docx import Document
from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import re
import os

from job_matcher import JOB_ROLES, calculate_match


# ---------- DATA ----------

SKILLS = [
    "Python", "C", "Java", "SQL", "HTML", "CSS",
    "JavaScript", "Machine Learning", "Data Structures",
    "Git", "MATLAB"
]

SECTIONS = [
    "Education", "Skills", "Projects",
    "Certifications", "Experience", "Career Objective"
]

resume_text = ""
analysis = None


# ---------- READ RESUME ----------

def read_resume(file):

    if file.endswith(".docx"):
        doc = Document(file)
        return "\n".join(p.text for p in doc.paragraphs)

    if file.endswith(".pdf"):
        pdf = PdfReader(file)
        return "\n".join(
            page.extract_text() or ""
            for page in pdf.pages
        )

    return ""


# ---------- ANALYZE RESUME ----------

def analyze(text):

    found = [
        skill for skill in SKILLS
        if re.search(
            r"\b" + re.escape(skill.lower()) + r"\b",
            text.lower()
        )
    ]

    missing = [
        skill for skill in SKILLS
        if skill not in found
    ]

    sections = [
        section for section in SECTIONS
        if section.lower() in text.lower()
    ]

    words = len(
        re.findall(r"\b\w+\b", text)
    )

    skills_score = round(
        len(found) / len(SKILLS) * 60
    )

    section_score = round(
        len(sections) / len(SECTIONS) * 30
    )

    content_score = round(
        min(words / 300, 1) * 10
    )

    total_score = (
        skills_score +
        section_score +
        content_score
    )

    return (
        words,
        found,
        missing,
        sections,
        skills_score,
        section_score,
        content_score,
        total_score
    )


# ---------- ATS KEYWORDS ----------

def get_keywords(text):

    words = re.findall(
        r"\b[a-zA-Z][a-zA-Z+#.]*\b",
        text.lower()
    )

    count = {}

    for word in words:

        if len(word) >= 4:
            count[word] = count.get(word, 0) + 1

    return sorted(
        count.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]


# ---------- CHOOSE RESUME ----------

def choose_resume():

    global resume_text, analysis

    file = filedialog.askopenfilename(
        title="Select Resume",
        filetypes=[
            ("Resume Files", "*.docx *.pdf"),
            ("Word Document", "*.docx"),
            ("PDF File", "*.pdf")
        ]
    )

    if not file:
        return

    resume_text = read_resume(file)
    analysis = None

    file_label.config(
        text=os.path.basename(file)
    )

    result.delete(
        "1.0",
        tk.END
    )

    graph.delete(
        "all"
    )

    result.insert(
        tk.END,
        "Resume selected successfully.\n\n"
        "Choose a job role and click "
        "'Analyze Resume'."
    )


# ---------- ANALYZE ----------

def analyze_resume():

    global analysis

    if not resume_text:

        messagebox.showwarning(
            "No Resume",
            "Please select a resume first."
        )

        return

    analysis = analyze(
        resume_text
    )

    (
        words,
        found,
        missing,
        sections,
        skills_score,
        section_score,
        content_score,
        total_score
    ) = analysis

    show_results()


# ---------- SHOW RESULTS ----------

def show_results():

    (
        words,
        found,
        missing,
        sections,
        skills_score,
        section_score,
        content_score,
        total_score
    ) = analysis

    role = role_box.get()

    match, matched, missing_job = calculate_match(
        resume_text,
        JOB_ROLES[role]
    )

    keywords = get_keywords(
        resume_text
    )

    result.delete(
        "1.0",
        tk.END
    )

    result.insert(
        tk.END,
        "RESUME ANALYSIS\n",
        "title"
    )

    result.insert(
        tk.END,
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    )

    result.insert(
        tk.END,
        f"Resume: {file_label.cget('text')}\n"
        f"Total Words: {words}\n\n"
    )

    result.insert(
        tk.END,
        "SKILLS FOUND\n",
        "heading"
    )

    result.insert(
        tk.END,
        ", ".join(found) + "\n\n"
    )

    result.insert(
        tk.END,
        "MISSING SKILLS\n",
        "heading"
    )

    result.insert(
        tk.END,
        ", ".join(missing) + "\n\n"
    )

    result.insert(
        tk.END,
        "RESUME SECTIONS\n",
        "heading"
    )

    result.insert(
        tk.END,
        ", ".join(sections) + "\n\n"
    )

    result.insert(
        tk.END,
        "SCORE BREAKDOWN\n",
        "heading"
    )

    result.insert(
        tk.END,
        f"Skills      : {skills_score}/60\n"
        f"Sections    : {section_score}/30\n"
        f"Content     : {content_score}/10\n"
        f"Overall     : {total_score}/100\n\n"
    )

    result.insert(
        tk.END,
        "JOB MATCH\n",
        "heading"
    )

    result.insert(
        tk.END,
        f"Role        : {role}\n"
        f"Match       : {match}%\n\n"
    )

    result.insert(
        tk.END,
        "MATCHING JOB SKILLS\n",
        "heading"
    )

    result.insert(
        tk.END,
        ", ".join(matched) + "\n\n"
    )

    result.insert(
        tk.END,
        "MISSING JOB SKILLS\n",
        "heading"
    )

    result.insert(
        tk.END,
        ", ".join(missing_job) + "\n\n"
    )

    result.insert(
        tk.END,
        "TOP ATS KEYWORDS\n",
        "heading"
    )

    for word, number in keywords:

        result.insert(
            tk.END,
            f"• {word}: {number}\n"
        )

    draw_graph()


# ---------- GRAPH ----------

def draw_graph():

    graph.delete(
        "all"
    )

    scores = [
        analysis[4],
        analysis[5],
        analysis[6],
        analysis[7]
    ]

    labels = [
        "Skills",
        "Sections",
        "Content",
        "Overall"
    ]

    graph_width = 600
    graph_height = 250

    bar_width = 80
    gap = 55

    for i, score in enumerate(scores):

        x1 = 35 + i * (
            bar_width + gap
        )

        x2 = x1 + bar_width

        y2 = 215

        y1 = y2 - (
            score / 100 * 170
        )

        graph.create_rectangle(
            x1,
            y1,
            x2,
            y2,
            fill="#4A90E2",
            outline=""
        )

        graph.create_text(
            (x1 + x2) / 2,
            y1 - 12,
            text=str(score),
            font=("Arial", 10, "bold")
        )

        graph.create_text(
            (x1 + x2) / 2,
            235,
            text=labels[i],
            font=("Arial", 10)
        )

    graph.create_text(
        graph_width / 2,
        15,
        text="Resume Score",
        font=("Arial", 14, "bold")
    )


# ---------- SAVE REPORT ----------

def save_report():

    if not analysis:

        messagebox.showwarning(
            "No Analysis",
            "Analyze the resume first."
        )

        return

    os.makedirs(
        "reports",
        exist_ok=True
    )

    role = role_box.get()

    match, matched, missing_job = calculate_match(
        resume_text,
        JOB_ROLES[role]
    )

    keywords = get_keywords(
        resume_text
    )

    (
        words,
        found,
        missing,
        sections,
        skills_score,
        section_score,
        content_score,
        total_score
    ) = analysis

    path = "reports/resume_analysis_report.txt"

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "RESUME ANALYZER REPORT\n"
            "======================\n\n"
        )

        file.write(
            f"Total Words: {words}\n"
            f"Skills Score: {skills_score}/60\n"
            f"Sections Score: {section_score}/30\n"
            f"Content Score: {content_score}/10\n"
            f"Overall Score: {total_score}/100\n\n"
        )

        file.write(
            "Skills Found:\n"
            + ", ".join(found)
            + "\n\n"
        )

        file.write(
            "Missing Skills:\n"
            + ", ".join(missing)
            + "\n\n"
        )

        file.write(
            "Resume Sections:\n"
            + ", ".join(sections)
            + "\n\n"
        )

        file.write(
            f"Selected Role: {role}\n"
            f"Job Match: {match}%\n\n"
        )

        file.write(
            "Matching Job Skills:\n"
            + ", ".join(matched)
            + "\n\n"
        )

        file.write(
            "Missing Job Skills:\n"
            + ", ".join(missing_job)
            + "\n\n"
        )

        file.write(
            "Top ATS Keywords:\n"
        )

        for word, number in keywords:

            file.write(
                f"- {word}: {number}\n"
            )

    messagebox.showinfo(
        "Report Saved",
        f"Report saved to:\n{path}"
    )


# ---------- MAIN WINDOW ----------

window = tk.Tk()

window.title(
    "Resume Analyzer"
)

window.geometry(
    "1000x750"
)

window.configure(
    bg="#F4F6F8"
)


# Header

header = tk.Frame(
    window,
    bg="#1F3A5F",
    height=90
)

header.pack(
    fill="x"
)

tk.Label(
    header,
    text="RESUME ANALYZER",
    bg="#1F3A5F",
    fg="white",
    font=("Arial", 24, "bold")
).pack(
    pady=(15, 2)
)

tk.Label(
    header,
    text="Analyze • Match • Improve",
    bg="#1F3A5F",
    fg="white",
    font=("Arial", 11)
).pack()


# File section

file_frame = tk.Frame(
    window,
    bg="white",
    bd=1,
    relief="solid"
)

file_frame.pack(
    fill="x",
    padx=25,
    pady=15
)

tk.Label(
    file_frame,
    text="Resume",
    bg="white",
    font=("Arial", 12, "bold")
).pack(
    side="left",
    padx=15,
    pady=15
)

file_label = tk.Label(
    file_frame,
    text="No resume selected",
    bg="white",
    fg="#666666",
    width=45,
    anchor="w"
)

file_label.pack(
    side="left"
)

tk.Button(
    file_frame,
    text="Choose Resume",
    command=choose_resume,
    bg="#4A90E2",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5
).pack(
    side="right",
    padx=15
)


# Job role section

role_frame = tk.Frame(
    window,
    bg="white",
    bd=1,
    relief="solid"
)

role_frame.pack(
    fill="x",
    padx=25,
    pady=5
)

tk.Label(
    role_frame,
    text="Target Job Role",
    bg="white",
    font=("Arial", 11, "bold")
).pack(
    side="left",
    padx=15,
    pady=12
)

role_box = ttk.Combobox(
    role_frame,
    values=list(JOB_ROLES.keys()),
    state="readonly",
    width=30
)

role_box.pack(
    side="left"
)

role_box.current(0)


def role_changed(event):
    if analysis:
        show_results()


role_box.bind(
    "<<ComboboxSelected>>",
    role_changed
)


tk.Button(
    role_frame,
    text="Analyze Resume",
    command=analyze_resume,
    bg="#2E7D32",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=12,
    pady=5
).pack(
    side="right",
    padx=15
)


# Main content

content = tk.Frame(
    window,
    bg="#F4F6F8"
)

content.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=15
)


# Results

result_frame = tk.Frame(
    content,
    bg="white",
    bd=1,
    relief="solid"
)

result_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 10)
)

tk.Label(
    result_frame,
    text="Analysis Results",
    bg="white",
    font=("Arial", 13, "bold")
).pack(
    pady=10
)

result = tk.Text(
    result_frame,
    bg="white",
    fg="#222222",
    font=("Consolas", 10),
    bd=0,
    wrap="word"
)

result.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=5
)

result.tag_config(
    "title",
    font=("Arial", 16, "bold")
)

result.tag_config(
    "heading",
    font=("Arial", 11, "bold")
)


# Graph

graph_frame = tk.Frame(
    content,
    bg="white",
    bd=1,
    relief="solid",
    width=320
)

graph_frame.pack(
    side="right",
    fill="y"
)

tk.Label(
    graph_frame,
    text="Score Graph",
    bg="white",
    font=("Arial", 13, "bold")
).pack(
    pady=10
)

graph = tk.Canvas(
    graph_frame,
    width=500,
    height=270,
    bg="white",
    highlightthickness=0
)

graph.pack(
    padx=10
)


# Bottom buttons

bottom = tk.Frame(
    window,
    bg="#F4F6F8"
)

bottom.pack(
    pady=10
)

tk.Button(
    bottom,
    text="Save Report",
    command=save_report,
    bg="#6A1B9A",
    fg="white",
    font=("Arial", 10, "bold"),
    width=18,
    pady=7
).pack(
    side="left",
    padx=8
)

tk.Button(
    bottom,
    text="Clear",
    command=lambda: result.delete(
        "1.0",
        tk.END
    ),
    bg="#757575",
    fg="white",
    font=("Arial", 10, "bold"),
    width=18,
    pady=7
).pack(
    side="left",
    padx=8
)


window.mainloop()