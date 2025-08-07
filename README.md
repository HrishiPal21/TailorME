# 🧠 TailorMe — Personal AI Resume Tailoring App

**TailorMe** is your own personal AI-powered resume assistant. Built entirely from scratch using Python and Streamlit, this app helps you tailor your resume to match any job description by highlighting the overlap and gaps between your resume and the job posting.

Whether you're applying for internships, jobs, or freelance roles, TailorMe keeps your resume sharp, targeted, and personalized — without wasting hours editing manually.

---

## 🔧 Features

- 📄 Upload your resume and job description (in `.txt` format)
- 🤖 Extracts key skills and terminology from the JD
- 🔍 Compares with your resume to highlight matches and gaps
- ✨ Ready for AI tailoring using OpenAI's GPT models (optional & secure)
- 💻 Clean, interactive Streamlit UI
- 🛡️ Local-first — no data sent unless GPT is enabled

---


## 🛠 Tech Stack

- **Python 3.12**
- **Streamlit**
- **OpenAI API (for optional GPT tailoring)**
- `dotenv`, `python-docx` (optional), `git`

---

## 🏁 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/HrishiPal21/TailorME.git
cd TailorME

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run tailor_app.py


🧪 Future Features (when I feel like it)
 .docx and .pdf support

 AI bullet rewrites with GPT-3.5/4

 Resume "match score" to guilt-trip myself

 Downloadable tailored resume

 LinkedIn job scraper maybe?



