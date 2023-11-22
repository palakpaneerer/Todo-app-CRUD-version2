# core package
import streamlit as st

# EDA package
import pandas as pd

# DB fanctions packages
from db_fxns import *


# this def run_home_page() will be used in the app.py
def run_home_page():
    
    # this sub menu will be appeared on the side bar
    choice = st.sidebar.selectbox("SubMenu", ["My Tasks","Search"])
    
    # the data frame with all task information is shown
    with st.expander("View All Task"):
        result = view_all_tasks()
        df = pd.DataFrame(result, columns=["Task Doer", "Task name", "Task Status", "Task Due Date"])
        st.dataframe(df)
    
    # if you will choose "My Tasks" in the side bar, you will see here 
    if choice == "My Tasks":
        # set the sub header
        st.subheader("My Tasks")
        
        # set the layout
        c1, c2 = st.columns([1,3])
    
        # you can choose one task to see the detail information on the left side
        with c1:
            st.info("Task List")
            list_of_tasks = [i[0] for i in view_all_task_names()]
            selected_task = st.selectbox("Your Task", list_of_tasks)

        # you can see the detail data according to your choice on the right side            
        with c2:
            st.info("Details")
            task_result = get_task_by_task_name(selected_task)
            task_doer = task_result[0][0]
            task_name = task_result[0][1]
            task_status = task_result[0][2]
            task_due_date = task_result[0][3]
            st.write(f"Task Doer: {task_doer}")
            st.write(f"Task name: {task_name}")
            st.write(f"Task status: {task_status}")
            st.write(f"Task Due Date: {task_due_date}")
    
    else:
        # set the sub header
        st.subheader("Search Task")
        
        # set the searcing term and field to search as you want
        search_term = st.text_input("Search Term")
        search_choice = st.radio("Field To Search", ("Task Doer", "Task Name"))
        
        # if you push this button, this system start to search the data according to your input searching infomation 
        if st.button("Search"):        
            if search_choice == "Task Name":
                search_result = get_task_by_task_name(search_term)
                st.write(search_result)
            else:
                search_result = get_task_by_task_doer(search_term)
                st.write(search_result)