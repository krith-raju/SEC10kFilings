import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# CSS styles for better aesthetics
st.markdown("""
<style>
.big-font {
    font-size:30px !important;
    font-weight: bold;
}
.dataframe {
    border: 2px solid #f0f0f0;
    border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-font">Yearly Risk Visualization App</div>', unsafe_allow_html=True)

# Define risk categories based on keywords
risk_categories = {
    'Economic': ['economic', 'financial', 'market'],
    'Political': ['political', 'regulation', 'legislative'],
    'Natural Disasters': ['natural', 'earthquake', 'flood', 'disaster'],
    'Cybersecurity': ['cyber', 'data breach', 'hacking', 'security'],
    'Health': ['health', 'pandemic', 'disease', 'virus'],
    'Environmental': ['environmental', 'pollution', 'climate'],
    'Social': ['social', 'labor', 'public opinion'],
    'Technological': ['technological', 'innovation', 'tech'],
    'Operational': ['operational', 'logistics', 'supply chain'],
    'Other': ['other', 'miscellaneous', 'various']
}

def categorize_risk(risk_text):
    for category, keywords in risk_categories.items():
        if any(keyword in risk_text.lower() for keyword in keywords):
            return category
    return 'Other'

# Mapping of tickers to file names
ticker_to_file = {
    'AAPL': 'C:/users/rajun/downloads/final/aapl_csv_data.csv',
    'GOOG': 'C:/users/rajun/downloads/final/goog_csv_data.csv'
}

# User inputs for tickers, starting empty
ticker1 = st.text_input("Enter Primary Stock Ticker (e.g., AAPL, GOOG)", '').upper()
ticker2 = st.text_input("Enter Secondary Stock Ticker (optional)", '').upper()

def load_and_process_data(ticker):
    if ticker in ticker_to_file and os.path.exists(ticker_to_file[ticker]):
        data = pd.read_csv(ticker_to_file[ticker])
        data['Risk Category'] = data['Risk'].apply(categorize_risk)
        return data
    else:
        st.error(f"Ticker {ticker} not found or file does not exist.")
        return None

data1 = load_and_process_data(ticker1) if ticker1 else None
data2 = load_and_process_data(ticker2) if ticker2 else None

# Create column layout for side-by-side comparison if both tickers are provided
if data1 is not None and data2 is not None:
    col1, col2 = st.columns(2)
else:
    col1, col2 = st.container(), None

# Display data for the first ticker
if data1 is not None:
    with col1:
        st.write(f"Comprehensive Risk Summary for {ticker1}:")
        risk_summary1 = data1.groupby(['Year', 'Risk Category']).size().unstack(fill_value=0)
        st.dataframe(risk_summary1)

        # Bar graph for the first ticker
        fig1, ax1 = plt.subplots()
        risk_summary1.plot(kind='bar', stacked=True, ax=ax1)
        ax1.set_ylabel('Count of Risks')
        ax1.set_title(f'Risk Counts by Year for {ticker1}')
        st.pyplot(fig1)

        # Line graph and slider for "Other" risks for the first ticker
        if 'Other' in risk_summary1:
            fig3, ax3 = plt.subplots()
            ax3.plot(risk_summary1.index, risk_summary1['Other'], marker='o', linestyle='-', color='red')
            ax3.set_title(f'"Other" Risks for {ticker1}')
            ax3.set_xlabel('Year')
            ax3.set_ylabel('Count')
            ax3.grid(True)
            st.pyplot(fig3)

            year_to_view1 = st.select_slider(f'Select a Year to View Details of "Other" Risks for {ticker1}', options=risk_summary1.index.unique())
            detailed_data1 = data1[(data1['Year'] == year_to_view1) & (data1['Risk Category'] == 'Other')]
            st.write(f'Detailed "Other" Risk Data for {ticker1} in {year_to_view1}:')
            st.dataframe(detailed_data1)

# Display data for the second ticker if provided
if data2 is not None and col2:
    with col2:
        st.write(f"Comprehensive Risk Summary for {ticker2}:")
        risk_summary2 = data2.groupby(['Year', 'Risk Category']).size().unstack(fill_value=0)
        st.dataframe(risk_summary2)

        # Bar graph for the second ticker
        fig2, ax2 = plt.subplots()
        risk_summary2.plot(kind='bar', stacked=True, ax=ax2)
        ax2.set_ylabel('Count of Risks')
        ax2.set_title(f'Risk Counts by Year for {ticker2}')
        st.pyplot(fig2)

        # Line graph and slider for "Other" risks for the second ticker
        if 'Other' in risk_summary2:
            fig4, ax4 = plt.subplots()
            ax4.plot(risk_summary2.index, risk_summary2['Other'], marker='o', linestyle='-', color='red')
            ax4.set_title(f'"Other" Risks for {ticker2}')
            ax4.set_xlabel('Year')
            ax4.set_ylabel('Count')
            ax4.grid(True)
            st.pyplot(fig4)

            year_to_view2 = st.select_slider(f'Select a Year to View Details of "Other" Risks for {ticker2}', options=risk_summary2.index.unique())
            detailed_data2 = data2[(data2['Year'] == year_to_view2) & (data2['Risk Category'] == 'Other')]
            st.write(f'Detailed "Other" Risk Data for {ticker2} in {year_to_view2}:')
            st.dataframe(detailed_data2)