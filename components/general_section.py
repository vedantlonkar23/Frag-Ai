# general_section.py
import streamlit as st
import pandas as pd
from utils.recommendation import recommend_perfumes

def show_general_section():
    st.title('Fragrance Finder')
    
    # Load Data
    df = pd.read_csv('data/fra_cleaned_processed.csv', encoding='ISO-8859-1')

    # Filters Section - Gender, Occasion, Brand
    st.subheader('Filter Your Preferences')
    brands = st.multiselect('Select Brand(s)', df['Brand'].unique()) if 'Brand' in df.columns else []
    genders = st.multiselect('Select Gender(s)', df['Gender'].unique()) if 'Gender' in df.columns else []
    occasions = st.multiselect('Select Occasion(s)', df['Occasion'].unique()) if 'Occasion' in df.columns else []
    moods = st.multiselect('Select Mood(s)', df['Mood'].unique()) if 'Mood' in df.columns else []

    # Apply Filters and Show Relevant Perfumes
    filtered_df = df.copy()
    if brands:
        filtered_df = filtered_df[filtered_df['Brand'].isin(brands)]
    if genders:
        filtered_df = filtered_df[filtered_df['Gender'].isin(genders)]
    if occasions:
        filtered_df = filtered_df[filtered_df['Occasion'].isin(occasions)]
    if moods:
        filtered_df = filtered_df[filtered_df['Mood'].isin(moods)]

    if not filtered_df.empty:
        st.write('### Relevant Perfumes Based on Your Selection')
        st.write(filtered_df[['Perfume']])
    else:
        st.write('No matching perfumes found. Try adjusting your filters.')

    # Recommendation Section
    if 'Perfume' in df.columns and not filtered_df.empty:
        selected_perfume = st.selectbox('Select a perfume for further recommendations', filtered_df['Perfume'].unique())
        if st.button('Recommend Similar Perfumes'):
            recommendations = recommend_perfumes(selected_perfume, df)
            st.write('### Recommended Perfumes Based on Your Selection')
            st.write(recommendations)

    # Explore and Discover Section at the End
    st.write('## Explore and Discover All Fragrances')
    if 'Perfume' in df.columns:
        st.write(df[['Perfume']])
    else:
        st.error("No Perfume column found.")

    st.write('Enjoy discovering your perfect fragrance!')
