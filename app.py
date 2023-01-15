import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px

df= pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")

df=df.sort_values(by=['marital'], ascending=False)

st.set_page_config(
    page_title = "Real-Time Data Science Dashborad",
    layout = 'wide'
)

# Dashboard Title
st.title("Real-Time / Live Data Science Dashboard")

# Top level filter

job_filter = st.selectbox("Select the Job", pd.unique(df["job"]))

## creating a single element container
placeholder = st.empty()

## Dataframe filter
df = df[df["job"]==job_filter]

# Near time/ Live feed simulation

for sec_1 in range(200):
    # while True: ( when we have to deploy code)

    df['age_new']= df['age'] * np.random.choice(range(1,5))
   


       
    df['balance_new'] = df['balance'] * np.random.choice(range(1,5))
 
    # Creating KPIs
    avg_age = np.mean(df["age_new"])
    count_married = int(df[(df["marital"]== 'married')]['marital'].count() + np.random.choice(range(1,3)))
    balance = np.mean(df['balance_new'])

    with placeholder.container():
# Create 3 columns with respective metrics and KPIs
        kpi1, kpi2, kpi3 = st.columns(3)
        kpi1.metric(label= "Age", value= round(avg_age), delta= round(avg_age)-10)
        kpi2.metric(label="Married Count", value = int(count_married), delta = -10 + count_married)
        kpi3.metric(label= "A/c Balance $", value= f"${round(balance,2)}", delta= -round(balance/count_married)* 100)

        # Create 2 columns for chart
        fig_col1, fig_col2 = st.columns(2)
       # print(df["marital"])
        with fig_col1:
            st.markdown("### Heat Map Plot")

            fig = px.density_heatmap(data_frame= df, y= 'age_new', x = 'marital')
            st.write(fig)
        with fig_col2:
            st.markdown('### Histogram Plot')
            fig2 = px.histogram(data_frame = df, x= 'age_new')
            st.write(fig2)
        st.markdown('### Detailed Data View')
        st.dataframe(df)
        time.sleep(0.5)
