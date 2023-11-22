# core package
import streamlit as st

# other pages other than this top page
from home_page import run_home_page
from post_page import run_task_page
from manage_page import run_manage_page





def main():
    # set the title    
    st.title("Simple CRUD App (TaskList)")
    
    # make options in the sidebar
    menu = ["Home", "Tasks", "Manage", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    
    
    # make a home page
    if choice == "Home":
        # set the sub title
        st.subheader("Home")
        
        # use the page contents defined in home_page.py
        run_home_page()
    
    
    
    # make a tasks paage
    if choice == "Tasks":
        # set the sub title
        st.subheader("Post Tasks")
        
        # use the page contents defined in post_page.py
        run_task_page()
     
     
     
    # make a manage page 
    if choice == "Manage":
        st.subheader("Manage Tasks")

        # use the page contents defined in manage_page.py
        run_manage_page()


    # make an abount page 
    if choice == "About":
        st.subheader("About")





if __name__ == '__main__':
    main()

