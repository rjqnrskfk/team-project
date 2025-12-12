import streamlit as st
from scheduler import generate_schedule  # 폴더 구조에 맞게 수정

st.title("자동 시간표 생성기")

subjects = ["수학", "영어", "국어", "과학"]
timeslots = ["월1", "월2", "화1", "화2"]

if st.button("시간표 생성"):
    result = generate_schedule(subjects, timeslots)
    st.write("📘 생성된 시간표:")
    st.write(result)
