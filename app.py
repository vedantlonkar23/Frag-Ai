import streamlit as st
from components.general_section import show_general_section
from components.maker_section import show_maker_section

st.set_page_config(page_title='Fragrance Recommendation App', layout='wide')

def main():
    st.sidebar.title('Navigation')
    section = st.sidebar.radio('Go to', ['General Fragrance Section', 'Fragrance Maker Section'])

    if section == 'General Fragrance Section':
        show_general_section()
    elif section == 'Fragrance Maker Section':
        show_maker_section()

if __name__ == '__main__':
    main()
