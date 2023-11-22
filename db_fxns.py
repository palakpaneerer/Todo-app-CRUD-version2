# core package
import sqlite3

# set connect the datbase
conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()





# make a creating table function
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS taskstable(task_doer TEXT, task_name TEXT, task_status TEXT, task_due_date DATE)')

# make an adding data function
def add_data(task_doer, task_name, task_status, task_due_date):
    c.execute('INSERT INTO taskstable(task_doer, task_name, task_status, task_due_date) VALUES (?,?,?,?)', (task_doer, task_name, task_status, task_due_date))
    conn.commit()
    
# make a viewing data function
def view_all_tasks():
    c.execute('SELECT * FROM taskstable')
    data = c.fetchall()
    return data

# make a viewing unique data function
def view_all_task_names():
    c.execute('SELECT DISTINCT task_name FROM taskstable')
    data = c.fetchall()
    return data

# make a searching and viewing specific data using task name function
def get_task_by_task_name(task_name):
    c.execute('SELECT * FROM taskstable WHERE task_name = ?', (task_name,))  # must be taple formart in the last part such as (task_name,)
    data = c.fetchall()
    return data

# make a searching and viewing specific data function usnig task doer
def get_task_by_task_doer(task_doer):
    c.execute('SELECT * FROM taskstable WHERE task_doer = ?', (task_doer,))  # must be taple formart in the last part such as (task_name,)
    data = c.fetchall()
    return data

# make an editing data function
def edit_task_data(new_task_doer,new_task_name,new_task_status,new_task_due_date,task_doer,task_name,task_status,task_due_date):
	c.execute("UPDATE taskstable SET task_doer =?,task_name =?,task_status=?,task_due_date=? WHERE task_doer=? and task_name=? and task_status=? and task_due_date=?",(new_task_doer,new_task_name,new_task_status,new_task_due_date,task_doer,task_name,task_status,task_due_date))
	conn.commit()
	data = c.fetchall()
	return data

# make a delete function
def delete_data(task_name):
    c.execute("DELETE FROM taskstable WHERE task_name=?", (task_name,)) # must be tuple format in the last part such as (task_name,)
    conn.commit()