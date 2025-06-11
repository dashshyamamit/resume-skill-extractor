import fitz  # PyMuPDF
import re

def extract_resume_data(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()

    data = {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
    }
    return data

def extract_email(text):
    match = re.search(r'\S+@\S+', text)
    return match.group() if match else None

def extract_phone(text):
    match = re.search(r'(\+91)?[\s\-]?[6-9]\d{9}', text)
    return match.group() if match else None

def extract_name(text):
    return text.strip().split("\n")[0]

def extract_skills(text):
    skill_keywords = ["Python", "Java", "SQL", "C++", "React", "Node.js", "Machine Learning"]
    return [skill for skill in skill_keywords if skill.lower() in text.lower()]
