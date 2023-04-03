import streamlit as st
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='startup analysis')

df = pd.read_csv('startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'],errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

def load_overall_analysis():
    st.title('Overall analysis')

    #total invested money
    total = round(df['amount'].sum())
    #maximum amount infused in startup
    max_funding = df.groupby('Startup')['amount'].max().sort_values(ascending=False).head().values[0]
    #avg ticket size
    avg_funding = df.groupby('Startup')['amount'].sum().mean()
    #total funded startup
    num_startup = df['Startup'].nunique()
    col1,col2,col3,col4=st.columns(4)

    with col1:
        st.metric('Total',str(total) + 'cr')
    with col2:
        st.metric('Max', str(max_funding) + 'cr')
    with col3:
        st.metric('Avg', str(round(avg_funding)) + 'cr')
    with col4:
        st.metric('Funded_startups',num_startup)

    st.header('MoM graph')
    selected_option = st.selectbox('Select Type',['Total','Count'])
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')

    fig3, ax3 = plt.subplots()
    ax3.plot(temp_df['x_axis'], temp_df['amount'])

    st.pyplot(fig3)


def load_investor_details(investor):
    st.title(investor)
    #load the recent 5 investment of investor
    last_5df = df[df['investor'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last_5df)
    col1 , col2 = st.columns(2)
    with col1:
            # biggest investments
            big_series = df[df['investor'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(
                ascending=False).head()
            st.subheader('Biggest Investments')
            fig, ax = plt.subplots()
            ax.bar(big_series.index, big_series.values)

            st.pyplot(fig)

    with col2:
        verical_series = df[df['investor'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors invested in')
        fig1, ax1 = plt.subplots()
        ax1.pie(verical_series, labels=verical_series.index,autopct="%0.01f%%")

        st.pyplot(fig1)

        print(df.info())

        df['year'] = df['date'].dt.year
        year_series = df[df['investor'].str.contains(investor)].groupby('year')['amount'].sum()

        st.subheader('YoY Investment')
        fig2, ax2 = plt.subplots()
        ax2.plot(year_series.index, year_series.values)

        st.pyplot(fig2)
st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':
        load_overall_analysis()
elif option == 'Startup':
    st.sidebar.selectbox('Select Startup',df['startup'].unique().tolist())
    st.title('StartUp Analysis')
    btn1 = st.sidebar.button('Find StartUp Detail')
else:
    selected_investor = st.sidebar.selectbox('Select Startup',sorted(set(df['investor'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Detail')
    if btn2:
        load_investor_details(selected_investor)