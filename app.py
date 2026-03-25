import streamlit as st
from rag import create_qa_chain

st.title("🚀 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

query = st.text_input("Ask a question about your resume")

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    # Save file temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    qa = create_qa_chain("temp.pdf")

    if st.button("Analyze"):
        if query:
            result = qa(query)
            st.subheader("📊 Analysis Result")
            st.write(result)
        else:
            st.warning("Please enter a question")
else:
    st.info("Please upload a resume to begin")