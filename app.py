import streamlit as st
from retriever import search
from llm_runner import ask_llm

st.title("PC Helper Bot 🤖🖥️")
question = st.text_input("Ask your PC troubleshooting question:")

if question:
    results = search(question)
    context = "\n\n".join(results['documents'][0])
    answer = ask_llm(context, question)

    st.write("### Answer")
    st.write(answer)

    with st.expander("See retrieved manual sections"):
        for doc in results['documents'][0]:
            st.write(doc)