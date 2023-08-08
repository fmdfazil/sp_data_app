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



import streamlit as st
import pandas as pd

# Create the dataframe
data = {
    'brand_name': ['benz', 'bmw', 'audi', 'jaguar', 'toyota'],
    'sales_volume': [100, 30, 80, 50, 500]
}
df = pd.DataFrame(data)


##Iteration 3
# Streamlit UI
st.title('Data Chat')
st.sidebar.markdown('### Select Dataset')
selected_dataset = st.sidebar.selectbox("Available Datasets", ['charging vio', 'vio based stations', 'Demand based stations', 'brand sales'], index=0)
user_input = st.text_input('User:', value='', max_chars=500)
submit_button = st.button('Send')

# Handle user input
if submit_button:
    if selected_dataset == 'charging vio':
        st.write("No data found")
    elif selected_dataset == 'vio based stations':
        st.write("No data found")
    elif selected_dataset == 'Demand based stations':
        st.write("No data found")
    elif selected_dataset == 'brand sales':
        if user_input == 'whats the most selling brand':
            most_selling_brand = df.loc[df['sales_volume'].idxmax(), 'brand_name']
            st.write(f"The most selling brand is {most_selling_brand}")
        elif user_input == 'what the sales by brand':
            st.write(df)
        else:
            st.write("No data found")

# Display chat history in the sidebar
st.sidebar.markdown('### Chat History')
for sender, message in chat_history:
    st.sidebar.text(f'{sender}: {message}')

