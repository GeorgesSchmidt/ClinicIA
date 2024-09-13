import streamlit as st 
from streamlit_option_menu import option_menu
import about, account, trending, your_post, home

st.set_page_config(
    page_title='Pondering',
)

class MultiApp:
    def __init__(self) -> None:
        self.apps = []
        
    def add_app(self, title, function):
        self.apps.append({
            'title': title,
            'function': function
        })
        
    def run():
        with st.sidebar:
            app = option_menu(
                menu_title='Pondering',
                options=['Home', 'Account', 'Trending', 'YourPost'],
                icons=['house-fill', 'person-circle'],
                default_index=1
            )
        if app == 'Home':
            home.app()
            
        if app == 'Account':
            account.app()
            
        if app == 'Trending':
            trending.app()
            
        if app == 'YourPost':
            your_post.app()
    run()

