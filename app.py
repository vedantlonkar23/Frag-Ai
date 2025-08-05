import streamlit as st
import sys
import traceback

# Add error handling for imports
try:
    from components.general_section import show_general_section
    from components.maker_section import show_maker_section
    IMPORTS_SUCCESSFUL = True
except Exception as e:
    IMPORTS_SUCCESSFUL = False
    st.error(f"Import error: {str(e)}")
    st.error(f"Full traceback: {traceback.format_exc()}")

st.set_page_config(page_title='Fragrance Recommendation App', layout='wide')

def main():
    if not IMPORTS_SUCCESSFUL:
        st.error("Failed to import required modules. Please check the error messages above.")
        return
    
    st.sidebar.title('Navigation')
    section = st.sidebar.radio('Go to', ['General Fragrance Section', 'Fragrance Maker Section'])

    if section == 'General Fragrance Section':
        show_general_section()
    elif section == 'Fragrance Maker Section':
        show_maker_section()

if __name__ == '__main__':
    main()
