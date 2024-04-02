import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from streamlit_option_menu import option_menu



# Function to create pie chart
def create_pie_chart(dataframe, column,  size=(4, 4)):
    counts = dataframe[column].value_counts()
    fig, ax = plt.subplots(figsize=size)
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)
    
# Main function
def main():
    
    st.set_page_config(layout="wide")
    
    LOGO_SIDEBAR_URL = "https://static.wixstatic.com/media/dd11e9_145d7c62f0a647979cbe9e9adef92f5b~mv2.png/v1/fill/w_344,h_60,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/White%20logo%20with%20tagline%20on%20Transparent%20b.png"

    if LOGO_SIDEBAR_URL: st.sidebar.image(
            LOGO_SIDEBAR_URL,             
            caption= 'Sharing expertise. Building relationships'
    )
     
    
    st.header('WATER POTABILITY PREDICTION - DRAFT')
    
    
    st.subheader('Input the Data CSV File Here')

    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        if st.button('Show the Uploaded file'):
            
            st.subheader('This is the Data File')
            st.write(df)    
            st.button('Hide the file') 
    st.write('A sample dataset of water quality level has been uploded for evaluation purposes!')
    st.write('You can check the uploaded raw file, the dataset after the preediction and the accuracy of the ML model from the left menu')
        
if __name__ == "__main__":
    main()