from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI 
import streamlit as st

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

# question = "Who is PM of India ?"
# res = llm.invoke(question)
# print(res.content)

# while True:
#     query = input("User: ")
#     if query.lower() in ["quit", "exit", "bye"]:
#         print("GoodBye")
#         break

#     res = llm.invoke(query)
#     print("AI: ", res.content[0]["text"], "\n")

st.title("AskBuddy - AI QnA Bot")
st.markdown("My Personal QnA Bot with LangChain and Google Gemini")

if "messages" not in st.session_state:
    st.session_state.messages= []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask Anything ?")
if query:
    st.session_state.messages.append({"role":"user", "content":query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.chat_message("ai").markdown(res.content[0]["text"]) # type: ignore
    st.session_state.messages.append({"role":"ai", "content":res.content[0]["text"]}) # type: ignore