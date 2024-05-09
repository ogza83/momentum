import os
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st
import openai

# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Initialize the OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)
flask_url = "http://127.0.0.1:5000"

with st.sidebar:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(BASE_DIR, 'static', 'image', 'logo.png')
    st.sidebar.image(logo_path, use_column_width=True)
    st.sidebar.title("Example Prompts")
    "Write me 3 facebook posts for [Product Description]"
    "Guide me to build Marketing Strategy"
    "Write me a marketing copy for [description]"
    " "
    " "
    " "# Change this to your Flask app URL
    st.markdown(f'<a href="{flask_url}" target="_self"><button class="btn btn-primary">Return to Momentum Home</button></a>', unsafe_allow_html=True)
# Define the URL to redirect to (Flask app URL)

# Streamlit button using HTML and JavaScript for redirection


st.title("💬 Your Marketing Assistant")  
st.caption("🚀 A Momentum chatbot powered by OpenAI to help with your marketing. Examples: 'Generate ad copy for my product', 'Brainstorm blog post ideas', 'Help me analyze campaign results'") 

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Let's boost your marketing! Need help with campaigns, content, or strategy?"}]

def generate_response(prompt, examples, instructions):
    messages = [
        {"role": "system", "content": instructions},
        {"role": "user", "content": "Here are some examples of marketing tasks and how I want you to respond:"},
        *examples,
        {"role": "user", "content": prompt}
    ]

    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        msg = response.choices[0].message.content
        return msg
    except openai.error.InvalidRequestError as e:  # Handle potential errors
        return f"Error: {e}. Please refine your examples or try a different prompt."

# Example usage
examples = [
    {"role": "user", "content": "Write a catchy email subject line for my new product launch."},
    {"role": "assistant", "content": "Sure, here are a few options: 1. Unveiling [Product Name]: Get Ready for Something Exciting!  2.  Limited-Time Offer: Experience the Revolution with [Product Name] ... "},
    {"role": "user", "content": "Write a few short and engaging social media posts to promote my webinar."},
    {"role": "assistant", "content": "Sure! Here are a few options: 1.  🤔 Strugglingggling with [problem the webinar addresses]? Join our FREE webinar to learn [key benefit].  Register now! [Link]  2.  Level up your [relevant skill]!  Our expert-led webinar will teach you how to [key benefits].  Spots are limited - sign up today! [Link]"},
    {"role": "user", "content": "What are good email open rates and click-through rates?"},
     {"role": "assistant", "content": "Average open rates are 17-28% (but less reliable nowadays). Aim for 2-3% click-through rate. Industry, subject line, and content quality greatly impact these metrics."}, 
]

instructions = """
Respond as a helpful and knowledgeable marketing assistant. Focus on providing creative ideas and actionable tips.  Be enthusiastic and encouraging!
""" 

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not OPENAI_API_KEY:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt) 
    msg = generate_response(prompt, examples, instructions)
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)  