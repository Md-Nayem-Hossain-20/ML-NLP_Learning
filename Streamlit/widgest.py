import streamlit as st 
import pandas as pd

st.title(" Streamlit Text Input: ")

name = st.text_input("Enter your Name: ")

age = st.slider("Select your Age: ", 0,100,25)
st.write(f"Your age is : {age}.")

if name:
    st.write(f"Hello, {name}")


options = ["Python","Java","C++","Go"]
choice = st.selectbox("Choose your favourite languages: ", options)
st.write(f"You have Selected {choice}")


data = {
    "Name": ["Nayem","Nobita","Hossain","Luffy"],
    "Age": [24,24,25,21],
    "City": ["Dhaka","Tokyo","Dhaka","Grandline"]
}

df = pd.DataFrame(data)
df.to_csv("data.csv")
st.write(df)

uploaded_file =st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)



