import streamlit as st
from file_processing import extract_text_from_pdf
from ai_engine import generate_summary, generate_quiz, answer_doubt

st.set_page_config(page_title="GenAI Tutor", layout="wide")
st.title("AI Study Assistant")

if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""
if "summary" not in st.session_state:
    st.session_state.summary = ""
if "quiz" not in st.session_state:
    st.session_state.quiz = []
if "show_quiz" not in st.session_state:
    st.session_state.show_quiz = False

uploaded_file = st.file_uploader("Upload your notes (PDF only)", type=["pdf"])

if uploaded_file:
    st.success("File uploaded successfully.")
    st.session_state.pdf_text = extract_text_from_pdf(uploaded_file)

    if st.button("Summarize Notes"):
        with st.spinner("Summarizing..."):
            st.session_state.summary = generate_summary(st.session_state.pdf_text)
        st.subheader("Summary")
        st.write(st.session_state.summary)

    if st.button("Generate Quiz"):
        with st.spinner("Generating quiz..."):
            quiz_text = generate_quiz(st.session_state.pdf_text)
            quiz_blocks = quiz_text.strip().split("Q")[1:]
            parsed_quiz = []
            for q in quiz_blocks:
                lines = q.strip().split("\n")
                question = "Q" + lines[0]
                options = lines[1:5]
                answer_line = next((line for line in lines if line.startswith("Answer")), "")
                correct = answer_line[-2:-1] if answer_line else ""
                parsed_quiz.append({"question": question, "options": options, "answer": correct})
            st.session_state.quiz = parsed_quiz
            st.session_state.show_quiz = True

if st.session_state.show_quiz:
    st.subheader("Quiz")
    for idx, q in enumerate(st.session_state.quiz):
        st.markdown(f"{q['question']}")
        
        user_ans = st.radio(
            f"Choose your answer:",
            q["options"],
            key=f"user_answer_{idx}",
            index=None
        )

        if st.button(f"Submit Q{idx+1}", key=f"submit_{idx}"):
            selected = user_ans.strip()[1].lower() if user_ans else None 
            correct = q["answer"].strip().lower()

            if selected == correct:
                st.success(f"Correct! The answer is ({correct.upper()}).")
            else:
                st.error(f"Incorrect. You selected ({selected.upper()}) — Correct answer is ({correct.upper()}).")

st.subheader("Ask a Doubt")
question = st.text_input("Type your question here...")

if st.button("Get Answer"):
    if question and st.session_state.pdf_text:
        with st.spinner("Thinking..."):
            answer = answer_doubt(st.session_state.pdf_text, question)
        st.success("Answer:")
        st.write(answer)
    else:
        st.warning("Please upload notes and type a question.")