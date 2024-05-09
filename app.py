import logging
import time
import threading
from flask import Flask, render_template, redirect
import os

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-chat')
def start_chat():
    # This route redirects to the Streamlit application
    return redirect("http://localhost:8501") 

if __name__ == '__main__':
    app.run(debug=True)
