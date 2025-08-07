import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Sample resume bullet
resume_bullet = "Managed SQL database and optimized data pipelines."

# Sample job description
job_description = """
We are looking for a Data Analyst who can manage ETL pipelines and optimize SQL queries for performance...
"""

# Prompt
prompt = f"""
You are a resume writing assistant. Tailor this resume bullet for the job:

Resume Bullet: {resume_bullet}

Job Description: {job_description}

Return a tailored bullet point that matches the job description.
"""

# Make the GPT-4 call
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.5,
)

# Print the result
print("\nTailored Resume Bullet:\n")
print(response.choices[0].message.content)
