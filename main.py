import streamlit as st
import os
from dotenv import load_dotenv
import json
import PyPDF2 as pdf
from langchain_community.llms import Ollama

ollama_model=Ollama(model='ats_llama3')

def get_ollama_response(input,resume):
    response=ollama_model.invoke("Job Description-"+input+"resume-"+resume)
    return response

def input_multiple_pdfs(uploaded_files):
    text = ""
    for uploaded_file in uploaded_files:
        reader = pdf.PdfReader(uploaded_file)
        for page in range(len(reader.pages)):
            page = reader.pages[page]
            text += str(page.extract_text())
    return text

st.title("ATS for HR Analysis Using Custom Ollama Model")
st.write("""I'm an AI that streamlines hiring by analyzing job descriptions and resumes. I pinpoint the best candidates by matching their skills to job requirements, saving HR time and effort while improving the quality of hires.

Here's how I can assist:
         
1. **Job Description Analysis**: Extract key skills and requirements.
2. **Resume Analysis**: Identify relevant skills and experience in resumes.
3. **Matching Score Calculation**: Compare resume skills with job requirements.
4. **Candidate Ranking**: Rank candidates based on their matching scores.""")
st.subheader("Job Description")
jobdes=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload the Resume", type="pdf",help="please upload PDF", accept_multiple_files=True)

submit=st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_multiple_pdfs(uploaded_file)
        response=get_ollama_response(jobdes,text)
        st.subheader(response)