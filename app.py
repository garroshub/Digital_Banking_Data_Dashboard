import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import plotly.express as px

path = 'bank-full.csv'
bank_data = pd.read_csv(path,sep=';')
bank_data.loc[(bank_data['pdays'] == -1), 'pdays'] = 0
yes_df = bank_data.loc[(bank_data['y'] == 'yes'), :]
no_df = bank_data.loc[(bank_data['y'] == 'no'), :]


st.title('Bank marketing analysis dashboard')
st.markdown('Data set source:')
st.write('I got this data set from UCI Machine Learning Repository, and this data set was available from this article Moro et al., 2014.')

st.sidebar.title('What do tou want to see?')
st.sidebar.write('Here are some options so you can navigate through this dashboard.')
option = st.sidebar.selectbox('Options:', ('Data Summary', 'Age', 'Job', 'Duration',
                                           'Education', 'Default', 'Housing',
                                           'Loan', 'Contact', 'Previous outcome',
                                           'Previous campaign', 'Campaign',
                                            'Campaign response',
                                           'Correlation heatmap'))

if option == 'Data Summary':
    st.header('Data Summary')
    st.write('Here is some summary calculations of the data, I splitted into 3 dataframes for better understanding.')
    if st.sidebar.checkbox('Raw data sets'):
        st.subheader('Bank data')
        st.write(bank_data.head())

    if st.sidebar.checkbox('Summary calculations'):
        st.subheader('Bank data summary:')
        st.write(bank_data.describe())

    else: st.write('Pick something to see in the sidebar.')

if option == 'Age':
    st.header('Age frequencies')
    st.write('Here are the age frequencies count for 3 dataframes.')
    st.subheader('Bank data')
    fig1 = plt.figure()
    age_freq = sns.countplot(x=bank_data['age'])
    age_freq.set_xticklabels(age_freq.get_xticklabels(), rotation=40, ha="right")
    age_freq.xaxis.set_major_locator(ticker.MultipleLocator(5))
    st.pyplot(fig1)
    st.subheader('yes_df')
    fig2 = plt.figure()
    yes_age_freq = sns.countplot(x=yes_df['age'])
    yes_age_freq.set_xticklabels(yes_age_freq.get_xticklabels(), rotation=40, ha="right")
    yes_age_freq.xaxis.set_major_locator(ticker.MultipleLocator(5))
    st.pyplot(fig2)
    st.subheader('no_df')
    fig3 = plt.figure()
    no_age_freq = sns.countplot(x=no_df['age'])
    no_age_freq.set_xticklabels(no_age_freq.get_xticklabels(), rotation=40, ha="right")
    no_age_freq.xaxis.set_major_locator(ticker.MultipleLocator(5))
    st.pyplot(fig3)

if option == 'Duration':
    st.header('Duration frequencies')
    st.write('Here are the duration frequencies count for 3 dataframes.')
    st.subheader('Bank data')
    fig1 = plt.figure()
    duration_freq = sns.countplot(x=bank_data['duration'])
    duration_freq.set_xticklabels(duration_freq.get_xticklabels(), rotation=40, ha="right")
    duration_freq.xaxis.set_major_locator(ticker.MultipleLocator(100))
    st.pyplot(fig1)
    st.subheader('yes_df')
    fig2 = plt.figure()
    yes_duration_freq = sns.countplot(x=yes_df['duration'])
    yes_duration_freq.set_xticklabels(yes_duration_freq.get_xticklabels(), rotation=40, ha="right")
    yes_duration_freq.xaxis.set_major_locator(ticker.MultipleLocator(100))
    st.pyplot(fig2)
    st.subheader('no_df')
    fig3 = plt.figure()
    no_duration_freq = sns.countplot(x=no_df['duration'])
    no_duration_freq.set_xticklabels(no_duration_freq.get_xticklabels(), rotation=40, ha="right")
    no_duration_freq.xaxis.set_major_locator(ticker.MultipleLocator(100))
    st.pyplot(fig3)

if option == 'Job':
    st.header('Job frequencies')
    st.write('Here are the job frequencies count for 3 dataframes.')
    st.subheader('Bank data')
    fig1 = plt.figure()
    job_freq = sns.countplot(x=bank_data['job'])
    job_freq.set_xticklabels(job_freq.get_xticklabels(), rotation=40, ha="right")
    st.pyplot(fig1)
    st.subheader('yes_df')
    fig2 = plt.figure()
    yes_job_freq = sns.countplot(x=yes_df['job'])
    yes_job_freq.set_xticklabels(yes_job_freq.get_xticklabels(), rotation=40, ha="right")
    st.pyplot(fig2)
    st.subheader('no_df')
    fig3 = plt.figure()
    no_job_freq = sns.countplot(x=no_df['job'])
    no_job_freq.set_xticklabels(no_job_freq.get_xticklabels(), rotation=40, ha="right")
    st.pyplot(fig3)

if option == 'Education':
    st.header('Education frequencies')
    st.write('Here are the education frequencies count for 3 dataframes.')
    st.subheader('Bank data')
    fig1 = plt.figure()
    education_freq = sns.countplot(x=bank_data['education'])
    education_freq.set_xticklabels(education_freq.get_xticklabels(), rotation=40, ha="right")
    st.pyplot(fig1)
    st.subheader('yes_df')
    fig2 = plt.figure()
    yes_education_freq = sns.countplot(x=yes_df['education'])
    yes_education_freq.set_xticklabels(yes_education_freq.get_xticklabels(), rotation=40, ha="right")
    st.pyplot(fig2)
    st.subheader('no_df')
    fig3 = plt.figure()
    no_education_freq = sns.countplot(x=no_df['education'])
    no_education_freq.set_xticklabels(no_education_freq.get_xticklabels(), rotation=40, ha="right")
    st.pyplot(fig3)

if option == 'Default':
    st.header('Default frequencies')
    st.write('Here are the default frequencies count for 3 dataframes.')
    st.subheader('Bank data')
    fig1 = plt.figure()
    default_freq = sns.countplot(x=bank_data['default'])
    st.pyplot(fig1)
    st.subheader('yes_df')
    fig2 = plt.figure()
    yes_default_freq = sns.countplot(x=yes_df['default'])
    st.pyplot(fig2)
    st.subheader('no_df')
    fig3 = plt.figure()
    no_default_freq = sns.countplot(x=no_df['default'])
    st.pyplot(fig3)

if option == 'Housing':
    st.header('Housing frequencies')
    st.write('Here are the housing frequencies count for 3 dataframes.')
    st.subheader('Bank data')
    fig1 = plt.figure()
    housing_freq = sns.countplot(x=bank_data['housing'])
    st.pyplot(fig1)
    st.subheader('yes_df')
    fig2 = plt.figure()
    yes_housing_freq = sns.countplot(x=yes_df['housing'])
    st.pyplot(fig2)
    st.subheader('no_df')
    fig3 = plt.figure()
    no_housing_freq = sns.countplot(x=no_df['housing'])
    st.pyplot(fig3)

if option == 'Loan':
    st.header('Loan frequencies')
    st.write('Here are the loan frequencies count for 3 dataframes.')
    st.subheader('Bank data')
    fig1 = plt.figure()
    loan_freq = sns.countplot(x=bank_data['loan'])
    st.pyplot(fig1)
    st.subheader('yes_df')
    fig2 = plt.figure()
    yes_loan_freq = sns.countplot(x=yes_df['loan'])
    st.pyplot(fig2)
    st.subheader('no_df')
    fig3 = plt.figure()
    no_loan_freq = sns.countplot(x=no_df['loan'])
    st.pyplot(fig3)

if option == 'Contact':
    st.header('Contact frequencies')
    st.write('Here are the contact frequencies count for 3 dataframes.')
    st.subheader('Bank data')
    fig1 = plt.figure()
    contact_freq = sns.countplot(x=bank_data['contact'])
    st.pyplot(fig1)
    st.subheader('yes_df')
    fig2 = plt.figure()
    yes_contact_freq = sns.countplot(x=yes_df['contact'])
    st.pyplot(fig2)
    st.subheader('no_df')
    fig3 = plt.figure()
    no_contact_freq = sns.countplot(x=no_df['contact'])
    st.pyplot(fig3)

if option == 'Previous outcome':
    st.header('Previous outcome frequencies')
    st.write('Here are the previous outcome frequencies count for 3 dataframes.')
    st.subheader('Bank data')
    fig1 = plt.figure()
    poutcome_freq = sns.countplot(x=bank_data['poutcome'])
    st.pyplot(fig1)
    st.subheader('yes_df')
    fig2 = plt.figure()
    yes_poutcome_freq = sns.countplot(x=yes_df['poutcome'])
    st.pyplot(fig2)
    st.subheader('no_df')
    fig3 = plt.figure()
    no_poutcome_freq = sns.countplot(x=no_df['poutcome'])
    st.pyplot(fig3)

if option == 'Previous campaign':
    st.header('Previous campaign frequencies')
    st.write('Here are the previous campaign frequencies count for 3 dataframes.')
    st.subheader('Bank data')
    fig1 = plt.figure()
    previous_freq = sns.countplot(x=bank_data['previous'])
    previous_freq.set_xticklabels(previous_freq.get_xticklabels(), rotation=40, ha="right")
    previous_freq.xaxis.set_major_locator(ticker.MultipleLocator(3))
    st.pyplot(fig1)
    st.subheader('yes_df')
    fig2 = plt.figure()
    yes_previous_freq = sns.countplot(x=yes_df['previous'])
    yes_previous_freq.set_xticklabels(yes_previous_freq.get_xticklabels(), rotation=40, ha="right")
    yes_previous_freq.xaxis.set_major_locator(ticker.MultipleLocator(3))
    st.pyplot(fig2)
    st.subheader('no_df')
    fig3 = plt.figure()
    no_previous_freq = sns.countplot(x=no_df['previous'])
    no_previous_freq.set_xticklabels(no_previous_freq.get_xticklabels(), rotation=40, ha="right")
    no_previous_freq.xaxis.set_major_locator(ticker.MultipleLocator(3))
    st.pyplot(fig3)

if option == 'Campaign':
    st.header('Campaign frequencies')
    st.write('Here are the campaign frequencies count for 3 dataframes.')
    st.subheader('Bank data')
    fig1 = plt.figure()
    campaign_freq = sns.countplot(x=bank_data['campaign'])
    campaign_freq.set_xticklabels(campaign_freq.get_xticklabels(), rotation=40, ha="right")
    campaign_freq.xaxis.set_major_locator(ticker.MultipleLocator(3))
    st.pyplot(fig1)
    st.subheader('yes_df')
    fig2 = plt.figure()
    yes_campaign_freq = sns.countplot(x=yes_df['campaign'])
    yes_campaign_freq.set_xticklabels(yes_campaign_freq.get_xticklabels(), rotation=40, ha="right")
    yes_campaign_freq.xaxis.set_major_locator(ticker.MultipleLocator(3))
    st.pyplot(fig2)
    st.subheader('no_df')
    fig3 = plt.figure()
    no_campaign_freq = sns.countplot(x=no_df['campaign'])
    no_campaign_freq.set_xticklabels(no_campaign_freq.get_xticklabels(), rotation=40, ha="right")
    no_campaign_freq.xaxis.set_major_locator(ticker.MultipleLocator(3))
    st.pyplot(fig3)

if option == 'Campaign response':
    st.subheader('Campaign response')
    st.write('Here is the response from the customers to the campaign.')
    fig1 = plt.figure()
    y_freq = sns.countplot(x = bank_data['y'])
    st.pyplot(fig1)

if option == 'Correlation heatmap':
    st.subheader('Correlation heatmap')
    st.write('Here is the correlation matrix plotted in a heatmap for easier visualization.')
    fig1 = plt.figure()
    corr_map = sns.heatmap(bank_data.corr(), annot=True)
    st.pyplot(fig1)
