# core package
import streamlit as st

# DB fanctions packages
from db_fxns import *

# this def run_task_page() will be used in the app.py
def run_task_page():
    # If there are no tables, this code makes a new table automatically
    create_table()
    
    # set the sub header
    st.subheader("Post and Update Tasks")
    
    # set the sub menu in this sidebar
    submenu = st.sidebar.selectbox("SubMenu", ["Add Task", "Edit Task"])
    
    
    
    
    
    # make Add Task page
    if submenu == "Add Task":
        # set the sub header
        st.subheader("Add Task")
        
        # set the page layout
        # make two areas on the main area
        col1, col2 = st.columns(2)
        
        # the task_doer and the task_name input area will be located in the left
        with col1:
            task_doer = st.text_input("Task Doer")
            task_name = st.text_area("Task")
        
        # the task_status and the task_due_date input area will be located in the right
        with col2:
            task_status = st.selectbox("Status", ["ToDo", "Done", "Doing", "Uncertain"])
            task_due_date = st.date_input("Task Due Date")
        
        # if you push this button, the data will be in the database
        if st.button("Add Task"):
            add_data(task_doer, task_name, task_status, task_due_date)
            st.success(f"Added {task_name}")
            
        # result will be shown
        result = view_all_tasks()
        st.write(result)
    
    
    
    
    # make Edit Task page
    elif submenu == "Edit Task":
        # set the sub header
        st.subheader("Update/Edit Task")
        
       
        # all data in the database will be shown and we can select one in this select box
        list_of_tasks = [i[0] for i in view_all_task_names()]    
        selected_task = st.selectbox("Task to be edited", list_of_tasks)
        
        # we can get the detail data selected above
        task_result = get_task_by_task_name(selected_task)
        st.write(task_result)
        
        # the below we can edit the imformation, so this sentense asks the question
        st.write("How do you edit?")
        
        # get the old data information
        if task_result:
            task_doer = task_result[0][0]
            task_name = task_result[0][1]
            task_status = task_result[0][2]
            task_due_date = task_result[0][3]
            
            # set the layout
            col1,col2 = st.columns(2)
            
            # new_task_doer and new_task_name input area will be left with old data as the defalut
            with col1:
                new_task_doer = st.text_input("Task Doer",task_doer)
                new_task_name = st.text_area("Task",task_name)

            # new_task_status and new_task_due_date input area will be left with old data as the defalut
            with col2:
                new_task_status = st.text_input("Status",task_status)
                new_task_due_date = st.date_input(task_due_date)
            
            # ifyou push the button, the data in the database will be updated
            if st.button("Update Task"):
                edit_task_data(new_task_doer,new_task_name,new_task_status,new_task_due_date,task_doer,task_name,task_status,task_due_date)
                st.success(f"Added {task_name}")

        # the all task will be shown
        result = view_all_tasks()
        st.write(result)
    
    