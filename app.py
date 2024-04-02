import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import warnings
warnings.filterwarnings("ignore")

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
    st.header('WATER POTABILITY PREDICTION - DRAFT')
    
    col1, col2 = st.columns(2)
    with col1:
        with st.expander('About this app'):

            st.write('A sample dataset of water quality level has been uploded!')
            st.image('https://static.wixstatic.com/media/dd11e9_145d7c62f0a647979cbe9e9adef92f5b~mv2.png/v1/fill/w_344,h_60,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/White%20logo%20with%20tagline%20on%20Transparent%20b.png', width=250)
  
    load_model = joblib.load('water_potability_model.joblib')
    
    uploaded_file = pd.read_csv("X_temp.csv")
    df = uploaded_file

    if st.button('Show the Uploaded file'):
        st.button('Hide the file') 
        st.subheader('This is the Data File')
        st.write(df)    

    scaler = MinMaxScaler()
    X = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    predictions = load_model.predict(X)
    predicted_pollution_df = pd.DataFrame({'Predicted Potability': predictions})
    merged_df = pd.concat([df, predicted_pollution_df], axis=1)

    if st.button('Show the Predicted file'):
        st.button('Hide the file') 
        st.subheader("This is the prediction")
        st.write(merged_df)    
         
    original_file = pd.read_csv("water_potability.csv")
    original_file['Potability'] = original_file['Potability'].replace({0: 'No', 1: 'Yes'})

    check_df = pd.concat([original_file, predicted_pollution_df], axis=1)
    check_df['Output'] = np.where(check_df['Potability'] == check_df['Predicted Potability'], "True", "False")

    if st.button('Show the Compared file'):
        st.button('Hide the file')
        st.subheader("This is the comparisson")
        st.write(check_df) 
        create_pie_chart(check_df, 'Output', size=(15, 3)) 
        
if __name__ == "__main__":
    main()