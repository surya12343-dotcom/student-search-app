import streamlit as st
import pandas as pd

st.set_page_config(page_title="Admission Number Search")

st.title("SRI SHENBAGA VINAYAGAR MAT HR SEC SCHOOL")
st.subheader("Student Admission Number Search")

df = pd.read_csv("students.csv")

df.columns = [str(col).strip() for col in df.columns]

name_col = None
id_col = None

for col in df.columns:
    if "name" in col.lower():
        name_col = col
    if "id" in col.lower() or "admission" in col.lower():
        id_col = col

student_name = st.text_input("Enter Student Name")

if st.button("Search"):

    result = df[
        df[name_col]
        .astype(str)
        .str.contains(student_name, case=False, na=False)
    ]

    if result.empty:
        st.error("No student found")
    else:
        st.dataframe(result[[name_col, id_col]], hide_index=True)

