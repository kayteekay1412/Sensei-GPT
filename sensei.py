# -*- coding: utf-8 -*-
"""
@author: ktk
"""

from openai import OpenAI
import streamlit as st

user = OpenAI(api_key="[ENTER API KEY HERE]")
userrole = "user"

pre_prompt = "Teach me the following concept:"
response = ""

st.title("Sensei GPT")
st.divider()

model_options = ["gpt-3.5-turbo", "gpt-4"]
selected_model = st.selectbox("Select GPT Model", model_options, index=0)

prompt = st.text_input("What do you want to learn today?")
gptbutton = st.button("Teach me")
st.caption("Sensei will teach you once you press the button.")
st.divider()

if gptbutton:
    if not prompt.strip():
        st.warning("Please enter a topic to learn.")
    else:
        with st.spinner("I am preparing notes for your lecture"):
            try:
                response = user.chat.completions.create(
                    model=selected_model,  # Use the selected model
                    messages=[{"role": userrole, "content": pre_prompt + prompt}])
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
