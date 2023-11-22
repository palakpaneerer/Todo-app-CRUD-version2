# core package
import streamlit as st

# EDA package
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib

# DB fanctions packages
from db_fxns import *



# this def run_manage_page() will be used in the app.py
def run_manage_page():
    
    # this sub menu will be appeared on the side bar
    submenu = ["Delete Task", "Analytics"]
    choice = st.sidebar.selectbox("SubMenu", submenu)
    
    # if you choose "Delete Task", you will see here
    if choice == "Delete Task":
        # set the sub header
        st.subheader("Delete Task")
        
        # show the all data in dataframe format
        result = view_all_tasks()
        df = pd.DataFrame(result, columns=["Task Doer", "Task name", "Task Status", "Task Due Date"])
        st.dataframe(df)
        
        # you can select every unique task name to delete
        unique_list = [i[0] for i in view_all_task_names()]
        delete_by_task_name = st.selectbox("Task to Delete", unique_list)
        
        # this is just warning before deleting items
        st.warning(f"Do you delete {delete_by_task_name}?")
        
        # if you push this button, the data will be deleted in the dataframe
        if st.button("Delete"):
            delete_data(delete_by_task_name)
            st.info(f"Deleted{delete_by_task_name}")

        # you can confirm updated dataframe after deleting the item        
        with st.expander("current Database"):
            result = view_all_tasks()
            new_df = pd.DataFrame(result, columns=["Task Doer", "Task name", "Task Status", "Task Due Date"])
            st.dataframe(new_df)
    
    # if you choose "Analytics", you can see here 
    else:
        # set the sub header
        st.subheader("Analytics")
        
        # get the data frame data to use it in the three expander later
        result = view_all_tasks()
        df = pd.DataFrame(result, columns=["Task Doer", "Task name", "Task Status", "Task Due Date"])


        # if you click "View All Task" expander, you can see the all task data  
        with st.expander("View All Task"):
            st.dataframe(df)
        
        
        # if you click "Task Doer Stats" expander, you can see the task doer pie chart                      
        with st.expander("Task Doer Stats"):
            # visualise the data in data frame format
            new_df = df["Task Doer"].value_counts().to_frame()
            new_df = new_df.reset_index()
            st.dataframe(new_df)

            # visualise the data in pie chart format
            p1 = px.pie(new_df, names='Task Doer', values="count")
            st.plotly_chart(p1, use_container_width=True)           # "use_container_width" makes the pie chart fit with the web page width
        
        # if you click "Task Stats" expander, you can see the task doer pie chart
        with st.expander("Task Stats"):
            # visualise the data in data frame format
            new_task_df = df["Task name"].value_counts().to_frame()
            new_task_df = new_task_df.reset_index()
            st.dataframe(new_task_df)

            # visualise the data in pie chart format
            p2 = px.pie(new_task_df, names='Task name', values="count")
            st.plotly_chart(p2, use_container_width=True)           # "use_container_width" makes the pie chart fit with the web page width
            
 
            
            
        
        
            