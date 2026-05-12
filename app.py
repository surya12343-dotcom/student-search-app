import streamlit as st
import pandas as pd

FILE_NAME = "26-27 Student Id.xlsx"

st.set_page_config(page_title="Admission Number Search", layout="centered")

st.title("SRI SHENBAGA VINAYAGAR MAT HR SEC SCHOOL")
st.subheader("Student Admission Number Search")

excel_data = pd.read_excel(FILE_NAME, sheet_name=None)

all_students = pd.DataFrame()

for sheet_name, df in excel_data.items():
    df.columns = [str(col).strip() for col in df.columns]

    name_col = None
    id_col = None

    for col in df.columns:
        if "name" in col.lower():
            name_col = col
        if "id" in col.lower() or "admission" in col.lower():
            id_col = col

    if name_col and id_col:
        temp = df[[name_col, id_col]].copy()
        temp.columns = ["Student Name", "Admission No"]
        temp["Class"] = sheet_name
        all_students = pd.concat([all_students, temp], ignore_index=True)

all_students = all_students.dropna(subset=["Student Name"])

student_name = st.text_input("Enter Student Name")

if st.button("Search"):
    if student_name.strip() == "":
        st.warning("Please enter student name")
    else:
        result = all_students[
            all_students["Student Name"]
            .astype(str)
            .str.contains(student_name, case=False, na=False)
        ]

        if result.empty:
            st.error("No student found. Please check spelling.")
        else:
            st.success("Student Found")
            st.dataframe(result, hide_index=True)


