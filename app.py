import streamlit as st
import pandas as pd

def filter_by_link_sections(df, link_sections):
    filtered_df = df[df['Link section'].isin(link_sections)]
    filtered_df = filtered_df.drop_duplicates(subset=['Link section', 'Site category', 'IL Value'])
    return filtered_df

# Streamlit app
st.title('Filter CSV Data by Link Section')

# File uploader for the main CSV file
uploaded_file = st.file_uploader('Upload your main CSV file', type='csv')

# File uploader for the Link sections CSV file
link_sections_file = st.file_uploader('Upload your Link sections CSV file', type='csv')

if uploaded_file is not None and link_sections_file is not None:
    # Read the main CSV file
    df = pd.read_csv(uploaded_file)
    
    # Read the Link sections CSV file
    link_sections_df = pd.read_csv(link_sections_file)
    
    # Extract the Link sections from the Link sections CSV file
    link_sections = link_sections_df.iloc[:, 0].tolist()
    
    # Display the dataframes
    st.write('Main Dataframe:')
    st.write(df)
    
    st.write('Link Sections Dataframe:')
    st.write(link_sections_df)
    
    # Filter the dataframe
    filtered_df = filter_by_link_sections(df, link_sections)
    
    # Display the filtered dataframe
    st.write('Filtered Dataframe:')
    st.write(filtered_df)
    
    # Download the filtered dataframe as a CSV file
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Filtered Data as CSV",
        data=csv,
        file_name='filtered_data.csv',
        mime='text/csv',
    )
