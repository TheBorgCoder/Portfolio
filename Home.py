import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Victor Christiansen")
    content = """
    Hello! I am a full time college student based out of Salt Lake City. I am currently pursuing my Bachelor's Degree in software engineering, with an emphasis on honing my Java skills. I have had a lifelong fascination with software and hardware and I am eager to dive deeper into the endless possibilities of the digital world!
    """
    st.info(content)

content2 = """
"Below you can find some of the apps I have built in Python. Feel free to contact me!"
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")