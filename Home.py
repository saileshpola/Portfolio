import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col3, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Sailesh Naidu Pola")
    content = """I am a software developer with a bachelor’s in Mechanical Engineering and a postgraduate degree in 
    Robotics. I have 2 years of experience and strong skills in Python and SQL. I am passionate about solving 
    technical challenges and building efficient, data-driven solutions. """
    st.info(content)

text1 = """Below you can find some apps I have built in Python. Feel free to contact me!"""
st.write(text1)

df = pandas.read_csv("data.csv", sep=';')
col3, col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")