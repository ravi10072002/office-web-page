import pandas
import streamlit as st

st.set_page_config(layout="wide")

st.header("The Best Company")
st.write("""
we build our computers the way we build our cities-over time,
over time,without a plan,on top of ruins
softwares are becoming the new cargo ships and freight trucks""")
st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])
with col2:
    for index, row in df[4:8].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])
