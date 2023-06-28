# Iteration 1
#import streamlit as st
#st.title('Data Chat')
#st.sidebar.markdown('### Select Dataset')
#st.sidebar.selectbox("Available Datasets",['charging vio','vio based stations','Demand based stations','Merket based stations'],index=0)
#user_input = st.text_input('User:', value='', max_chars=500)
#submit_button = st.button('Send')


import os
import tempfile
import subprocess
import sys
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
from pandasai.llm.open_assistant import OpenAssistant
import streamlit as st

# Set the cache directory
cache_dir = os.path.join(tempfile.gettempdir(), "pandasai_cache")
os.makedirs(cache_dir, exist_ok=True)

# Upgrade pip and install packages
def install_packages():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

install_packages()

# Defining model
OPENAI_API_KEY = "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"
llm = OpenAI(api_token=OPENAI_API_KEY)
pandas_ai = PandasAI(llm)

# load data
df_long = pd.read_csv('dummy_data_long.csv')

st.title('Data Chat')
st.sidebar.markdown('### Select Dataset')
st.sidebar.selectbox("Available Datasets", ['charging vio', 'vio based stations', 'Demand based stations', 'Merket based stations'], index=0)

user_prompt = st.text_input("Enter your prompt")

if st.button("Submit"):
    response = pandas_ai.run(df_long, prompt=user_prompt, is_conversational_answer=False)
    st.write("Response:", response)
