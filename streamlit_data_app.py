# # Iteration 1
# import streamlit as st
# st.title('Data Chat')
# st.sidebar.markdown('### Select Dataset')
# st.sidebar.selectbox("Available Datasets",['charging vio','vio based stations','Demand based stations','Merket based stations'],index=0)
# user_input = st.text_input('User:', value='', max_chars=500)
# submit_button = st.button('Send')


# import os
# import tempfile
# import subprocess
# import sys
# import pandas as pd
# from pandasai import PandasAI
# from pandasai.llm.openai import OpenAI
# from pandasai.llm.open_assistant import OpenAssistant
# import streamlit as st

# # Set the cache directory
# cache_dir = os.path.join(tempfile.gettempdir(), "pandasai_cache")
# os.makedirs(cache_dir, exist_ok=True)

# # Upgrade pip and install packages
# def install_packages():
#     with open('requirements.txt') as f:
#         packages = f.read().splitlines()
#     for package in packages:
#         subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# install_packages()

# # Defining model
# OPENAI_API_KEY = "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"
# llm = OpenAI(api_token=OPENAI_API_KEY)
# pandas_ai = PandasAI(llm)

# # load data
# df_long = pd.read_csv('dummy_data_long.csv')

# st.title('Data Chat')
# st.sidebar.markdown('### Select Dataset')
# st.sidebar.selectbox("Available Datasets", ['charging vio', 'vio based stations', 'Demand based stations', 'Merket based stations'], index=0)

# user_prompt = st.text_input("Enter your prompt")

# if st.button("Submit"):
#     response = pandas_ai.run(df_long, prompt=user_prompt, is_conversational_answer=False)
#     st.write("Response:", response)



#iteration3

import streamlit as st
import pandas as pd

# Create the dataframe
data = {
    'brand_name': ['benz', 'bmw', 'audi', 'jaguar', 'toyota'],
    'sales_volume': [100, 30, 80, 50, 500]
}
df = pd.DataFrame(data)

# Streamlit UI
st.title('Data Chat')
st.sidebar.markdown('### History')
user_input = st.text_input('User:', value='', max_chars=500)
submit_button = st.button('Send')

# Cache for storing results
@st.cache
def compute_result(input_text):
    if input_text == 'whats the most selling brand':
        most_selling_brand = df.loc[df['sales_volume'].idxmax(), 'brand_name']
        return f"The most selling brand is {most_selling_brand}"
    elif input_text == 'what the sales by brand':
        return df
    else:
        return "No data found"

# Retrieve history from cache or initialize empty list
history = st.session_state.get('history', [])

# Add user input to history only if it's not empty
if user_input and user_input not in history:
    history.append(user_input)
    history = history[-5:]

# Store updated history in session state
st.session_state.history = history

# Display clickable history
for item in history[::-1]:
    if st.sidebar.button(item):
        user_input = item

result = compute_result(user_input)
st.write(result)



