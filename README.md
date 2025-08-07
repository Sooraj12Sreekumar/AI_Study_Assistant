# AI Study Assistant 

An interactive AI-powered study assistant built with Python. This tool allows users to upload PDFs, generate summaries, create quizzes, and clear doubts using state-of-the-art language models.


## Features

- Extract text from uploaded PDFs
- Generate concise summaries
- Create quizzes and practice questions
- Clear doubts using LLM-based answers
- Easy-to-run Python app with Streamlit UI

---

## Technologies Used

- *Python*
- *Streamlit* – for interactive frontend
- *Gemini API* – for AI/LLM processing
- *PyMuPDF* – to extract PDF text

---

## Project Structure

```
AI-Study-Assistant/
│
├── app.py               # Main Streamlit app
├── ai_engine.py         # Handles AI responses, summary, Q&A
├── file_processing.py   # Extracts text from PDF files
├── requirements.txt     # Python dependencies
└── .gitignore
```

## Setup Instructions

1. Clone the repository
```
git clone https://github.com/sooraj12sreekumar/AI_Study_Assistant.git
cd A__Study_Assistant
```


2. Create and activate virtual environment
```
python -m venv menv
source menv/bin/activate     # Linux/macOS
menv\Scripts\activate        # Windows
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Set up your .env file

Create a .env file in the root directory and add your API keys:
```
API_KEY=your_openai_or_gemini_key
```

5. Run the app
```
streamlit run app.py
```
