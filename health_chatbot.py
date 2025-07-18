import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import os

# Set OpenAI Key from user input (use secret box for safety)
openai_key = st.text_input("Enter your OpenAI API Key", type="password")
if openai_key:
    os.environ["OPENAI_API_KEY"] = openai_key

    # Initialize chatbot
    chat = ChatOpenAI(temperature=0.4, model_name="gpt-3.5-turbo")

    st.set_page_config(page_title="AI Health Companion")
    st.title("🤖 AI Health Companion")
    st.markdown("Ask about health symptoms, first-aid, or wellness tips.")

    user_input = st.text_input("You:", "")

    system_message = SystemMessage(
        content=(
            "You are a helpful AI health assistant designed for rural users. "
            "Give simple advice about symptoms, first-aid, and wellness. "
            "Avoid prescriptions. Respond in easy language."
        )
    )

    if user_input:
        messages = [system_message, HumanMessage(content=user_input)]
        response = chat(messages)
        st.markdown("**AI Health Bot:**")
        st.success(response.content)
