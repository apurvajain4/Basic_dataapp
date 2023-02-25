import streamlit as st 
import numpy as np
import plotly.figure_factory as ff
#title
st.title(":blue[Apurva's] Data Application :pizza:")
add_selectbox = st.sidebar.selectbox(
    'What would you like to do?',
    ('Work','Search')
)
# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose Timeline",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
#Some text
st.text('A data application analyzes large-scale data to quickly surface rich insight or take autonomous action.')
#slider
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
# display chart
# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2
# Group data together
hist_data = [x1, x2, x3]
group_labels = ['ABC', 'PQR', 'LMS']
# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])
# Plot!
st.plotly_chart(fig, use_container_width=True)
btn_click=st.button("Next")