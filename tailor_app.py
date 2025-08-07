import streamlit as st
import os

st.set_page_config(page_title="TailorMe - AI Resume Tailor", layout="centered")

st.title("🤖 TailorMe - AI Resume Tailoring App (Lite Version)")

# Upload Resume
resume_file = st.file_uploader("Upload your resume (.txt)", type="txt")

# Upload JD
jd_file = st.file_uploader("Upload the job description (.txt)", type="txt")

# Placeholder for extracted content
resume_text = ""
jd_text = ""

# Read files
if resume_file is not None:
    resume_text = resume_file.read().decode("utf-8")

if jd_file is not None:
    jd_text = jd_file.read().decode("utf-8")

if resume_text and jd_text:
    st.subheader("🔍 Extracted Keywords & Matching Skills")

    # Extract keywords from JD (very basic for now)
    jd_words = set(jd_text.lower().split())
    resume_words = set(resume_text.lower().split())

    matching = sorted(list(jd_words.intersection(resume_words)))
    missing = sorted(list(jd_words - resume_words))

    st.markdown("✅ **Skills/Keywords Present in Your Resume:**")
    st.write(", ".join(matching[:50]))

    st.markdown("⚠️ **Missing or Less-Visible Keywords (from JD):**")
    st.write(", ".join(missing[:50]))

    # Placeholder for GPT tailoring
    st.divider()
    st.markdown("✍️ **AI Resume Tailoring (Coming Soon)**")
    st.button("Run AI Tailoring ✨ (requires OpenAI key)")

else:
    st.info("👆 Please upload both your resume and job description to begin.")

