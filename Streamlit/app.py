import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("Hello World!")

# Display a simple Text
st.write("This is a simple text")

# Create a dataframe

df = pd.DataFrame({
    'first column': [1,3,5,7],
    'second column': [10,20,30,40]
})

## Display the Dataframe

st.write("Here is the dataframe")
st.write(df)


# Create a line Chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns = ['a','b','c']
)

st.line_chart(chart_data) 