# HR-Resume-Analyser

Project Description:
ATS for HR Analysis Using Custom Ollama Model is an AI-driven Applicant Tracking System (ATS) that streamlines the hiring process by analyzing job descriptions and resumes. It efficiently identifies the best candidates by comparing their skills and experience with job requirements, enhancing hiring accuracy and reducing HR workload.

1. Job Description Analysis – Extracts key skills and requirements from job descriptions.
2. Resume Analysis – Identifies relevant skills and experience in candidate resumes.
3. Matching Score Calculation – Compares resumes with job descriptions to generate a compatibility score.
4. Candidate Ranking – Ranks candidates based on their matching scores to help HR make informed decisions.

## Pre Requisits/ Setup steps
Install Ollama3 from https://ollama.com
List of models available in ollama- https://ollama.com/library

Running ollama in terminal
- ollama pull <Model_Name> #Downloads the model
- ollama run <Model_Name> # Runs the model
- ollama list #list of installed models
- /exit to exit a model

Creating a model file
- nano <model_file_name>
- Inside the file give parameters and commands Guide- https://github.com/ollama/ollama/blob/main/docs/modelfile.md
Sample model file- ats_ollama3

After writing the model file create your custom model using command
- ollama create <custom_model_name> -f ./<model_file_name>
- ollama run <custom_model_name> to use the model in terminal.
- check list ($ ollama list) to see your model there which can be used in your notebook/code

VS code environment setup using conda
- conda create -p <your_env_name> python==3.10 -y
- create 2 files .env and requirements.txt
- .env file is to store your api key which is not a part of this project as we are using local model.
- requirements.txt to list all the required libraries.

Installing requirements
- conda activate <your_env_name> #activate your env
- pip install -r requirements.txt # installl all required libraries
- conda deactivate #deactivate env after use

Running streamlit app
- streamlit run app.py 
