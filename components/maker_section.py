import streamlit as st
import pandas as pd
from utils.ingredient_suggestion import suggest_ingredients

def show_maker_section():
    st.title('Fragrance Maker - Ingredient Suggestion')
    
    # Load data
    df = pd.read_csv('data/fra_cleaned_processed.csv', encoding='ISO-8859-1')

    # Get unique notes from dataset
    all_notes = pd.concat([df[col] for col in ['Top', 'Middle', 'Base'] if col in df.columns]).dropna().str.split(', ').explode().unique()

    # Input for perfumers
    selected_note = st.selectbox('Select a primary note for your fragrance', all_notes)

    if st.button('Suggest Ingredients'):
        suggestions = suggest_ingredients(selected_note, df)
        if 'Note' in suggestions.columns:
            st.write(f"Based on your primary note ({selected_note}), consider these complementary ingredients:")
            st.write(suggestions[['Note']])
        else:
            st.error("No 'Note' column found in the suggestion data.")
    
    # Add Perfume Section
    st.title('Add Perfume Details')
    if 'Perfume' in df.columns:
        selected_perfume = st.selectbox('Select a perfume to view its notes', df['Perfume'].unique())
        perfume_details = df[df['Perfume'] == selected_perfume][[col for col in ['Top', 'Middle', 'Base'] if col in df.columns]]
        st.write('### Fragrance Notes')
        st.write(perfume_details)

    st.write('Create and explore your unique fragrance blend!')
