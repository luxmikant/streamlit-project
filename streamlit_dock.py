import pandas as pd
import numpy as np
import streamlit as st
import time


st.title('Startup Dashboard')

st.header('I am  Learing streamlit')
st.subheader('And i  am Loving it')
st.write('this is  a normal text')

st.markdown("""
### My favorite movies
- race 3
- humskalas
- dhoom 3
""")

st.code("""
def foo(input):
    return foo**2
    print(foo)
""")

st.latex('x^2 + y^2 + 2 = 0')
st.latex('\int \oint \sum \prod')
df = pd.DataFrame({
    'name':['nitish','ankit','shree'],
    'marks':[65,86,89],
    'package':[23,53,67]
})

st.dataframe(df)

st.metric('Revenue','Rs 3L','-3%')
st.json({
    'name':['nitish','ankit','shree'],
    'marks':[65,86,89],
    'package':[23,53,67]
})

#displaying media
st.image('image.jpeg')

st.sidebar.title('sidebar title')
col1, col2 = st.columns(2)
with col1:
    st.image('image.jpeg')
with col2:
    st.image('image.jpeg')
st.error('LOGIN Failed')

st.success('LONGIN Success')
st.info('hi')
st.warning('dsfjhg')

bar = st.progress(0)

for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)

email = st.text_input('Enter email')
number = st.number_input('Enter number')
st.date_input('Enter reg date')

email = st.text_input('Enter Email')
password = st.text_input('Enter password')
gender = st.selectbox('Select Gender', ['male', 'female', 'other'])

btn = st.button('Login kro')

if btn:
    if email == 'nitish@gmail.com' and password == '1234':
        # st.balloons()


        st.snow()
        st.write(gender)
    else:
        st.error('login failed')
import streamlit as st
import pandas as pd

#file uploader
file = st.file_uploader('Upload a csv file')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())



