import streamlit as st
import requests

st.title("Multi-Agent Research Assistant")

question = st.text_input("Ask a question")

if st.button("Submit"):

    response = requests.post(
        "http://127.0.0.1:8000/api/ask/",
        json={"question": question}
    )
    # st.write(response.text)
    print(response.status_code)
    print(response.text)


    data = response.json()

    st.subheader("Planner Decision")
    st.write(data.get("plan"))

    # st.subheader("Research Result")
    # st.write(data.get("research"))

    st.subheader("Final Answer")
    st.write(data.get("answer"))