import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
        
    
    check_df = pd.read_csv("predicted.csv")
    check_df['Output'] = np.where(check_df['Potability'] == check_df['Predicted Potability'], "True", "False")

    st.subheader("This is the comparisson")
    st.write(check_df) 
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Accuracy of the Prediction")
        create_pie_chart(check_df, 'Output', size=(6, 4)) 
        
if __name__ == "__main__":
    main()