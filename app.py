import streamlit as st
import pandas as pd

def filter_by_link_sections_and_lane(df, link_sections):
    filtered_df = df[df['Link section'].isin(link_sections)]
    
    # Identify duplicates across lanes
    duplicates = filtered_df.duplicated(subset=['Link section', 'Site category', 'IL Value'], keep=False)
    
    # Separate duplicates and non-duplicates
    duplicates_df = filtered_df[duplicates]
    non_duplicates_df = filtered_df[~duplicates]
    
    # For duplicates, keep only those with Lane 'CL1' and mark as 'all lanes'
    duplicates_df = duplicates_df[duplicates_df['Lane'] == 'CL1']
    duplicates_df['Lane'] = 'all lanes'
    
    # Combine the dataframes
    final_filtered_df = pd.concat([non_duplicates_df, duplicates_df]).drop_duplicates()
    
    return final_filtered_df

# Streamlit app
st.title('Filter CSV Data by Link Section and Lane')

# File uploader for the main CSV file
uploaded_file = st.file_uploader('Upload SCRIM_IL master sheet', type='csv')

# File uploader for the Link sections CSV file
link_sections_file = st.file_uploader('Upload your Link sections CSV file', type='csv')

if uploaded_file is not None and link_sections_file is not None:
    # Read the main CSV file
    df = pd.read_csv(uploaded_file)
    
    # Read the Link sections CSV file
    link_sections_df = pd.read_csv(link_sections_file)
    
    # Extract the Link sections from the Link sections CSV file
    link_sections = link_sections_df.iloc[:, 1].tolist()
    
    # Display the dataframes
    st.write('Main Dataframe:')
    st.write(df)
    
    st.write('Link Sections Dataframe:')
    st.write(link_sections_df)
    
    # Filter the dataframe
    filtered_df = filter_by_link_sections_and_lane(df, link_sections)
    
    # Merge the filtered dataframe with the Link sections dataframe to include site numbers
    filtered_df = filtered_df.merge(link_sections_df, on='Link section', how='left').drop_duplicates()
    
    # Display the filtered dataframe
    st.write('Filtered Dataframe:')
    st.write(filtered_df)
    
    # Download the filtered dataframe as a CSV file
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Filtered Data as CSV",
        data=csv,
        file_name='IL_Sitecategory.csv',
        mime='text/csv',
    )
