import streamlit as st
import pandas as pd

def filter_by_link_sections(df, link_sections):
    filtered_df = df[df['Link section'].isin(link_sections)]
    return filtered_df

# Streamlit app
st.title('Filter CSV Data by Link Section')

# File uploader
uploaded_file = st.file_uploader('Upload your CSV file', type='csv')

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Display the dataframe
    st.write('Dataframe:')
    st.write(df)
    
    # Input for Link sections
    link_sections_input = st.text_input('Enter Link sections (comma-separated)', 'A1,B2,C3')
    
    if link_sections_input:
        link_sections = [section.strip() for section in link_sections_input.split(',')]
        
        # Filter the dataframe
        filtered_df = filter_by_link_sections(df, link_sections)
        
        # Display the filtered dataframe
        st.write('Filtered Dataframe:')
        st.write(filtered_df)
