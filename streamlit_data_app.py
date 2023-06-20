import streamlit as st
st.title('Skynet Chat')
st.sidebar.markdown('### Select Dataset')
st.sidebar.selectbox("Available Datasets",['charging vio','vio based stations','Demand based stations','Merket based stations'],index=0)
user_input = st.text_input('User:', value='', max_chars=500)
submit_button = st.button('Send')
